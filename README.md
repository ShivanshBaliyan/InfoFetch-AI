# 🏏 InfoFetch AI - Cricket Assistant

A cricket chatbot built with **FastAPI** and **Streamlit** that provides live cricket information using the CricketData API.

## 🌐 Live Demo

- **Application:** https://infofetch-ai-3rcr9zbkzfbwzkqlqrcxox.streamlit.app/
- **Backend:** https://infofetch-ai.onrender.com

## ✨ Features

- Live matches
- Upcoming matches
- Player information
- Match information
- Series search
- Series details

## 🛠 Tech Stack

- FastAPI
- Streamlit
- httpx
- Pydantic
- CricketData API

## 📁 Project Structure

```text
InfoFetch-AI/
│
├── backend/
│   ├── main.py
│   ├── routes.py
│   ├── services.py
│   ├── clients.py
│   ├── schemas.py
│   ├── intents.py
│   ├── utils.py
│   ├── formatters.py
│   └── config.py
│
├── frontend/
│   ├── app.py
│   └── api.py
│
└── README.md
```

## 🚀 Run Locally

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## 💬 Example Queries

- Live matches
- Upcoming matches
- Who is Virat Kohli?
- Information about Rohit Sharma
- IPL
- Asia Cup
- India vs Australia

## 📌 Deployment

- **Backend:** Render
- **Frontend:** Streamlit Community Cloud