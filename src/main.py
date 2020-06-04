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

  # DEBUG mode: automatially start the game
  start()


  # fullscreen_message('Welcome to Military Simulator', color='green')
  # time.sleep(2)

  # show_options()


def show_options():
  clear_screen()
  option = mc_prompt(
      'What would you like to do?',
      choices=['play', 'github', 'quit']
  )

  # start game
  if option == 'play':
    start()

  # open github repo
  elif option == 'github':
    webbrowser.open('https://github.com/ninest')

  # quit program completely
  elif option == 'quit':
    clear_screen()
    sys.exit()


if __name__ == '__main__':
  main()
