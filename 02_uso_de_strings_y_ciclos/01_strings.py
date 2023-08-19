country = "Guatemala"
# Obtiene el primer caracter
print(country[0])
# Obtiene el ultimo caracter
print(country[-1])
# Obtine la cantidad de caracteres que posee la cadena
print(len(country))
second_letter = country[1]
print(second_letter)

# Imprime la ubicación de memoria en la que se encuentra el caracter
print(id(second_letter))
print(id("u"))

print(id(country[3]))
print(id("t"))

print(id("O"))
print(id("o"))

color = "Blue"
print(id(color))
color += "s"
print(id(color))
