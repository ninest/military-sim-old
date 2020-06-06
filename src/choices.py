import time

from utils.prompts import mc_prompt


def change_enlistment_scheme(military):
  choice = mc_prompt('What would your like to do?', choices=['Enlist more soldiers', 'Fire soldiers'])

  # leave a line
  print()

  if choice == 0:
    print('enlisting more ...')
    military.join_rate += 0.2
    time.sleep(2)
    return True
  else:
    print('firing soldiers!')
    military.leave_rate += 0.2
    time.sleep(2)
    return True
  
  return False
