import time
from rich import print

from models.military import Military
from models.state import State

from utils.displays import display, clear_screen, display_stats, typewrtier_print
from utils.prompts import mc_prompt

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

  alerts = []
  # every 10 years, all reservists leave the army
  if (state.rounds_complete % 5 == 0) and (state.rounds_complete != 0):
    # clear the number of reservists, but only updated in table next year
    military.left_this_year += military.clear_reservists()
    alerts.append('Reservists are leaving soon')
  
  # print alerts if there are any
  if alerts:
    print('\n[bold]Alerts: [\bold]')
    for alert in alerts:
      print(f'- {alert}')


  # add some spacing
  print('\n\n')

  # actual game logix
  choice = mc_prompt('What would you like to do now?', ['nothing'])
  # choice logic
  # TODO:


  # functions called at the end of the year (pay salary, enlist soldiers, )
  military.year_end()

  # game state
  state.round()