from collections import Counter
import datetime
import random


class Formation:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def __repr__(self):
    return f'<{self.name} formation>'


infantry = Formation('Infantry', 100)
transport = Formation('Transport', 50)
supply = Formation('Supply', 50)

# when soldiers in combat units leave the army, they're added to the reservists
# reservists leave at the end of the year
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

    # how many new people were enlisted and de-enlisted this year
    # this is stored in the table of militry stats
    self.joined_this_year = 0
    self.left_this_year = 0

    # how much money the army has, used to pay salary
    self.budget = 75000
    self.govt_support_amount = 5000

  def total_count(self):
    return sum(self.formations.values())

  def yearly_enlistment(self):
    ''' 
    - Called at the end of the game loop
    - enlists a random number of soldiers in each formation
    - a random number of soldiers de-enlist from the army
    '''

    for each_formation in self.formations:
      if each_formation != reservists:
        # only non-reservists will be added to the army
        previous_pop = self.formations[each_formation]
        newly_enlisted = random.randint(0, int(previous_pop/3))
        de_enlisted = random.randint(0, int(previous_pop/10))

        print(each_formation.name, newly_enlisted, de_enlisted)
        

        self.formations[each_formation] += newly_enlisted - de_enlisted

        if each_formation == infantry:
          # those who leave the infantry (or any other combat unit) join the reservists
          self.formations[reservists] += de_enlisted
        else:
          self.left_this_year += de_enlisted
        self.joined_this_year += newly_enlisted
    
      

  def yearly_pay_salary(self):
    '''
    - Called at the end of the game loop
    - pays the salary for each formation soldier (money taken from budget)
    '''

    for each_formation in self.formations:
      no_soldiers = self.formations[each_formation]
      pay = each_formation.salary

      self.budget -= pay * no_soldiers
  
  def year_end(self):
    self.yearly_pay_salary()
    self.yearly_enlistment()

    # get money if military has government support
    self.budget += self.govt_support_amount
    
  def clear_reservists(self):
    no_reservists = self.formations[reservists]
    self.formations[reservists] = 0
    return no_reservists



class State:
  def __init__(self):
    self.rounds_complete = 0
    self.time_started = datetime.datetime.now()

  def round(self):
    self.rounds_complete += 1

  def get_time_played(self):
    ''' return amount of time played '''
    now = datetime.datetime.now()
    difference = now - self.time_started

    return int(difference.seconds / 60)
