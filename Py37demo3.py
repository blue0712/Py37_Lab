import numpy
import flask

l1 = ['a', 'b', 'c']
l2 = ['d', 'e', 'f']
print(l1 + l2)
l3 = [1, 2, 3]
l4 = [4, 5, 6]
print(l3 + l4)
print(l1 + l4)
a1 = numpy.array(l3)
a2 = numpy.array(l4)
print(a1, a2)
print(a1 + a2, a1 - a2, a1 * a2, a1 / a2, a1 ** a2)
print('flask = ' + flask.__version__)
