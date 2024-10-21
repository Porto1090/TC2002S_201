from openai import OpenAI
from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()
secret_key = os.getenv('PROFESOR_KEY')

# Crear una instancia de OpenAI
client= OpenAI(
    api_key=secret_key,
)

prompt = "What is the capital of Spain?"

completition = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
    ],
    max_tokens=100,
    temperature=1
)

print(completition.choices[0].message.content)