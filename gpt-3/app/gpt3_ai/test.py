from dotenv import load_dotenv
import openai
import os

load_dotenv()

openai.api_key = os.getenv("CHATGPT_API_KEY")
def talk_with(persona, tell_user, ask_user):

    file = open("test.txt", "r")
    contents = file.read()
    lines = contents.split("\n")

    message_history = []
    print(message_history)
    while True:
        user_input = ask_user()
        if user_input == "":
            return message_history

        message_history.append({"role": "user", "content": user_input})
        query = [{"role": "system", "content": persona}]
        query.extend(message_history)
        result = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages=query
        )
        gpt_message = result["choices"][0]["message"]
        message_history.append({"role": gpt_message["role"], "content": gpt_message["content"]})

        tell_user("GPT: " + gpt_message["content"])

talk_with(
    persona="""You are a helpful cooking expert. You answer question by providing a short explanation and a list of easy to follow steps. You list ingredients, tools, and instructions.""",
    tell_user=print,
    ask_user=input
)