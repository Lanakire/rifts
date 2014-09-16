"""
package docstring
"""
import random


class Dice(object):
    """
    Baseline dice class for random rolls. Like damage and such.
    """
    sides = 0
    num_die = 0

    def __init__(self, sides, count):
        """
        Initialization function for :class:`~rifts.rolling.Dice`.

        :param sides: Number of sides on each die.
        :type sides: int
        :param count: Number of dice.
        :type count: int
        :return: A new instance of the Dice class.
        :rtype: :class:`~rifts.rolling.Dice`
        """
        self.sides = sides
        self.num_die = count

    def roll(self, **kwargs):
        """
        Utility function which returns the result of a number of rolls on dice specified by the
        :class:`~rifts.rolling.Dice` objects attributes.

        :param kwargs: only valid argument is offset which is a positive or negative modifier to the result
        :type kwargs: dict
        :return: the sum of the random rolls and offset.
        :rtype: int
        """
        offset = kwargs.get('offset', 0)
        total = []
        for _ in xrange(0, self.num_die-1):
            total.append(random.randint(1, self.sides))
        return sum(total) + offset