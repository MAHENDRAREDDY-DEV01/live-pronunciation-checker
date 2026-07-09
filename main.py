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

model = whisper.load_model("tiny")
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

    try:
        duration = get_audio_duration(filepath)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    if duration < 30 or duration > 45:
        os.remove(filepath)
        raise HTTPException(
            status_code=400,
            detail="Audio must be between 30 and 45 seconds."
        )
    # duration = 30

    result = model.transcribe(filepath, language="en")
    transcript = result["text"]
    analysis = evaluate_pronunciation(transcript)

    return {
        "duration": round(duration, 2),
        "transcript": transcript,
        "score": analysis["score"],
        "mistakes": analysis["mistakes"]
    }