import os
import time
from textwrap import TextWrapper
from rich.console import Console
from rich.table import Column, Table


console = Console()

# It's okay if you don't understand exactly what these functions are doing


def display(message, style=''):
  console.print(message, style=style)


def display_stats(military, state):
  ''' Prints a table of the army stats '''

  # Tables are made using the 'rich' module: https://github.com/willmcgugan/rich#tables

  table = Table(show_header=True, header_style='bold white')

  # columns: breakup of how many people in each formation and total budget
  table.add_column('Breakup')
  table.add_column('Budget ($)')
  table.add_column('Months passed')

  breakup = ''
  for each_formation in military.formations:
    breakup += f'[bold]{each_formation.name}[/bold]: [gray]{military.formations[each_formation]} soldiers[/gray]\n'

  breakup += f'[bold]Total: {military.total_count()}[/bold]\n'

  # show the change in number of people
  breakup += f'[red]-{military.left_this_month} ({military.leave_rate})[/red]   [green]+{military.joined_this_month} ({military.join_rate})[/green]'
  # NOTE: military.leave_rate and military.join_rate are not meant to be shown. They are being shown for debug purposes only

  table.add_row(
      breakup,
      f'{military.budget}',
      f'{state.rounds_complete}'
  )
  console.print(table)


def clear_screen():
  os.system('clear')


def typewrtier_print(message, style=''):
  ''' print a message being typed in a typewriter-like effect '''

  for char in message:
    console.print(char, end='', style=style)
    # time.sleep(0.055)
    time.sleep(0.005)

  # leave line at the end
  print()


def fullscreen_message(message, color=''):
  ''' Display message with a border '''
  os.system('clear')
  screen_height, screen_width = list(map(int, os.popen('stty size', 'r').read().split(" ")))

  text_offset_top = int(screen_height/2)

  wrap = TextWrapper(width=screen_width/2)
  wrap_list = wrap.wrap(text=message)

  # border for top (---)
  console.print('+' + '-' * (screen_width-2) + '+', style=f'bold {color}')

  # side borders (|) and text in center
  for row_index in range(screen_height-2 - len(wrap_list)):
    if row_index == text_offset_top - int(len(wrap_list) / 2):
      for line in wrap_list:
        string = line.center(screen_width-2, ' ')
        console.print(f'|{string}|', style=f'bold {color}')

    else:
      console.print('|' + ' '*(screen_width-2) + '|', style=f'bold {color}')

  # border for bottom (---)
  console.print('+' + '-' * (screen_width-2) + '+', style=f'bold {color}')
