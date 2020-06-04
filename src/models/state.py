import datetime

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
