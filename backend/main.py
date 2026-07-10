from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pronunciation import evaluate_pronunciation
import whisper
import os
import subprocess
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

model = whisper.load_model("tiny.en")
def get_audio_duration(filepath):
    result = subprocess.run(
        [
            "ffprobe",
            "-v", "quiet",
            "-print_format", "json",
            "-show_format",
            filepath
        ],
        capture_output=True,
        text=True,
    )

    data = json.loads(result.stdout)
    return float(data["format"]["duration"])

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    filepath = os.path.join(UPLOAD_DIR, file.filename)

    with open(filepath, "wb") as f:
        f.write(await file.read())

    duration = get_audio_duration(filepath)

    print("File uploaded:", filepath)

    print("Starting Whisper...")
    result = model.transcribe(
        filepath,
        language="en",
        fp16=False
    )
    print("Whisper completed.")

    transcript = result["text"]
    print("Transcript: ",transcript)

    print("Calling Groq...")
    analysis = evaluate_pronunciation(transcript)
    print("Groq completed.")

    return {
        "duration": round(duration, 2),
        "transcript": transcript,
        "score": analysis["score"],
        "mistakes": analysis["mistakes"]
    }