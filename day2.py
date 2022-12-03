#!/bin/python3
import unittest
import lib

SIMPLE_INPUT = 'day2.txt'
SANITIZE_INPUT = 'day2.txt'
REAL_INPUT = 'day2_real.txt'

kinds = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
}

winlose = {
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win',
}

beats = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper',
}

notbeats = {v: k for k, v in beats.items()}

points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3,
}


def sanitize_one(filename):
  lines = lib.readlines(filename)
  letters = [l.strip().split(' ') for l in lines]
  return [(kinds[l], kinds[r]) for l, r in letters]


def sanitize_two(filename):
  lines = lib.readlines(filename)
  letters = [l.strip().split(' ') for l in lines]
  return [(kinds[l], winlose[r]) for l, r in letters]


def score_round_one(other, you):
  if you == other:
    return 3 + points[you]
  if beats[you] == other:
    return 6 + points[you]
  return 0 + points[you]


def transform_part_one(sanitized):
  return sum(score_round_one(*players) for players in sanitized)


def score_round_two(other, you):
  if you == 'Lose':
    return 0 + points[beats[other]]
  if you == 'Draw':
    return 3 + points[other]
  if you == 'Win':
    return 6 + points[notbeats[other]]
  raise ValueError(you)


def transform_part_two(sanitized):
  return sum(score_round_two(*players) for players in sanitized)


class Day2(unittest.TestCase):

  def test_sanitize(self):
    sanitized = sanitize_one(SANITIZE_INPUT)

    self.assertEqual(sanitized, [
        ('Rock', 'Paper'),
        ('Paper', 'Rock'),
        ('Scissors', 'Scissors'),
    ])

  def test_sanitize_two(self):
    sanitized = sanitize_two(SANITIZE_INPUT)

    self.assertEqual(sanitized, [
        ('Rock', 'Draw'),
        ('Paper', 'Lose'),
        ('Scissors', 'Win'),
    ])

  def test_transform(self):
    solution = transform_part_one(sanitize_one(SIMPLE_INPUT))

    self.assertEqual(solution, 15)

  def test_real(self):
    solution = transform_part_one(sanitize_one(REAL_INPUT))

    self.assertEqual(solution, 17189)

  def test_transform_two(self):
    solution = transform_part_two(sanitize_two(SIMPLE_INPUT))

    self.assertEqual(solution, 12)

  def test_real_two(self):
    solution = transform_part_two(sanitize_two(REAL_INPUT))

    self.assertEqual(solution, 0)


if __name__ == '__main__':
  unittest.main()
