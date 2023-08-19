country = "Guatemala"
# Indexes: 012345678
# Obtiene el primer caracter
print(country[0])
# Obtiene el ultimo caracter
print(country[-1])

print(country[:3])
print(country[3:])
print(country[3:3])
print(country[:])
print(country[1:-1:2])

long_world = "ferrocarril"
print(long_world[1:4])
print(long_world[1:8])
# Invierte el orden de la cadena "lirracorref"
print(long_world[::-1])
# Inicia desde el principio : hasta el indice 8: vete de 3 en 3 pasos
print(long_world[:8:3])
# Inicia desde el principio : hasta el final: vete de 2 en 2 pasos
print(long_world[::2])