import requests
import json
from datetime import datetime

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:4b"
LOGFILE = "ollama_log.json"


def query_ollama(prompt):
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    r = requests.post(OLLAMA_URL, json=payload)
    r.raise_for_status()
    return r.json()["response"]


def log_interaction(prompt, response):
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "model": MODEL,
        "prompt": prompt,
        "response": response
    }

    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    while True:
        prompt = input(">>> ")
        if prompt.lower() in {"exit", "quit"}:
            break

        response = query_ollama(prompt)
        print(response)
        log_interaction(prompt, response)
