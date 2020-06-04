class Formation:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  def __repr__(self):
    return f'<{self.name} formation>'