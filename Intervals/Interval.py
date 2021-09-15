# -*- coding: utf-8 -*-
"""
Interval Class
@author: Stuart Roland

Base class for intevals, parent class to Ratios, Cents, and Scalars.
"""

from math import log2, pow


class Interval:
    def __init__(self):
        pass

    """ Get and Set Methods """

    def getScalar(self):
        pass

    def getCents(self):
        pass

    """ Utility Methods """

    def scalarToCents(self, scalar):
        return 1200 * log2(scalar)

    def centsToScalar(self, cents):
        return 2 ** (cents / 1200)

    """ Casting """

    def __str__(self):
        return str(self.getScalar())

    def __float__(self):
        return self.getScalar()

    def __int__(self):
        return int(float(self))

    """ Operations """

    def __add__(self, other):

        return Interval()

    def __sub__(self, other):
        return Interval()

    def __mul__(self, other):
        return Interval()

    def __truediv__(self, other):
        return Interval()

    def __rmul__(self, other):
        return Interval()

    def __neg__(self):
        return Interval()

    """ Comparison Methods """

    def __lt__(self, other):
        if float(self) < float(other):
            return True
        else:
            return False

    def __le__(self, other):
        if float(self) <= float(other):
            return True
        else:
            return False

    def __eq__(self, other):
        if float(self) == float(other):
            return True
        else:
            return False

    def __ne__(self, other):
        if float(self) != float(other):
            return True
        else:
            return False

    def __ge__(self, other):
        if float(self) >= float(other):
            return True
        else:
            return False

    def __gt__(self, other):
        if float(self) > float(other):
            return True
        else:
            return False

    """ Other Built-in compatibility """

    def __repr__(self):
        return str(self)
