import requests

prompt = "Welche Auswirkungen hat ein Bauvorhaben in einem FFH-Gebiet?"

response = requests.post(
    'http://localhost:11434/api/generate',
    json={
        'model': 'mistral',
        'prompt': prompt,
        'stream': False
    }
)

antwort = response.json()['response']
print("Antwort von Mistral:", antwort)
