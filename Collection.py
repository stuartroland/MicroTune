# -*- coding: utf-8 -*-
"""
Interval Collection
@author: Stuart Roland

Base class for a collection of musical intervals, stored as Ratios, Scalars, or Cents objects.
"""

import Interval
import Ratio
import Scalar
import Cents
from math import log2


class Collection:
    def __init__(self, intervals=None, name="", description=''):
        if intervals is None:
            intervals = [Ratio.Ratio(1)]

        self.intervals = [Ratio.Ratio(1)]
        self.setIntervals(intervals)
        self.name = name
        self.description = description

    """ Get and Set Methods """

    def setIntervals(self, intervals, interpretAs='FLEX'):
        self.clear()
        self.append(Ratio.Ratio(1), interpretAs=interpretAs)
        if type(intervals) == list:
            for i in intervals:
                self.append(i, interpretAs=interpretAs)
        elif type(intervals) == str and ',' in intervals:
            for i in intervals.split(','):
                self.append(i, interpretAs=interpretAs)

    def append(self, interval, interpretAs='FLEX'):
        if len(self) == 0:
            self.intervals.append(Ratio.Ratio(1))
            self.setInterval(0, self.interpretInterval(interval, interpretAs=interpretAs))
        elif self.interpretInterval(interval, interpretAs=interpretAs) != Ratio.Ratio(1) and self[0] == Ratio.Ratio(1):
            self.intervals.append(Ratio.Ratio(1))
            self.setInterval(len(self) - 1, self.interpretInterval(interval, interpretAs=interpretAs))

    def setInterval(self, key, value):
        if key < 0 or key >= len(self):
            raise ValueError("Key must be non-negative and within the bounds of the collection.")
        elif isinstance(value, Interval.Interval):
            self.intervals[key] = value
        elif type(value) == int:
            self.intervals[key] = Ratio.Ratio(value)
        elif type(value) == float:
            self.intervals[key] = Scalar.Scalar(value)

    def delInterval(self, key):
        if key < 0 or key >= len(self):
            raise ValueError("Key must be non-negative and within the bounds of the collection.")
        else:
            del self.intervals[key]

    def getInterval(self, index):
        if len(self) == 1:
            return self.intervals[index]
        elif len(self) > 1:
            if 0 <= index < len(self):
                return self.intervals[index]
            else:
                return self.intervals[-1] * (index // (len(self) - 1)) + self.intervals[index % (len(self) - 1)]

    def getIntervals(self):
        return self.intervals

    def setCents(self):
        for i in range(self.numIntervals()):
            self.setInterval(i, Cents.Cents(self[i]))

    def setScalar(self):
        for i in range(self.numIntervals()):
            self.setInterval(i, Scalar.Scalar(self[i]))

    def setRatioScalar(self):
        for i in range(self.numIntervals()):
            if type(self.getInterval(i)) != Ratio.Ratio:
                self.setInterval(i, Scalar.Scalar(self[i]))

    def sort(self, key=None, reverse=False):
        self.intervals.sort(key=key, reverse=reverse)

    def stretch(self, factor):
        if type(factor) == int or type(factor) == float:
            for i in range(self.numIntervals()):
                self.setInterval(i, self.getInterval(i) * factor)

    def setName(self, name):
        self.name = str(name)

    def getName(self):
        return self.name

    def setDescription(self, description):
        self.description = str(description)

    def getDescription(self):
        return self.description

    def clear(self):
        # self.intervals = [Ratio.Ratio(1)]
        self.intervals = []
        self.setName('')
        self.setDescription('')

    def numIntervals(self):
        return len(self.intervals)

    """ Utility Methods """

    def scalarToCents(self, scalar):
        return 1200 * log2(scalar)

    def centsToScalar(self, cents):
        return 2 ** (cents / 1200)

    def interpretInterval(self, interval, interpretAs='FLEX'):
        if "FLEX" in interpretAs:
            if isinstance(interval, Interval.Interval):
                return interval
            if type(interval) == float:
                return Scalar.Scalar(interval)
            if type(interval) == int:
                return Ratio.Ratio(interval)
            if type(interval) == str:
                if ('/' in interval) or ("." not in interval and 'c' not in interval):
                    return Ratio.Ratio(interval)
                elif 'c' in interval or 'C' in interval:
                    return Cents.Cents(interval)
                else:
                    return Scalar.Scalar(interval)
        elif "CENT" in interpretAs:
            return Cents.Cents(interval)
        elif "SCALAR" in interpretAs:
            return Scalar.Scalar(interval)
        elif "RATIO" in interpretAs:
            return Ratio.Ratio(interval)

    """ Casting """

    def __str__(self):
        return str(self.intervals)

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.numIntervals()

    """ Operations """

    def __contains__(self, item):
        return item in self.intervals

    def __getitem__(self, item):
        return self.getInterval(item)

    def __setitem__(self, key, value):
        self.setInterval(key, value)

    def __delitem__(self, key):
        self.delInterval(key)

    def __add__(self, other):
        if isinstance(other, Collection):
            return Collection(self.getIntervals() + other.getIntervals())
        elif type(other) == list:
            return Collection(self.getIntervals() + other)
        elif isinstance(other, Interval.Interval) or type(other) == float or type(other) == int:
            return Collection(self.getIntervals() + [other])

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Collection([self[i] * other for i in range(len(self))])

    def __rmul__(self, other):
        return self * other

    """ Save and Load to/from Scala (SCL) Files"""

    # read a .scl Scala scale file
    # .scl file specification here: http://www.huygens-fokker.org/scala/scl_format.html
    def readSCL(self, filename):
        scl = open(filename, 'r')

        self.clear()
        self.setName(filename.split('/')[-1][:-4])

        i = 0  # non-comment line number
        interval = '0'

        self.append(Ratio.Ratio(1))

        for line in scl:
            if line[0] != '!':
                if i == 0:
                    self.setDescription(line)
                elif i > 1:
                    # Strip away whitespace and non-digit, non-"/" and non-"." characters
                    interval = ''.join([c for c in line.split()[0] if c in '0123456789./'])
                    if '.' in interval:
                        self.append(self.interpretInterval(interval, interpretAs="CENTS"))
                    else:
                        self.append(self.interpretInterval(interval, interpretAs="RATIO"))
                i += 1
        scl.close()

    # write to a .scl Scala scale file
    # .scl file specification here: http://www.huygens-fokker.org/scala/scl_format.html
    def writeSCL(self, filename):
        # create a new file, fails if this file already exists
        scl = open(filename, "x")
        scl.write("! " + filename.split('/')[-1] + '\n' + '!\n')
        scl.write(self.description + '\n')

        # exclude the first interval if it is the ratio or scalar 1 or 0 cents
        lenScl = len(self) - (self[0] == 1)
        scl.write(str(lenScl) + '\n' + '!')

        # for every interval other than the ratio or scalar 1 or 0 cents
        for r in range(len(self) - lenScl, len(self)):
            if type(self[r]) == Ratio:
                scl.write('\n' + str(self[r]))
            else:
                scl.write('\n' + str(self[r].getCents()) + ' c')
        scl.close()
