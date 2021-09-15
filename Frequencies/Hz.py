# -*- coding: utf-8 -*-
"""
Frequency Class
@author: Stuart Roland

Hertz class for musical frequencies. Can be operated upon with intervals. Represents note frequencies as Hz.
"""

import Frequencies.Frequency as Frequency
import Intervals.Interval as Interval
import Intervals.Scalar as Scalar


class Hz(Frequency.Frequency):
    def __init__(self, freq=1.0):
        super().__init__(freq)

    """ Get and Set Methods """

    def setFreq(self, freq):
        self.setHz(freq)

    def getFreq(self):
        return self.getHz()

    def getHz(self):
        return self.freq

    def getBpm(self):
        return self.hzToBpm(self.getFreq())

    def setHz(self, hz):
        self.freq = float(hz)

    def setBpm(self, bpm):
        self.setFreq(self.bpmToHz(bpm))

    """ Casting """

    def __str__(self):
        return str(self.getFreq())+"Hz"

    """ Operations """

    def __add__(self, other):
        if isinstance(other, Interval.Interval):
            return Hz(float(self) * float(other))
        elif type(other) == float or type(other) == int:
            return Hz(float(self) + other)

    def __sub__(self, other):
        if isinstance(other, Interval.Interval):
            return Hz(float(self) / float(other))
        elif type(other) == float or type(other) == int:
            return Hz(float(self) - other)
        elif isinstance(other, Frequency.Frequency):
            Scalar.Scalar((self.getHz() - other.getHz()) / self.getHz())

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return Hz(float(self) * other)

    def __truediv__(self, other):
        if type(other) == float or type(other) == int:
            return Hz(float(self) / other)
