from collections import Counter
import datetime
import random

from models.formation import Formation


infantry = Formation('Infantry', 100)  # starting salary of $100
transport = Formation('Transport', 50)  # starting salary of $50
supply = Formation('Supply', 50)

# when soldiers in combat units leave the army, they're added to the reservists
# reservists leave at the end of the month
reservists = Formation('Reservists', 50)


class Military:
  def __init__(self):
    # default count in each military position
    self.formations = Counter({
        infantry: 50,
        transport: 10,
        supply: 10,
        reservists: 0
    })

    # how many new people were enlisted and de-enlisted this month
    # this is stored in the table of militry stats
    self.joined_this_month = 0
    self.left_this_month = 0

    # mulitplier for how many people will join/leave the army
    self.join_rate = 1
    self.leave_rate = 1

    # how much money the army has, used to pay salary
    self.budget = 75000
    self.govt_support_amount = 5000

  def total_count(self):
    return sum(self.formations.values())

  def monthly_enlistment(self):
    ''' 
    - Called at the end of the game loop
    - enlists a random number of soldiers in each formation
    - a random number of soldiers de-enlist from the army
    '''

    for each_formation in self.formations:
      if each_formation != reservists:
        # only non-reservists will be added to the army
        previous_pop = self.formations[each_formation]
        newly_enlisted = random.randint(0, int(previous_pop/3 * self.join_rate))
        de_enlisted = random.randint(0, int(previous_pop/3 * self.leave_rate))

        # print(each_formation.name, newly_enlisted, de_enlisted)

        self.formations[each_formation] += newly_enlisted - de_enlisted

        if each_formation == infantry:
          # those who leave the infantry (or any other combat unit) join the reservists
          self.formations[reservists] += de_enlisted
        else:
          self.left_this_month += de_enlisted
        self.joined_this_month += newly_enlisted

  def monthly_pay_salary(self):
    '''
    - Called at the end of the game loop
    - pays the salary for each formation soldier (money taken from budget)
    '''

    for each_formation in self.formations:
      no_soldiers = self.formations[each_formation]
      pay = each_formation.salary

      self.budget -= pay * no_soldiers

  def month_end(self, state):
    '''
    - pay the soldiers
    - get paid by gahmen
    '''

    self.monthly_pay_salary()
    self.monthly_enlistment()

    # get money if military has government support
    self.budget += self.govt_support_amount

    # clear the number of reservists every 10 months
    if (state.rounds_complete % 10 == 0) and (state.rounds_complete != 0):
      # (although they are cleared right now, the number is only updated in the teble the next month)
      self.left_this_month += self.clear_reservists()

  def clear_reservists(self):
    no_reservists = self.formations[reservists]
    self.formations[reservists] = 0
    return no_reservists
