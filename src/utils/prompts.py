from rich.console import Console

try:
  from utils.displays import typewrtier_print
except:
  from displays import typewrtier_print


console = Console()


def prompt(prompt_message=None):
  ''' A customized prompt to be used instead of input (doesn't require a prompt_message) '''

  # if no prompt_message, only ask for the prompt
  if prompt_message is not None:
    # console.print(prompt_message, style='bold')
    typewrtier_print(prompt_message, style='bold')

  console.print('> ', end='', style='bold')
  answer = input()
  return answer


def mc_prompt(prompt_message, choices):
  ''' Multiple choice prompt that returns an element from the choices list '''

  # console.print(prompt_message, style='bold')
  typewrtier_print(prompt_message, style='bold')

  for each_choice in enumerate(choices):
    option_no, option_text = each_choice

    console.print(f'{option_no}. {option_text}', style='white')

  answer_prompt = prompt().lower().strip()

  # check if the answer was a number, and return the choice accordinly
  try:
    answer = int(answer_prompt)
  except:
    answer = choices.index(answer_prompt)

  return answer
