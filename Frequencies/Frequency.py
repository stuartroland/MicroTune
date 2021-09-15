# -*- coding: utf-8 -*-
"""
Frequency Class
@author: Stuart Roland

Base class for musical frequencies. Can be operated upon with intervals. Can represent notes in Hz or beats in BPM.
"""

import Intervals.Interval as Interval
import Intervals.Scalar as Scalar


class Frequency:
    def __init__(self, freq=1.0):
        self.freq = freq
        self.setFreq(freq)

    """ Get and Set Methods """

    def setFreq(self, freq):
        self.freq = float(freq)

    def getFreq(self):
        return self.freq

    def getHz(self):
        return self.freq

    def getBpm(self):
        return self.hzToBpm(self.getFreq())

    def setHz(self, hz):
        self.freq = hz

    def setBpm(self, bpm):
        self.setFreq(self.bpmToHz(bpm))

    """ Utility Methods """

    def hzToBpm(self, hz):
        return hz/60.0

    def bpmToHz(self, bpm):
        return 60.0*bpm

    """ Casting """

    def __float__(self):
        return float(self.getFreq())

    def __int__(self):
        return int(float(self))

    def __str__(self):
        return str(self.getFreq())

    def __repr__(self):
        return str(self)

    """ Operations """

    def __add__(self, other):
        if isinstance(other, Interval.Interval):
            return Frequency(float(self) * float(other))
        elif type(other) == float or type(other) == int:
            return Frequency(float(self) + other)

    def __sub__(self, other):
        if isinstance(other, Interval.Interval):
            return Frequency(float(self) / float(other))
        elif type(other) == float or type(other) == int:
            return Frequency(float(self) - other)
        elif isinstance(other, Frequency):
            Scalar.Scalar((self.getFreq() - other.getFreq()) / self.getFreq())

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return Frequency(float(self) * other)

    def __truediv__(self, other):
        if type(other) == float or type(other) == int:
            return Frequency(float(self) / other)

    def __rmul__(self, other):
        return self*other

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
