from models import Military, Formation
from displays import clear_screen, display_stats
from prompts import mc_prompt

# instantiate the military!
military = Military()

def start():
  clear_screen()

  while True:
    gameloop()


def gameloop():
  clear_screen()

  # display stats of military
  display_stats(military)

  # add some spacing
  print('\n\n')

  choice = mc_prompt('What would you like to do now?', ['nothing'])

  military.formations[Formation.Infantry] += 10
  military.formations[Formation.Transport] += 2
  military.formations[Formation.Supply] += 2

  military.budget += 137
