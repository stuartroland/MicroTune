from Collections import Temperament
from Intervals.Scalar import Scalar

"""Init Temperament and set to 19EDO"""
t = Temperament.Temperament()
t.setET(19)
print(t, '\n')

"""Stretch the Temperament so that it instead represents 19 notes of 12EDO"""
t.stretch(19 / 12)
print(t, '\n')

"""Change the type of intervals"""
t.setScalar()
print(t, '\n')

# cents = '344.345c cents 90234 fsd e'
# c = ''.join([c for c in cents.split()[0] if c in '0123456789.'])
# print(c, '\n')

"""Init new Temperament and set to Just Intonation JI5 temperament"""
ji5 = Temperament.Temperament()
ji5.setJI5()
print(ji5, '\n')

"""Init new Temperament and set to prexisting list with different input-interpretation parameters"""
testInput = [1, '3/2', 2, 3.0, '2400c']
testTemp = Temperament.Temperament()
testTemp.setIntervals(testInput)
print(testTemp, '\n')
testTemp.setIntervals(testInput, interpretAs='FLEX')
print(testTemp, '\n')
testTemp.setIntervals(testInput, interpretAs='RATIO')
print(testTemp, '\n')
testTemp.setIntervals(testInput, interpretAs='SCALAR')
print(testTemp, '\n')
testTemp.setIntervals(testInput, interpretAs='CENTS')
print(testTemp, '\n')

"""Init new Temperament, set to 12EDO, define and print Frequencies over a range beyond the fundamental range of the Temperament (below 0 and above 12)"""
tet12 = Temperament.Temperament()
tet12.setET(12)
print(tet12, '\n')

for i in range(-13, 14):
    print(Scalar(tet12[i]))
