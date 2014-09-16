"""
package docstring
"""
import random


class Dice(object):
    sides = 0
    num_die = 0

    def __init__(self, sides, count):
        self.sides = sides
        self.num_die = count

    def roll(self):
        total = []
        for _ in xrange(0, self.num_die-1):
            total.append(random.randint(1, self.sides))
        return sum(total)