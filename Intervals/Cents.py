# -*- coding: utf-8 -*-
"""
Cents Class
@author: Stuart Roland

Class that is able to store musical intervals as cent values. Able to cast to scalar/float values.
"""

import Intervals.Interval as Interval


class Cents(Interval.Interval):
    def __init__(self, cents=0.0):
        self.cents = 0.0
        self.setCents(cents)

    """ Get and Set Methods """

    def setCents(self, cents):
        if isinstance(cents, Interval.Interval):
            self.cents = cents.getCents()
        elif type(cents) == str:
            # strip input of num-numeric characters
            self.cents = float(''.join([c for c in cents.split()[0] if c in '0123456789.']))
        elif type(cents) == float:
            self.cents = cents
        elif type(cents) == int:
            self.cents = float(cents)

    def getCents(self):
        return self.cents

    def getScalar(self):
        return self.centsToScalar(self.getCents())

    def invert(self):
        self.cents = -self.getCents()

    """ Casting """

    def __float__(self):
        return self.getScalar()

    def __str__(self):
        return str(self.cents) + "c"

    def __repr__(self):
        return str(self)

    """ Operations """

    def __add__(self, other):
        if isinstance(other, Interval.Interval):
            return Cents(self.getCents() + other.getCents())

    # def __radd__(self, other):
    #     return self+other

    def __sub__(self, other):
        if isinstance(other, Interval.Interval):
            return Cents(self.getCents() - other.getCents())

    # # def __rsub__(self, other):
    #     if isinstance(other, Interval.Interval):
    #         return Cents(other.getCents() - self.getCents())

    def __mul__(self, other):
        if type(other) == int:
            return Cents(self.getCents() * other)
        elif type(other) == float:
            return Cents(self.getCents() * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if type(other) == int:
            return Cents(self.getCents() / other)
        elif type(other) == float:
            return Cents(self.getCents() / other)

    def __neg__(self):
        return Cents(-self.getCents())
