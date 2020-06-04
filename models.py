from collections import Counter
import enum


class Formation(enum.Enum):
  Infantry = 'infantry'
  Transport = 'transport'
  Supply = 'supply'


class Military:
  def __init__(self):
    # default count in each military position
    self.formations = Counter({
        Formation.Infantry: 50,
        Formation.Transport: 10,
        Formation.Supply: 10,
    })

    self.budget = 10000
