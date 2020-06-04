from rich.console import Console

console = Console()


def prompt(prompt_message=None):
  # if no prompt_message, only ask for the prompt
  if prompt_message is not None:
    console.print(prompt_message, style='bold')

  console.print('> ', end='', style='bold')
  answer = input()
  return answer


def mc_prompt(prompt_message, choices):
  console.print(prompt_message, style='bold')

  for each_choice in enumerate(choices):
    option_no, option_text = each_choice

    console.print(f'{option_no}. {option_text}', style='white')
  
  answer_prompt = prompt().lower().strip()

  # check if the answer was a number, and return the choice accordinly
  try:
    answer_int = int(answer_prompt)
    answer = choices[answer_int]
  except:
    answer = answer_prompt
  
  return answer

# print(
#   mc_prompt('What would you like to do?', ['eat', 'sleep', 'go'])
# )
