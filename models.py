from collections import Counter
import random
import enum


class Formation:
  def __init__(self, name, pay):
    self.name = name
    self.pay = pay

  def __repr__(self):
    return f'<{self.name} formation>'


infantry = Formation('Infantry', 1000)
transport = Formation('Transport', 700)
supply = Formation('Supply', 700)


class Military:
  def __init__(self):
    # default count in each military position
    self.formations = Counter({
        infantry: 50,
        transport: 10,
        supply: 10,
    })

    # how much money the army has, used to pay salary
    self.budget = 10000

  def yearly_enlistment(self):
    ''' 
    - Called at the end of the game loop
    - enlists a random number of soldiers in each formation
    - a random number of soldiers de-enlist from the army
    '''

    for each_formation in self.formations:
      # choose a random multiplier value for 10% of the formation population
      previous_pop = self.formations[each_formation]
      new_pop = int(previous_pop + (previous_pop/10 * random.random()))

      self.formations[each_formation] = new_pop
