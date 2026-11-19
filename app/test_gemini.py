from pathlib import Path
from dotenv import load_dotenv
from google import genai
import os
import time

# Cargar .env desde la raíz del proyecto
load_dotenv(Path(__file__).parent.parent / ".env")

print("KEY FOUND:", bool(os.getenv("GEMINI_API_KEY")))

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# CAMBIA ESTE MODELO EN CADA PRUEBA
MODEL = "gemini-3.5-flash-lite"

print(f"\nTESTING: {MODEL}")

start = time.time()

try:
    response = client.models.generate_content(
        model=MODEL,
        contents="Respond only with OK"
    )

    print(f"SUCCESS ({time.time()-start:.1f}s)")
    print(response.text)

except Exception as e:
    print(f"FAILED ({time.time()-start:.1f}s)")
    print(type(e).__name__)
    print(e)