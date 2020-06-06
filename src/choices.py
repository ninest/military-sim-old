from utils.prompts import mc_prompt


def change_enlistment_scheme():
  choice = mc_prompt('What would your like to do?', choices=['Enlist more soldiers', 'Fire soldiers'])
