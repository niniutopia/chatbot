from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(override=True)

OPENAI_API_KEY_OP = os.getenv('OPENAI_API_KEY_OP')
BASE_URL = "https://openrouter.ai/api/v1"

# MODEL = "moonshotai/kimi-k2"
MODEL = "nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free"

richiesta = input('inserisci domanda: ')

client = OpenAI(
                base_url=BASE_URL,
                api_key=OPENAI_API_KEY_OP,
                )

completion = client.chat.completions.create(
                                            extra_body={},
                                            model=MODEL,
                                            messages=[
                                                {
                                                "role": "user",
                                                "content": richiesta
                                                }
                                            ]
                                            )
print(completion.choices[0].message.content)
