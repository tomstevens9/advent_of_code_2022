from enum import Enum, IntEnum

import sys


class Shape(IntEnum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

  @classmethod
  def from_str(cls, s):
    return {
      'A': cls.ROCK,
      'X': cls.ROCK,
      'B': cls.PAPER,
      'Y': cls.PAPER,
      'C': cls.SCISSORS,
      'Z': cls.SCISSORS,
    }[s]

class Outcome(Enum):
  LOSE = 1
  DRAW = 2
  WIN = 3

  @classmethod
  def from_str(cls, s):
    return {
      'X': cls.LOSE, 
      'Y': cls.DRAW, 
      'Z': cls.WIN, 
    }[s]

beats = {
  Shape.ROCK: Shape.SCISSORS,
  Shape.SCISSORS: Shape.PAPER,
  Shape.PAPER: Shape.ROCK,
}

loses = {v: k for k, v in beats.items()}


def part1(input):
  total = 0
  for move in input:
    s1, s2 = (Shape.from_str(s) for s in move)
    if s1 == s2:
      total += s2 + 3
    else:
      total += s2 + (6 if beats[s2] == s1 else 0)
  return total


def part2(input):
  total = 0
  for raw_shape, raw_outcome in input:
    shape= Shape.from_str(raw_shape)
    outcome = Outcome.from_str(raw_outcome)

    if outcome == Outcome.DRAW:
      total += 3 + shape
    elif outcome == Outcome.WIN:
      total += 6 + loses[shape]
    elif outcome == Outcome.LOSE:
      total += beats[shape]
  return total


input_filename = sys.argv[1]
moves = []
with open(input_filename) as f:
  input = [line.strip().split(' ') for line in f]

print(part1(input))
print(part2(input))
