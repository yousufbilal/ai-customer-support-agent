from ollama import chat
from ollama import ChatResponse

def chatbot_fun():

  while True:
    print("enter your message:")
    user_input = input()

    response: ChatResponse = chat(
      model='qwen2.5:3b',
      messages=[
        {
          'role': 'user',
          'content': user_input,
        },
      ],
    )

    print(response['message']['content'])

    if user_input == "quit":
      break

chatbot_fun()