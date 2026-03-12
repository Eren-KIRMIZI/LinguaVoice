# VoiceTranslator

Mikrofondan Türkçe konuşursun, uygulama sesi yazıya döker, Groq API üzerinden İngilizceye çevirir ve çevrilen metni sesli olarak okur. Tüm bu adımlar tek bir web arayüzünde gerçekleşir.

---

https://github.com/user-attachments/assets/3c231520-d039-40fe-89e8-6b864732254b


## Ne İşe Yarar

Türkçe konuştuğun anda metin ekrana düşer. Arkada Groq'un sunduğu Llama 3.3 70B modeli bu metni İngilizceye çevirir. Çeviri tamamlanınca tarayıcının yerleşik ses sentezi devreye girerek sonucu yüksek sesle okur. İstersen dinle butonuna tıklayarak çeviriyi tekrar dinleyebilirsin.

---

## Kullanılan Teknolojiler

**Frontend** olarak saf HTML, CSS ve JavaScript kullanıldı. Harici bir framework tercih edilmedi. Ses kaydı için tarayıcının kendi Web Speech API'si kullanıldığından ek bir kütüphane kurulumu gerekmiyor. Sesli okuma için de aynı şekilde tarayıcı yerleşik Web Speech Synthesis API'sinden yararlanıldı.

**Backend** tarafında Python ile yazılmış bir FastAPI uygulaması çalışıyor. Frontend dosyaları da doğrudan bu uygulama üzerinden sunuluyor, yani ayrı bir sunucuya gerek yok.

**Çeviri motoru** olarak Groq API kullanıldı. Groq, büyük dil modellerini son derece hızlı çalıştıran bir altyapı sunuyor. Bu projede Llama 3.3 70B modeli tercih edildi. Google Translate gibi kural tabanlı bir çeviri yerine dil modeliyle yapılan çeviri sayesinde daha doğal ve bağlama uygun sonuçlar elde ediliyor.

---

## Groq API Key

Uygulamanın çalışabilmesi için bir Groq API anahtarına ihtiyaç var. [console.groq.com](https://console.groq.com) adresine girerek ücretsiz hesap açabilir ve API anahtarı oluşturabilirsin. Kredi kartı bilgisi istenmiyor. Ücretsiz katmanda dakikada 30 istek ve günde binlerce token hakkı tanınıyor, kişisel kullanım için fazlasıyla yeterli.

Anahtarı aldıktan sonra `backend` klasörü içine `.env` adında bir dosya oluşturup şu şekilde kaydetmen gerekiyor:

```
GROQ_API_KEY=buraya_kendi_anahtarını_yaz
```
---

## Kurulum

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Sunucu ayağa kalktıktan sonra tarayıcıda `http://localhost:8000` adresini açman yeterli. Chrome veya Edge kullanman öneriliyor, çünkü Web Speech API bu tarayıcılarda tam olarak destekleniyor.

---

## Lisans

MIT
