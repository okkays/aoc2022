#!/bin/python
import unittest
import lib

SIMPLE_INPUT = 'day1.txt'
SANITIZE_INPUT = 'day1.txt'
REAL_INPUT = 'day1_real.txt'


def sanitize(filename):
  calories = lib.readlines(filename)
  current_elf = []
  elves = [current_elf]
  for c in calories:
    if not c.strip():
      current_elf = []
      elves.append(current_elf)
      continue
    current_elf.append(int(c.strip()))

  return [e for e in elves if e]


def transform_part_one(sanitized):
  return max(sum(s) for s in sanitized)


def transform_part_two(sanitized):
  return sum(sorted(sum(s) for s in sanitized)[-3:])


class Day1(unittest.TestCase):

  def test_sanitize(self):
    sanitized = sanitize(SANITIZE_INPUT)

    self.assertEqual(
        sanitized,
        [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]])

  def test_transform(self):
    solution = transform_part_one(sanitize(SIMPLE_INPUT))

    self.assertEqual(solution, 24000)

  def test_real(self):
    solution = transform_part_one(sanitize(REAL_INPUT))

    self.assertEqual(solution, 71300)

  def test_transform_two(self):
    solution = transform_part_two(sanitize(SIMPLE_INPUT))

    self.assertEqual(solution, 45000)

  def test_real_two(self):
    solution = transform_part_two(sanitize(REAL_INPUT))

    self.assertEqual(solution, 209691)


if __name__ == '__main__':
  unittest.main()
