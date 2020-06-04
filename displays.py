import os
import time
from textwrap import TextWrapper
from rich.console import Console
from rich.table import Column, Table

console = Console()


def display_stats(military):
  ''' Prints a table of the army stats '''

  table = Table(show_header=True, header_style='bold white')

  # columns: breakup of how many people in each formation and total budget
  table.add_column('Breakup')
  table.add_column('Budget ($)')

  breakup = ''
  for each_formation in military.formations:
    breakup += f'[bold]{each_formation.name}[/bold]: [gray]{military.formations[each_formation]} soldiers[/gray]\n'

  table.add_row(
      breakup,
      f'{military.budget}'
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
