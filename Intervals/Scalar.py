# -*- coding: utf-8 -*-
"""
Cents Class
@author: Stuart Roland

Class that is able to store musical intervals as scalar (float) values. Able to cast to cent values.
"""

import Intervals.Interval as Interval


class Scalar(Interval.Interval):
    def __init__(self, scalar=1.0):
        self.scalar = scalar
        self.setScalar(scalar)

    """ Get and Set Methods """

    def setScalar(self, scalar):
        if isinstance(scalar, Interval.Interval):
            self.scalar = scalar.getScalar()
        elif type(scalar) == str:
            # strip input of num-numeric characters
            self.scalar = float(''.join([c for c in scalar.split()[0] if c in '0123456789.']))
        elif type(scalar) == float:
            self.scalar = float(scalar)
        elif type(scalar) == int:
            self.scalar = float(scalar)

    def getScalar(self):
        return self.scalar

    def getCents(self):
        return self.scalarToCents(self.getScalar())

    def invert(self):
        self.scalar = pow(self.scalar, -1)

    """ Casting """

    def __float__(self):
        return self.getScalar()

    def __str__(self):
        return str(self.scalar)

    def __repr__(self):
        return str(self)

    """ Operations """

    def __add__(self, other):
        if isinstance(other, Interval.Interval):
            return Scalar(self.getScalar() * other.getScalar())

    # def __radd__(self, other):
    #     return self+other

    def __sub__(self, other):
        if isinstance(other, Interval.Interval):
            return Scalar(self.getScalar() / other.getScalar())

    # def __rsub__(self, other):
    #     if isinstance(other, Interval.Interval):
    #         return Scalar(other.getScalar() / self.getScalar())

    def __mul__(self, other):
        if type(other) == int:
            return Scalar(self.getScalar() ** other)
        elif type(other) == float:
            return Scalar(pow(self.getScalar(), other))

    def __truediv__(self, other):
        if type(other) == int:
            return Scalar(pow(self.getScalar(), 1/other))
        elif type(other) == float:
            return Scalar(pow(self.getScalar(), 1/other))

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return Scalar(pow(self.getScalar(), -1))
