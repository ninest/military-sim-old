from models import Military, Formation, State
from displays import clear_screen, display_stats
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
  # clear_screen()

  # display stats of military
  display_stats(military)

  # add some spacing
  print('\n\n')

  choice = mc_prompt('What would you like to do now?', ['nothing'])

  military.yearly_pay_salary()
  military.yearly_enlistment()

  # get money if military has government support
  military.budget += military.govt_support_amount

  # game state
  state.round()
  print('time played: ', state.get_time_played())