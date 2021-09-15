# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#
# if __name__ == '__main__':
#     unittest.main()


from Intervals.Ratio import Ratio
from Intervals.Cents import Cents
from Intervals.Scalar import Scalar

values = ['1', '4/3', '3/2', '9/5', '2']
ratios = []
scalars = []
cents = []
for i in range(5):
    ratios.append(Ratio(values[i]))
    scalars.append(Scalar(ratios[i]))
    cents.append(Cents(scalars[i]))

intervals = [ratios, scalars, cents]

"""Check comparisons between diff interval types"""
for i in range(3):
    for v in range(5):
        print(intervals[i][v], ' ')
        print(intervals[i][v] == intervals[(i + 1) % 3][v])
    print('\n')

"""Addition"""
print("Addition\n")

for i in range(3):
    print(intervals[i][1], ' + ', intervals[i][2], ' = ', intervals[i][1] + intervals[i][2])
print('\n')

for i in range(3):
    print(intervals[i][1], ' + ', intervals[(i + 1) % 3][2], ' = ', intervals[i][1] + intervals[(i + 1) % 3][2])
print('\n')

"""Subtraction"""
print("Subtraction\n")

for i in range(3):
    print(intervals[i][4], ' - ', intervals[i][2], ' = ', intervals[i][4] - intervals[i][2])
print('\n')

for i in range(3):
    print(intervals[i][4], ' - ', intervals[(i + 1) % 3][2], ' = ', intervals[i][4] - intervals[(i + 1) % 3][2])
print('\n')

for i in range(3):
    print(intervals[i][4], ' - ', intervals[(i - 1) % 3][2], ' = ', intervals[i][4] - intervals[(i - 1) % 3][2])
print('\n')

for i in range(3):
    print(intervals[i][4], ' - ', intervals[(i - 1) % 3][2], ' = ', intervals[i][4] - intervals[(i - 1) % 3][2])
print('\n')

"""Multiplication"""
print("Multiplication\n")

for i in range(3):
    print(intervals[i][4], ' * ', 3, ' = ', Cents(intervals[i][4] * 3))
print('\n')

for i in range(3):
    print(intervals[i][2], ' * ', 0.5, ' = ', intervals[i][2] * 0.5, ' == ', Cents(intervals[i][2] * 0.5))
print('\n')

for i in range(3):
    print(intervals[i][2], ' * ', -2, ' = ', intervals[i][2] * -2, ' == ', Cents(intervals[i][2] * -2))
print('\n')

for i in range(3):
    print(intervals[i][2], ' * ', -2.4, ' = ', intervals[i][2] * -2.4, ' == ', Cents(intervals[i][2] * -2.4))
print('\n')

for i in range(3):
    print(intervals[i][2], ' * ', 0, ' = ', intervals[i][2] * 0)
print('\n')

for i in range(3):
    print(intervals[i][2], ' * ', (2/7), ' = ', intervals[i][2] * (2/7))
print('\n')

"""Division"""
print("Division\n")

for i in range(3):
    print(intervals[i][4], ' / ', -2.1, ' = ', intervals[i][4] / -2.1, ' == ', Cents(intervals[i][4] / -2.1))
print('\n')

"""Ratio test"""
print(Ratio('2'), Ratio('3/2'), Ratio('4/'), Ratio('5 / 3'))

print(Ratio("5/4   E\ "))

