import os
import sys
import time
import webbrowser
from rich import print
from displays import fullscreen_message, clear_screen
from prompts import prompt, mc_prompt
from game import start


def main():
  # TODO: set the background color to a darker color

  fullscreen_message('Welcome to Military Sim', color='green')
  time.sleep(0.3)

  # start game
  # while True:
  clear_screen()
  option = mc_prompt(
      'What would you like to do?',
      choices=['play', 'github', 'quit']
  )

  if option == 'play':
    start()

  elif option == 'github':
    webbrowser.open('https://github.com/ninest')

  elif option == 'quit':
    clear_screen()
    sys.exit()


if __name__ == '__main__':
  main()
