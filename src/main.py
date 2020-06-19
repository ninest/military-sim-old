import os
import sys
import time
import webbrowser
from rich import print

from utils.displays import fullscreen_message, clear_screen
from utils.prompts import prompt, mc_prompt
from game import start


def main():
  # TODO: set the background color to a darker color

  # DEBUG mode: automatially start the game
  # start()


  fullscreen_message('Welcome to Military Simulator', color='green')
  time.sleep(2)

  show_options()


def show_options():
  while True:
    clear_screen()
    # mc_prompt = multichoice prompt
    option = mc_prompt(
        'What would you like to do?',
        choices=['play', 'github', 'quit']
    )

    # start game
    if option == 0:
      start()

    # open github repo
    elif option == 1:
      webbrowser.open('https://github.com/ninest/military-sim')

    # quit program completely
    elif option == 2:
      clear_screen()
      sys.exit()


if __name__ == '__main__':
  main()
