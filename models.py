from collections import Counter
import random
import enum


class Formation:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def __repr__(self):
    return f'<{self.name} formation>'


infantry = Formation('Infantry', 100)
transport = Formation('Transport', 50)
supply = Formation('Supply', 50)


class Military:
  def __init__(self):
    # default count in each military position
    self.formations = Counter({
        infantry: 50,
        transport: 10,
        supply: 10,
    })

    # how much money the army has, used to pay salary
    self.budget = 25000

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

  def yearly_pay_salary(self):
    '''
    - Called at the end of the game loop
    - pays the salary for each formation soldier (money taken from budget)
    '''

    for each_formation in self.formations:
      no_soldiers = self.formations[each_formation]
      pay = each_formation.salary

      self.budget -= pay * no_soldiers
