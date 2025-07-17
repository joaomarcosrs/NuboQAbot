import requests
from decouple import config


MODEL = config('MODEL', cast=str)

def call_llm(prompt: str, model: str = MODEL) -> str:
    response = requests.post(
        f'{config('OLLAMA_SERVER', cast=str)}/api/generate',
        json={
            'model': model,
            'prompt': prompt,
            'stream': False
        }
    )

    return response.json()['response']
