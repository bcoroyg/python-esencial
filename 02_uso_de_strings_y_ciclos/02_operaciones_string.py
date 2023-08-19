""" 
Los strings tienen varios metodos que nos sirver para manipularlas

Algunos son:

upper
lower
find
startswith
endswith
capitalize
"""

texto = "hello, World"

arreglo = ["Pera", "Banana", "Melón"]
# Convierte a mayuscula toda la cadena
print(texto.upper())
# Convierte a minuscula toda la cadena
print(texto.lower())
# Convierte a mayuscula el primer caracter de la cadena y los demas en minusculas
print(texto.capitalize())
# Campara si el primer caracter de la cadena es igual al ingresado, retornando un "bool"
print(texto.startswith("h"))
# Campara si el ultimo caracter de la cadena es igual al ingresado, retornando un "bool"
print(texto.endswith("d"))
# El separator divide con el carácter "," -  retornando un arreglo
print(texto.split(","))
# Si el separator no es espeficado se divide con el carácter por default el cual es  " "
print(texto.split())
# Remplaza todos los caracteres de la cadena por el indicado (old, new)
print(texto.replace("l", "L"))
# Convierte un arreglo a una cadena separandolos por coma
print(type(texto.join(arreglo)))
print(texto.join(arreglo))
# Retorna el index del primer caracter que encuentra en la cadena de acuerdo al ingresado ("h"). 
print(texto.index("h"))
# Retorna todos los metodos que pueden trabajar con la cadena
print(dir(texto))

def my_function():
    "Este es un texto de ayuda de como utilizar esta función, el cual es conocido como docstrings"
    pass

# Retorna el docstring que contiene la función, el cual es necesario para documentar la funcion
print(help(my_function))