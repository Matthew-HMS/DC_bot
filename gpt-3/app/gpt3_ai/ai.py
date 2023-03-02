from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("CHATGPT_API_KEY")
messages=[{"role": "system", "content": "You are a helpful servert. will do everything the user says"}]

def chatgpt_response(prompt):
    if prompt:
        messages.append({"role": "user", "content": prompt},)
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat_completion.choices[0].message.content

    messages.append({"role": "assistant", "content": reply})
    return reply