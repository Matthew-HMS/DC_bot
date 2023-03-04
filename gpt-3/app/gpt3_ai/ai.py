from dotenv import load_dotenv
import openai
import os
import json

load_dotenv()

openai.api_key = os.getenv("CHATGPT_API_KEY")

file = open("history.txt", "r")
contents = file.read()
lines = []
lines = contents.split("\n")
#history = [{"role": "system", "content": "You are a cat model, will add 'peko' at the end of every sentence"}]
history = []

for line in lines:
    mes = json.loads(line)
    history.append(mes)

def chatgpt_response(prompt):
    if prompt:

        history.append({"role": "user", "content": prompt})
        file = open("history.txt", "a")
        file.write('\n{"role": "user", "content": "' + prompt + '"}')
        
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages = history,
            max_tokens = 1000, temperature = 1.2
        )
    reply = chat_completion.choices[0].message.content

    history.append({"role": "assistant", "content": reply})
    file = open("history.txt", "a")
    file.write('\n{"role": "assistant", "content": "' + reply + '"}')
    return reply

