import time
from rich import print

from models.military import Military
from models.state import State
from utils.displays import display, clear_screen, display_stats, typewrtier_print
from utils.prompts import mc_prompt

from functions import show_alerts


# instantiate the military!
military = Military()

# start game state (round counter, time played)
state = State()


def start():
  clear_screen()

  while True:
    gameloop()


def gameloop():
  clear_screen()

  # display stats of military
  display_stats(military)

  # reset the number of peole joined and left this year
  military.joined_this_year = military.left_this_year = 0

  show_alerts(state, military)
  # add some spacing
  print('\n\n')

  # actual game logix
  choice = mc_prompt('What would you like to do now?', ['change enlistment scheme', 'change salary', 'nothing'])
  # choice logic
  if choice == 0:
    pass
  elif choice == 2:
    pass

  # functions called at the end of the year (pay salary, enlist soldiers, )
  military.year_end()

  # game state
  state.round()
