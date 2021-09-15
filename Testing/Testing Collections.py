from Collections import Collection
from Intervals import Ratio, Cents

"""init a collection, append and set values"""
c = Collection.Collection([1.1, 1.5, 2])
c.append(Cents.Cents(1900))
c.append(3)
c[4] = Ratio.Ratio(31, 8)
print(c, '\n')

c.setRatioScalar()
print(c, '\n')

c.setScalar()
print(c, '\n')

c.setCents()
print(c, '\n')

c.setScalar()
print(c, '\n')

c.append(4)
print(c, '\n')
# c[-1] = 4

"""Concatenation"""
d = c + [4.2, 5]
print(d, '\n')

d = d + 5 + 5.2
print(d, '\n')

cc = c + c
print(cc, '\n')

"""Change the type of intervals in the collection"""
d.setScalar()
print(d, '\n')

d.setCents()
print(d, '\n')

"""Sorting"""
cc.sort()
print(cc, '\n')

cc.sort(reverse=True)
print(cc, '\n')
