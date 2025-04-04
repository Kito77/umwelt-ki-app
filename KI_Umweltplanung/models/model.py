 # Definition des Hauptmodells

import requests

class OllamaAssistant:
    def __init__(self, model_name='mistral', host='http://localhost:11434'):
        self.model_name = model_name
        self.api_url = f"{host}/api/generate"

    def frage_stellen(self, prompt):
        response = requests.post(
            self.api_url,
            json={
                'model': self.model_name,
                'prompt': prompt,
                'stream': False
            }
        )
        if response.status_code == 200:
            return response.json()['response']
        else: 
            return f"Fehler bei der Anfrage: {response.status_code}"