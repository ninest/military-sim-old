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
  while True:  
    # only break when a choice has been made successfully
    # when a choice has been made, the current "round loop" ends, and the next round starts
    clear_screen()

    # display stats of military in a tabular form
    display_stats(military, state)

    # show any messages eg. Reservists leaving the army, wars starting soon
    show_alerts(military, state)

    # add some spacing
    print('\n\n')

    # actual game logic
    choice = mc_prompt('What would you like to do now?', ['change enlistment scheme', 'change salary', 'nothing'])

    # add some spacing
    print()
    # choice logic
    if choice == 0:
      result = change_enlistment_scheme(military)
      if result:
        break

    elif choice == 1:
      # TODO: implement change salary
      pass

    elif choice == 2:
      # nothing choice has been made
      # this means that for the round (1 month), the army does nothing
      break

  # reset the number of peole joined and left this month
  military.joined_this_month = military.left_this_month = 0

  # functions called at the end of the month (pay salary, enlist soldiers, )
  military.month_end(state)

  # change game state: add 1 to the number of rounds completed
  state.round()
