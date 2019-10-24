a1 = list('ABCDE')
print(type(a1), a1)
a2 = a1
a3 = a1[:]
a4 = list(a1)
print(type(a3))
print(a1, a2, a3, a4)
a1[0] = 'a'
a2[1] = 'b'
print(a1, a2, a3, a4)