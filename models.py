from collections import Counter
import enum


class Position(enum.Enum):
  Infantry = 'infantry'
  Transport = 'transport'
  Supply = 'supply'


class Military:
  def __init__(self):
    # default count in each military position
    self.breakup = Counter()
    self.breakup[Position.Infantry] = 50,
    self.breakup[Position.Transport] = 20,
    self.breakup[Position.Supply] = 10,
