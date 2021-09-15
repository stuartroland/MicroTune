# -*- coding: utf-8 -*-
"""
Frequency Class
@author: Stuart Roland

Class for storing tempos as BPM frequency values. Can be operated upon with intervals.
"""

import Frequency
import Interval
import Scalar


class BPM(Frequency.Frequency):
    def __init__(self, freq=1.0):
        super().__init__(freq)

    """ Get and Set Methods """

    def setFreq(self, freq):
        self.setBpm(freq)

    def getFreq(self):
        return self.getBpm()

    def getHz(self):
        return self.bpmToHz(self.getBpm())

    def getBpm(self):
        return self.freq

    def setHz(self, hz):
        self.setBpm(self.hzToBpm(hz))

    def setBpm(self, bpm):
        self.freq = float(bpm)


    """ Casting """

    def __float__(self):
        return float(self.getHz())

    def __str__(self):
        return str(self.getFreq())+"BPM"

    """ Operations """

    def __add__(self, other):
        if isinstance(other, Interval.Interval):
            return BPM(self.getBpm() * float(other))
        elif type(other) == float or type(other) == int:
            return BPM(fself.getBpm() + other)

    def __sub__(self, other):
        if isinstance(other, Interval.Interval):
            return BPM(self.getBpm() / float(other))
        elif type(other) == float or type(other) == int:
            return BPM(self.getBpm() - other)
        elif isinstance(other, Frequency.Frequency):
            Scalar.Scalar((self.getBpm()-other.getBpm())/self.getBpm())

    def __mul__(self, other):
        if type(other) == float or type(other) == int:
            return BPM(self.getBpm() * other)

    def __truediv__(self, other):
        if type(other) == float or type(other) == int:
            return BPM(self.getBpm() / other)

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
