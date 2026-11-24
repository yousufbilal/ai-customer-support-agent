from ollama import ChatResponse, chat

def add_two_numbers(a: int, b: int) -> int:
  """
  Add two numbers

  Args:
    a (int): The first number
    b (int): The second number

  Returns:
    int: The sum of the two numbers
  """
  return int(a) + int(b)


def subtract_two_numbers(a: int, b: int) -> int:
  """
  Subtract two numbers
  """
  # The cast is necessary as returned tool call arguments don't always conform exactly to schema
  return int(a) - int(b)

# messages = [{'role': 'user', 'content': 'What is three minus one?'}]
messages = [{'role': 'user', 'content': 'what’s 3 minus 1?'}]


print('Prompt:', messages[0]['content'])

available_functions = {
  'add_two_numbers': add_two_numbers,
  'subtract_two_numbers': subtract_two_numbers,
}

response: ChatResponse = chat(
  'qwen2.5:3b',
  messages=messages,
  tools=[add_two_numbers, subtract_two_numbers],
)

print()
print("Response",response)
print()
print("Messages",response.message)
print()
print("Tool Calls",response.message.tool_calls)
print()
print("Tool Name",response.message.tool_name)


if response.message.tool_calls:
  # There may be multiple tool calls in the response
  # Add the assistant message with tool calls to the conversation
  messages.append(response.message)
  print("appended messages",messages)


#   for tool in response.message.tool_calls:
#     # Ensure the function is available, and then call it
#     # print("tool: ",tool)
#     # print("tool.function.name: ",tool.function.name)
#     function_to_call = available_functions.get(tool.function.name)
#     # print("FUNCTION TO CALL",function_to_call)

#     if function_to_call:
#       print('Calling function:', tool.function.name)
#       print('Arguments:', tool.function.arguments)
#       output = function_to_call(**tool.function.arguments)
#       print('Function output:', output)
#     else:
#       print('Function', tool.function.name, 'not found')
#       output = 'Function not found'

# #     # Add each tool result as a separate message
#     messages.append({'role': 'tool', 'content': str(output), 'tool_name': tool.function.name})

# #   # Get final response from model with all tool call results
#   final_response = chat('qwen2.5:3b', messages=messages)
#   print('Final response:', final_response.message.content)

#   print("MESSAGES: ",messages)

# else:
#   print('No tool calls returned from model')