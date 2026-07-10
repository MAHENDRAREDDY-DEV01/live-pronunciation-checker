🎙️ AI Pronunciation Scoring Web App

An AI-powered web application that analyzes English speech pronunciation. Users can upload an English audio recording (30–45 seconds), receive an overall pronunciation score, and view highlighted pronunciation mistakes with suggestions for improvement.

🚀 Live Demo

- Frontend: [https://live-pronunciation-checker.vercel.app/]
- Backend: [https://live-pronunciation-checker-production.up.railway.app/docs] -It is used to upload the audio file and you can see working in backend
- [or Use this]
- [https://live-pronunciation-checker-production.up.railway.app/]

---

✨ Features

- Upload English audio files (30–45 seconds)
- Automatic speech-to-text transcription using OpenAI Whisper
- AI-powered pronunciation evaluation using the Groq API
- Overall pronunciation score
- Highlights pronunciation mistakes with explanations
- Provides suggestions for improving pronunciation
- Responsive and user-friendly interface
- Validates audio duration before processing

---

🛠️ Tech Stack

Frontend

- React.js
- HTML5
- CSS3
- JavaScript
- Axios

Backend

- FastAPI
- Python
- OpenAI Whisper
- Groq API
- FFmpeg / FFprobe

Deployment

- Frontend: Vercel
- Backend: Railway

---

⚙️ How It Works

1. The user uploads an English audio file (30–45 seconds).
2. The backend validates the audio duration.
3. OpenAI Whisper converts the speech into text.
4. The transcript is sent to the Groq API for pronunciation analysis.
5. The AI generates:
   - An overall pronunciation score
   - Mispronounced or unclear words
   - Explanations of pronunciation issues
   - Suggestions for improvement
6. The results are displayed on the web application.

---

🤖 AI Models Used

- OpenAI Whisper – Converts speech into text.
- Groq API – Evaluates the transcript, generates a pronunciation score, identifies pronunciation mistakes, and provides improvement suggestions.

---

📂 Project Structure

project/

├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json

├── backend/
│   ├── app.py
│   ├── pronunciation.py
│   ├── requirements.txt
│   ├── uploads/
│   └── .env

└── README.md

---

🔧 Installation

Backend

cd backend
pip install -r requirements.txt
uvicorn app:app --reload

[OR USE if you clone this github in local machine then use this for Run the Backend part]
cd backend
venv\Scripts\activate
uvicorn app:app --reload

Frontend

cd frontend
npm install
npm run dev

---

🔐 Environment Variables



GROQ_API_KEY="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"

---

📄 License

This project was developed as part of the Livo AI Software Engineer Assessment.
