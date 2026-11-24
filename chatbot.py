from ollama import ChatResponse, chat
from sqlite_db import get_bouquets_for_occasion


while True:
  print("enter: What occassion is the flowers needed for \nenter quit to end chat")
  user_input = input()

  if user_input == "quit":
    break

  messages = [{'role': 'user', 'content': user_input}]
  print('Prompt:', messages[0]['content'])

  available_functions = {'get_bouquets_for_occasion': get_bouquets_for_occasion}

  response: ChatResponse = chat(
    'llama3.2:latest',
    messages=messages,
    tools=[get_bouquets_for_occasion])

  if response.message.tool_calls:
    messages.append(response.message)

    for tool in response.message.tool_calls:
      function_to_call = available_functions.get(tool.function.name)

      if function_to_call:
        print('Calling function:', tool.function.name)
        print('Arguments:', tool.function.arguments)
        output = function_to_call(**tool.function.arguments)
      else:
        print('Function', tool.function.name, 'not found')
        output = 'Function not found'
        
      messages.append({'role': 'tool', 'content': str(output), 'tool_name': tool.function.name})

      final_response = chat('qwen2.5:3b', messages=messages)
      print('Final response:', final_response.message.content)

  else:
    print('No tool calls returned from model')
    break



  