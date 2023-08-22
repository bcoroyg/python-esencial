a = 1, 2, 3

print(type(a))

a = (1, 2, 3)
print(type(a))

print(a[0])
print(a[1])
print(a[2])

# IndexError: tuple index out of range
# print(a[3])

# Las tuplas y los strings son inmutables ya que no pueden ser modificadas durante su ejecucion
# TypeError: 'tuple' object does not support item assignment
# a[0] = 20
print(a)

a = 'Nombre'
# TypeError: 'str' object does not support item assignment
# a[0] = 'n'

a = (1, 1, 1, 2, 3, 4)

print(type(a))

print(dir(a))

print(a.count(1))
print(a.count(2))
print(a.index(1))
print(a.index(3))

# Type SET
a = set([1, 2, 3])
b = {3, 4, 5}

print(type(a))
print(type(b))

# TypeError: 'set' object is not subscriptable
# print(a[1])

a.add(3)

print(a)

a.add(20)
print(a)

c = a.intersection(b)
print('a ∩ b ⇒', c)

d = a.union(b)
print('a ∪ b ⇒', d)

e = a.difference(b)
print('a ≠ b ⇒', e)

f = b.difference(a)
print('b ≠ a ⇒', f)

a.remove(20)
print('Remove value 20 de "a" ⇒', a)

print(dir(a))