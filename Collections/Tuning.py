# -*- coding: utf-8 -*-
"""
Tuning Class
@author: Stuart Roland

Class for storing musical tunings. Based on temperaments or scales and reference pitches,
scales define series of musical notes.
Can edit the temperament/scale, what degrees comprise the scale, and what reference frequency defines the tuning.
Can load or write the temp/scale to .scl Scala scale files for compatibility with thousands of temperaments and scales.
"""

import Frequencies.Hz as Hz


class Tuning:
    def __init__(self, temperament=Scale.Scale([1], [0]), referencePitch=Hz(440), referenceNote=0, name='', description=''):
        self.temperament = temperament