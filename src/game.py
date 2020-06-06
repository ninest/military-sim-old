import time
from rich import print

from models.military import Military
from models.state import State
from utils.displays import display, clear_screen, display_stats, typewrtier_print
from utils.prompts import mc_prompt

from functions import show_alerts
from choices import change_enlistment_scheme


# instantiate the military!
military = Military()

# start game state (round counter, time played)
state = State()


def start():
  clear_screen()

  while True:
    gameloop()


def gameloop():
  while True:  # only break when a choice has been made successfully
    clear_screen()

    # display stats of military
    display_stats(military, state)

    show_alerts(military, state)
    # add some spacing
    print('\n\n')

    # actual game logic
    choice = mc_prompt('What would you like to do now?', ['change enlistment scheme', 'change salary', 'nothing'])

    print()
    # choice logic
    if choice == 0:
      result = change_enlistment_scheme(military)
      if result:
        break

    elif choice == 1:
      pass

    elif choice == 2:
      # nothing choice has been made
      break

  # reset the number of peole joined and left this year
  military.joined_this_year = military.left_this_year = 0

  # functions called at the end of the year (pay salary, enlist soldiers, )
  military.year_end(state)

  # game state
  state.round()
