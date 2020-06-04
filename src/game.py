import time
from rich import print

from displays import typewrtier_print
from models import Military, Formation, State
from displays import display, clear_screen, display_stats
from prompts import mc_prompt

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

  military.joined_this_year = military.left_this_year = 0

  alerts = []
  # every 10 years, all reservists leave the army
  if (state.rounds_complete % 5 == 0) and (state.rounds_complete != 0):
    military.left_this_year += military.clear_reservists()
    alerts.append('Reservists to leave army next year')
  
  # print alerts if there are any
  if alerts:
    print('\n[bold]Alerts: [\bold]')
    for alert in alerts:
      print(f'- {alert}')


  # add some spacing
  print('\n\n')

  choice = mc_prompt('What would you like to do now?', ['nothing'])
  # choice logic
  # TODO:

  military.yearly_pay_salary()
  military.yearly_enlistment()

  # get money if military has government support
  military.budget += military.govt_support_amount

  # game state
  state.round()