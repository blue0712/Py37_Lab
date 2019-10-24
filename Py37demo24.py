import numpy

a1 = numpy.array([1, 2, 3, 4, 5, 1, 3, 5])
a2 = a1
a3 = a1.copy()
print(a1, a2, a3)
a1 *= 2
print(a1, a2, a3)