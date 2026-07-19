import os
import urllib.request
import json

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise SystemExit("Set GROQ_API_KEY as an environment variable first.")

payload = json.dumps({
    "model": "llama-3.1-8b-instant",
    "messages": [{"role": "user", "content": "Say hello in one sentence."}],
    "max_tokens": 50
}).encode("utf-8")

req = urllib.request.Request(
    "https://api.groq.com/openai/v1/chat/completions",
    data=payload,
    headers={"Content-Type": "application/json", "Authorization": "Bearer " + GROQ_API_KEY},
    method="POST"
)

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode("utf-8"))
    print("SUCCESS!")
    print(data["choices"][0]["message"]["content"])