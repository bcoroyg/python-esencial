import copy

coutries = ['Mexico', 'Venezuela', 'Colombia', 'Argentina']
ages = [12, 18, 21, 34, 50]
weights = [12,18, 21, 34, 50]
receta = ['Ensalada', 2, 'lechuga', 5, 'jitomates']
print(id(coutries))
print(id(ages))
print(id(weights))
# Las listas son mutables, ya que puede cambiar el estado una vez fue creado
coutries[0] = 'Ecuador'
print(coutries)

name = 'David'

print(name[0])

# Los string son inmutables, ya que no puede cambiar el estado una vez fue creado
# name[0] = 'A'

global_countries = coutries

# coutries[0] = 'Guatemala'

# print(global_countries)
# print(coutries)

# Copia de la lista
global_countries = None
global_countries = copy.copy(coutries)
coutries[0] = 'Guatemala'
print(global_countries)
print(coutries)

for country in global_countries:
    print(country)