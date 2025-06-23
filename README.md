# AI Knowledge Assistant using LLMs

## 🚀 Overview
An AI-powered knowledge assistant that uses a fine-tuned Large Language Model (LLM) to provide context-aware answers and summaries through a React + Flask web app.

## ✨ Features
- Fine-tuned GPT-J or LLaMA for niche domain Q&A
- React frontend with chat-like UI
- Flask backend serving the model
- Prompt engineering & ranking
- Caching for speed

## 📂 Structure
- `/frontend` — React app
- `/backend` — Flask API, model scripts
- `/model` — Fine-tuning & prompt files
- `/data` — Example training data

## 🧰 Tech Stack
- LLM: GPT-J, LLaMA (via Hugging Face)
- Frontend: React, Axios
- Backend: Flask, Transformers, Torch

## ⚡️ Run Locally
```bash
git clone https://github.com/YOUR_USERNAME/ai-knowledge-assistant-llm.git
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

# In another terminal
cd ../frontend
npm install
npm start
```
Open [http://localhost:3000](http://localhost:3000)

## 🤖 Demo
Add screenshots or a demo GIF here.

## 📚 Learnings
- Fine-tuning LLMs
- Prompt design
- Caching & latency trade-offs
- End-to-end deployment

## 📜 License
MIT License.
