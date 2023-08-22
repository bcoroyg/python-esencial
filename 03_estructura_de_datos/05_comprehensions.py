import random
lista_numeros = list(range(100))

# List comprehension
pares = [numero for numero in lista_numeros if numero % 2 == 0]
print(pares)

student_uid = [1, 2, 3]
students = ['Juan', 'Jose', 'Larsen']

# Dictionary comprehension
student_with_uid = {uid: student for uid, student in zip(student_uid, students)}
print(student_with_uid)


random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(0, 3))

print(random_numbers)

# Set comprehension
not_repeated = {number for number in random_numbers}
print(not_repeated)