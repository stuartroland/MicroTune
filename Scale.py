# -*- coding: utf-8 -*-
"""
Scale Class
@author: Stuart Roland

Class for storing musical scales, composed of scale degrees of a temperament.
Can edit the underlying temperament or what degrees comprise the scale.
Can load or write to .scl Scala scale files for compatibility with thousands of temperaments and scales.
"""

import Temperament
import Ratio
import Cents


class Scale(Temperament.Temperament):
    def __init__(self, intervals=None, degrees=None, name='', description=''):
        super().__init__(intervals, name, description)
        if degrees is None:
            degrees = []
        self.degrees = degrees
        self.setDegrees(degrees)

    """Set and Get Methods"""

    def setDegrees(self, degrees=None):
        if degrees is None or len(degrees) == 0:
            self.resetDegrees()
        elif type(degrees) == str:
            self.degrees = [int(d) for d in degrees.split(',')]
        else:
            self.degrees = [int(d) for d in degrees]
        self.degrees.sort()

    def resetDegrees(self):
        self.degrees = list(range(len(self.intervals)))

    def clearDegrees(self):
        self.degrees = []

    def getDegrees(self):
        return self.degrees

    def removeDegree(self, degree):
        del self.degrees[self.degrees.index(degree)]

    def addDegree(self, degree):
        self.degrees.append(degree)
        self.degrees.sort()

    def numDegrees(self):
        return len(self.degrees)

    def setIntervals(self, intervals, interpretAs='FLEX'):
        super().setIntervals(intervals, interpretAs=interpretAs)
        self.resetDegrees()

    def append(self, interval, interpretAs='FLEX'):
        super().append(interval, interpretAs=interpretAs)
        self.addDegree(len(self.intervals) - 1)

    def getScale(self):
        return [self.intervals[d] for d in self.degrees]

    def clear(self):
        super().clear()
        self.clearDegrees()

    # def getNote(self,):

    """ Casting """

    def __repr__(self):
        tempStr = 'Scale('
        if len(self.name) > 0: tempStr += self.getName() + ', '
        tempStr += str(self)
        tempStr += ')'
        return tempStr

    def __len__(self):
        return self.numDegrees()

    """ Operations """

    def __contains__(self, item):
        return item in self.getScale()

    def __getitem__(self, item):
        return self.intervals[self.degrees[item]]

    def __setitem__(self, key, value):
        if isinstance(value, Interval.Interval):
            self.intervals[self.degrees[key]] = value
        elif type(value) == int:
            self.intervals[self.degrees[key]] = Ratio.Ratio(value)
        elif type(value) == float:
            self.intervals[self.degrees[key]] = Scalar.Scalar(value)

    def __delitem__(self, key):
        del self.intervals[self.degrees[key]]
        self.removeDegree(key)

    # def __add__(self, other):
    #     if isinstance(other, Collection):
    #         return Collection(self.getIntervals() + other.getIntervals())
    #     elif type(other) == list:
    #         return Collection(self.getIntervals() + other)
    #     elif isinstance(other, Interval.Interval) or type(other) == float or type(other) == int:
    #         return Collection(self.getIntervals() + [other])
    #

