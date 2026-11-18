from ollama import chat
from ollama import ChatResponse

def chatbot_fun():

  messages = []

  while True:
    print("enter your message:")
    user_input = input()

    messages.append({'role':'user','content': user_input})

    response: ChatResponse = chat(
      model='qwen2.5:3b',
      messages=messages
    )

    print(response['message']['content'])

    messages.append({'role':'assistant','content': response['message']['content']})

    if user_input == "quit":
      break

chatbot_fun()