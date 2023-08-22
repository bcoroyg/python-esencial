import random

a = list(range(0, 100, 2))
b = list(range(0, 10, 1))

# Operaciones validas con listas
c = a + b
d = a * 2 
print(c)
print(d)

# Las operaciones que no se pueden realizar con arreglos son los siguientes.
# a / b
# a % b
# a - b

fruits = list()
fruits.append('apple')
fruits.append('banana')
fruits.append('orange')
print(fruits)

# pop(optional index) → remueve el ultimo elemento de la lista y retorna el valor eliminado.
some_fruits = fruits.pop()

print(some_fruits)

print(fruits)

# pop(index)
some_fruits = fruits.pop(0)
print(some_fruits)

print(fruits)

# keyword del [lista[index]]
del fruits[0]
print(fruits)

random_numbers = []

for i in range(10):
    random_numbers.append(random.randint(0, 15))

print('Randon numbers', random_numbers)

# Ordenamiento de lista - sorted(lista)
ordered_numbers = sorted(random_numbers)
print(ordered_numbers)

# Orden de una lista con el metodo sort()
random_numbers.sort()
print(random_numbers) 

# Obtener todos los metodos de una lista dir(lista)
print(dir(random_numbers))