# -*- coding: utf-8 -*-
"""
Ratio Class
@author: Stuart Roland

Class that is able to store musical intervals as exact ratios as such and perform mathematical operations on them.
Can be cast to scalars/floats or cents when necessary.
Keeps ratios in nice, neat, musically useful form.


TODO
-add a method to check if float values can be easily converted to ratios
    -implement into both the setRatio as well as the operations 
"""

import Interval
import Cents
import Scalar


class Ratio(Interval.Interval):
    def __init__(self, numerator=1, denominator=1):
        self.num = 1
        self.den = 1
        self.setRatio(numerator, denominator)

    """ Get and Set Methods """

    def setRatio(self, numerator, denominator=1):
        if type(numerator) == str:
            # split the input into num and den whether the ratio is expressed as 'num/den' or 'num' or even 'num/ blah'
            splitInput = (''.join([c for c in numerator if c in '0123456789/'])).split('/')
            if len(splitInput) == 1:
                splitInput += [1]
            elif splitInput[1] == "":
                splitInput[1] = 1
            # cast and assign num and den
            self.num, self.den = int(splitInput[0]), int(splitInput[1])
        elif type(numerator) == int:
            self.num, self.den = int(numerator), int(denominator)
        elif type(numerator) == float:
            self.num, self.den = int(numerator), int(denominator)
        elif type(numerator) == Ratio:
            self.num, self.den = numerator.getNumerator(), numerator.getDenominator()
        # # Trying to handle non ratio values
        # elif type(numerator) == Cents.Cents:
        #     return Scalar.Scalar(numerator)
        # elif type(numerator) == Scalar.Scalar:
        #     return Scalar.Scalar(numerator)
        else:
            raise ValueError

        # simplify the ratio
        self.__simplify__()

        # make sure numerator carries the negative sign, if any
        self.__signSimplify__()
        # a musical ratio should never have a negative value

    def getCents(self):
        return self.scalarToCents(self.getScalar())

    def getScalar(self):
        return self.num / self.den

    def getNumerator(self):
        return self.num

    def getDenominator(self):
        return self.den

    def invert(self):
        oldNum = self.num
        self.num = self.den
        self.den = oldNum

    """ Internal Methods """

    def __gcd__(self, a, b):
        mx = max(abs(a), abs(b))
        mn = min(abs(a), abs(b))
        if mn == 0:
            return mx
            # if mx == 0:
            #     return 1
            # else:
            #     return mx
        else:
            return self.__gcd__(mx % mn, mn)

    def __simplify__(self):
        gcd = self.__gcd__(self.num, self.den)
        self.num = self.num / gcd
        self.den = self.den / gcd

    def __signSimplify__(self):
        if self.num < 0:
            if self.num < 0:
                self.num = abs(int(self.num))
                self.den = abs(int(self.den))
            else:
                self.num = -int(self.num)
                self.den = abs(int(self.den))
        elif self.den == 0:
            self.num = int(self.num)
            self.den = 1
            # print("Error: Denominator cannot be 0")
            raise ZeroDivisionError
        else:
            self.num = int(self.num)
            self.den = int(self.den)

        # interpret negation as inverting
        if self.num < 0:
            self.num = abs(self.num)
            self.invert()

    """ Casting """

    def __float__(self):
        return self.getScalar()

    def __str__(self):
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        return "Ratio(" + str(self) + ")"

    """ Operations """

    def __add__(self, other):
        if type(other) == Ratio:
            return Ratio(self.getNumerator() * other.getNumerator(), self.getDenominator() * other.getDenominator())
        elif type(other) == Scalar.Scalar:
            return Scalar.Scalar(self.getScalar() * other.getScalar())
        elif type(other) == Cents.Cents:
            return Cents.Cents(self.getCents() + other.getCents())

    # def __radd__(self, other):
    #     return self+other

    def __sub__(self, other):
        if type(other) == Ratio:
            return Ratio(self.getNumerator() * other.getDenominator(), self.getDenominator() * other.getNumerator())
        elif type(other) == Scalar.Scalar:
            return Scalar.Scalar(self.getScalar() / other.getScalar())
        elif type(other) == Cents.Cents:
            return Cents.Cents(self.getCents() - other.getCents())

    # def __rsub__(self, other):
    #     if type(other) == Ratio:
    #         return Ratio(other.getNumerator() * self.getDenominator(), other.getDenominator() * self.getNumerator())
    #     elif type(other) == Scalar.Scalar:
    #         return Scalar(other.getScalar() / self.getScalar())
    #     elif type(other) == Cents.Cents:
    #         return Cents(other.getCents() / self.getCents())

    def __mul__(self, other):
        if type(other) == int:
            if other >= 0:
                return Ratio(self.num * other, self.den)
            else:
                return Ratio(self.den * abs(other), self.num)
        elif type(other) == float:
            # return Scalar.Scalar(pow(self.getScalar(),other))
            return Scalar.Scalar(self) * other

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if type(other) == int:
            return Scalar.Scalar(self) / other
        elif type(other) == float:
            return Scalar.Scalar(self) / other

    def __neg__(self):
        return Ratio(self.den, self.num)
