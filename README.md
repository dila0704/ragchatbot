# 🤖 Local RAG AI Chatbot

LangChain, Ollama, Llama 3, ChromaDB ve Streamlit kullanılarak geliştirilmiş tamamen local çalışan bir RAG (Retrieval-Augmented Generation) chatbot uygulaması.

Bu proje sayesinde kullanıcılar PDF dosyalarını yükleyip belgeyle doğal dil üzerinden sohbet edebilir. Sistem tamamen local çalışır ve herhangi bir OpenAI API gerektirmez.

---

# ✨ Özellikler

- 📄 PDF ile sohbet etme
- 🧠 Tamamen local çalışan Llama 3 modeli
- 🔍 Semantic search desteği
- 💻 Offline AI sistemi
- ⚡ ChromaDB ile hızlı retrieval
- 🎨 Modern Streamlit arayüzü

---

# 🏗️ Sistem Mimarisi

```text
PDF
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Database
 ↓
Similarity Search
 ↓
Llama 3
 ↓
AI Response
```

---

# 🛠️ Kullanılan Teknolojiler

| Teknoloji | Amaç |
|---|---|
| Python | Backend |
| Streamlit | Arayüz |
| LangChain | RAG Pipeline |
| Ollama | Local LLM Runtime |
| Llama 3 | Dil modeli |
| ChromaDB | Vector Database |
| nomic-embed-text | Embedding modeli |

---

# 📸 Ekran Görüntüleri

## Ana Arayüz
<img width="1453" height="789" alt="Ekran Resmi 2026-05-20 14 37 08" src="https://github.com/user-attachments/assets/6b01c796-6569-4f53-8fda-55f991fd5687" />




<img width="1464" height="800" alt="Ekran Resmi 2026-05-20 14 35 40" src="https://github.com/user-attachments/assets/8fe65c35-cbf3-467b-9220-62aea9e9f535" />


---

# 🚀 Kurulum

## 1. Repoyu klonla

```bash
git clone https://github.com/kullaniciadi/local-rag-chatbot.git
cd local-rag-chatbot
```

---

## 2. Conda environment oluştur

```bash
conda create -n ragbot python=3.11
conda activate ragbot
```

---

## 3. Gerekli paketleri yükle

```bash
pip install -r requirements.txt
```

---

## 4. Ollama kur

Ollama'yı indir:

https://ollama.com/

---

## 5. Modelleri indir

```bash
ollama pull llama3
ollama pull nomic-embed-text
```

---

## 6. Ollama servis başlat

```bash
ollama serve
```

---

## 7. Uygulamayı çalıştır

```bash
streamlit run app.py
```

---

# 🧠 RAG Sistemi Nasıl Çalışıyor?

Bu projede Retrieval-Augmented Generation (RAG) mimarisi kullanılmaktadır.

Sistem şu şekilde çalışır:

1. Kullanıcının yüklediği PDF okunur
2. Metin küçük chunk’lara bölünür
3. Her chunk embedding vektörüne dönüştürülür
4. Veriler ChromaDB içinde saklanır
5. Kullanıcının sorusuna en yakın chunk’lar bulunur
6. Llama 3 modeli bu context ile cevap üretir

---

# ⚠️ Geliştirme Sürecinde Karşılaşılan Problemler

Proje geliştirilirken şu problemlerle karşılaşıldı:

- LangChain import değişiklikleri
- Paket bağımlılığı sorunları
- Local embedding performansı
- Chunk size optimizasyonu
- Local inference kurulumu

---

# 🔮 Gelecekte Eklenebilecek Özellikler

- Çoklu PDF desteği
- Conversation memory
- Source citation sistemi
- Hybrid search
- Daha gelişmiş UI/UX
- Docker desteği



---

# 👨‍💻 Geliştirici

Dila Alpay
