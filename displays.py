import os
from textwrap import TextWrapper
from rich.console import Console

console = Console()


def clear_screen():
  os.system('clear')


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
