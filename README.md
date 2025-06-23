# 🧠 AI Knowledge Assistant using LLMs

## 🚀 Overview
This project is an AI-powered knowledge assistant built with a fine-tuned **Large Language Model (LLM)**. It provides context-aware answers and summaries for a niche community via a modern **React + Flask** full-stack web app.

---

## ✨ Features
- ✅ Fine-tuned GPT-J, LLaMA, or any text-generation LLM
- ✅ Custom prompt templates with system instructions
- ✅ Fast response times using caching
- ✅ Clean API design with input validation and error handling
- ✅ Modular frontend with React hooks, reusable components, and Axios integration
- ✅ Easy local `.env` configuration for quick environment setup

---

## 📂 Project Structure

### 📁 **Backend**
| File/Folder | Purpose |
| ----------- | ------- |
| `app.py` | Flask app factory — initializes server, loads configs, enables CORS, registers API blueprints |
| `config.py` | Central config for environment variables (model name, cache timeout) |
| `requirements.txt` | Python dependencies |
| `.env.example` | Example backend environment variables |
| `api/routes.py` | REST API endpoints (e.g., `/answer`); handles validation and error responses |
| `model/loader.py` | Loads the LLM pipeline (via Hugging Face) |
| `model/prompt_handler.py` | Builds custom prompt templates with instructions |
| `utils/cache.py` | Simple in-memory caching for repeated Q&A |
| `utils/logger.py` | Logging setup for request tracking |

### 📁 **Frontend**
| File/Folder | Purpose |
| ----------- | ------- |
| `package.json` | Frontend dependencies & npm scripts |
| `.env.example` | Example API URL variable |
| `src/App.js` | Main React entry — renders the base layout and routes |
| `src/api/assistantAPI.js` | Encapsulates Axios calls to the backend |
| `src/hooks/useAssistant.js` | Custom React hook for Q&A logic & loading state |
| `src/components/ChatBox.js` | Reusable component for question/context input |
| `src/components/AnswerCard.js` | Displays the returned answer nicely |
| `src/pages/HomePage.js` | Combines `ChatBox` and `AnswerCard` in a page |

---

## ⚡️ Quick Start

### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/ai-knowledge-assistant-llm.git
cd ai-knowledge-assistant-llm


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

## 📚 Learnings
- Fine-tuning LLMs
- Prompt design
- Caching & latency trade-offs
- End-to-end deployment

## 📜 License
MIT License.
