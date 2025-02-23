# 📝 FastAPI Summarizer Model

🚀 A lightweight **news summarization API** built using **FastAPI**. This service processes **text, images, and videos** to generate **concise and meaningful summaries**.  


## 🌟 Features
✅ **Text Summarization** - Extracts key points from long articles.  
✅ **Image-Based News Extraction** - Uses OCR to extract and summarize text from images.  
✅ **Video News Summarization** - Converts speech to text and generates a concise summary.  
✅ **FastAPI Framework** - High-speed, async processing with minimal overhead.  
✅ **Docker Support** - Easily deploy the model anywhere.  

---

## 🏗 Project Structure  
📂 **processed/** - Stores processed news summaries.  
📂 **uploads/** - Stores uploaded files (text, images, videos).  
📄 **main.py** - FastAPI backend with endpoints for summarization.  
📄 **requirements.txt** - Lists necessary dependencies.  
📄 **dockerfile** - Configuration for Docker deployment.  
📄 **startup.sh** - Shell script to initialize the service.  
📄 **vercel.json** - Configuration for Vercel deployment.  

---

## ⚙️ Installation & Setup  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/Priyank911/FNA_Summarizer.git
cd FNA_Summarizer
```
### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the FastAPI Server  
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
### 4️⃣ Access the API  
- Open **http://localhost:8000/docs** to explore the API using Swagger UI.  

---

## 🔗 API Endpoints  
| **Method** | **Endpoint** | **Description** |
|------------|-------------|-----------------|
| `POST` | `/summarize/text` | Summarizes given text. |
| `POST` | `/summarize/image` | Extracts and summarizes text from an image. |
| `POST` | `/summarize/video` | Converts speech to text and summarizes the content. |
| `GET` | `/health` | Checks if the API is running. |

---

## 📦 Deployment  
### 🚀 Deploy with Docker  
```bash
docker build -t fastapi-summarizer .
docker run -p 8000:8000 fastapi-summarizer
```
### ☁️ Deploy on Vercel  
```bash
vercel --prod
```

---

## 🚀 Future Enhancements  
🔹 Improved NLP models for better accuracy.  
🔹 Support for multi-language summarization.  
🔹 Integration with IPFS for decentralized storage.  

---

## 🤝 Contributions  
Feel free to contribute! Open a PR or raise an issue.  

---

## 📜 License  
Licensed under **MIT License**.  

---

**🔗 Stay Connected:** [GitHub Repository](https://github.com/Priyank911/FNA_Summarizer)  

💡 *"Turning long news into short, factual insights!"* 🚀  
