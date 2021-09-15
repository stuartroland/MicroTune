# -*- coding: utf-8 -*-
"""
Temperament Class
@author: Stuart Roland

Class for storing musical temperaments, collections of intervals which define a tuning,
independent of reference pitches or MIDI mappings.
Can be tuned to specific reference pitch to generate a specific temperament and/or mapped to MIDI note numbers.
Works with Ratios, Scalars, and Cents.
Can load or write to .scl Scala scale files for compatibility with thousands of temperaments and scales.
"""

import Collection
import Ratio
# import Scalar
import Cents


class Temperament(Collection.Collection):
    def __init__(self, intervals=None, name='', description=''):
        super().__init__(intervals, name, description)

    """Set and Get Methods"""

    def getEffectiveOctave(self):
        return self.intervals[-1]

    def setET(self, tonesPerOctave):
        if type(tonesPerOctave) != int:
            raise ValueError("tonesPerOctave must be an integer")

        self.setName(str(tonesPerOctave) + "TET")
        self.setDescription(str(tonesPerOctave) + " Tone Equal Temperament")
        self.setIntervals([(1200 * i / tonesPerOctave) for i in range(tonesPerOctave+1)], interpretAs='CENTS')

    def setJI5(self):
        self.setName("5-Limit JI")
        self.setDescription("12 tone 5-Limit Just Intonation Temperament")
        self.setIntervals("16/15,9/8,6/5,5/4,4/3,25/18,3/2,8/5,5/3,9/5,15/8,2", interpretAs="RATIO")


    """ Built-in compatibility """

    def __repr__(self):
        tempStr = 'Temperament('
        if len(self.name) > 0: tempStr += self.getName() + ', '
        tempStr += str(self)
        tempStr += ')'
        return tempStr

