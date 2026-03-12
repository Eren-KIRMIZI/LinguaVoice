from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="VoiceTranslator API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY bulunamadı. .env dosyasına ekle.")

client = Groq(api_key=GROQ_API_KEY)

app.mount("/static", StaticFiles(directory="../frontend"), name="static")


class TranslateRequest(BaseModel):
    text: str
    source_lang: str = "Turkish"
    target_lang: str = "English"


class TranslateResponse(BaseModel):
    original: str
    translated: str
    source_lang: str
    target_lang: str


@app.get("/")
def serve_frontend():
    return FileResponse("../frontend/index.html")


@app.post("/translate", response_model=TranslateResponse)
async def translate(req: TranslateRequest):
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Metin boş olamaz.")

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        f"You are a professional translator. "
                        f"Translate the user's {req.source_lang} text to {req.target_lang}. "
                        f"Return ONLY the translated text. No explanations, no quotes, nothing else."
                    ),
                },
                {
                    "role": "user",
                    "content": req.text,
                },
            ],
            temperature=0.2,
            max_tokens=1024,
        )

        translated = response.choices[0].message.content.strip()

        return TranslateResponse(
            original=req.text,
            translated=translated,
            source_lang=req.source_lang,
            target_lang=req.target_lang,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Çeviri hatası: {str(e)}")