from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def evaluate_pronunciation(transcript):

    prompt = f"""
You are an expert English pronunciation evaluator.

Analyze the transcript and estimate the speaker's pronunciation quality.

Rules:
-responsce only in english.
- Score must be between 60 and 100.
-find a atleast 5 pronuncation mistake if possible.
- If pronunciation is generally good, give 80-95.
- Only report words that are likely mispronounced.
- Give a short issue and a useful suggestion.
- Return ONLY valid JSON.

Format:
{{
  "score": 85,
  "mistakes": [
    {{
      "word": "",
      "issue": "",
      "suggestion": ""
    }}
  ]
}}

Transcript:
{transcript}
"""
    print("Transcript genrate sucessfull")
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )
    print("Groq response recieved")

    text = response.choices[0].message.content.strip()

    # Remove markdown if model returns it
    text = text.replace("```json", "").replace("```", "").strip()

    print("Groq Response:")
    print(text)

    try:
        return json.loads(text)

    except Exception as e:
        print("JSON Error:", e)

        return {
            "score": 75,
            "mistakes": [
                {
                    "word": "Unknown",
                    "issue": "Could not parse model response.",
                    "suggestion": "Try again."
                }
            ]
        }