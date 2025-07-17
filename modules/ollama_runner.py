# modules/ollama_runner.py

import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi"

def query_ollama(prompt):
    try:
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(OLLAMA_URL, json=payload)

        if response.status_code == 200:
            data = response.json()
            return data.get("response", "").strip()
        else:
            return f"❌ Ollama Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"❌ Exception while querying Ollama: {e}"
