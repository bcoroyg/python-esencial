################################
########## FUNCIONES ###########
################################
"""
Funciones: Se define con la palabra reservada junto a un nombre y unos 
paréntesis que reciben los parámetros a usar, terminando con dos puntos.
"""
def my_first_function():
    return "Hello, world!"

my_first_function()


################################
########## VARIABLES ###########
################################
"""
Variables: En Python todo es un objeto y las variables no se define su tipo 
de dato como en otro lenguajes de programación
"""

A = 3 
B = A


################################
############ LISTAS ############
################################
"""
Listas: Se declaran con corchetes, pueden tener cualquier tipo de dato hasta
otra lista.
"""
L = [22, True, "una lista", [1, 2]] 
print(L[0])


################################
############ TUPLAS ############
################################
"""
Tuplas: Se declaran con paréntesis y no pueden ser editados los datos 
de una tupla después de ser creado.
"""
T = (22, True, "una tupla", (1, 2)) 
print(T[0])


################################
######### DICCIONARIOS #########
################################
"""
En los diccionarios la primera cadena o número será la "key o llave" para acceder al segundo dato, 
el segundo dato será el dato al cual se puede acceder con la "key o llave" y 
los diccionarios son listas de llave:valor
"""
D = {"Kill Bill": "Tamarino", "Amelie": "Jean-Pierre Jeunet"}
print(D["Kill Bill"])


################################
######## CONVERSIONES ##########
################################
print(int(4.3)) # De flotante a entero:
print(float(4)) # De entero a flotante:
print(str(4.3)) # De entero a string:
print(list((4, 5, 2))) # De tupla a lista:


################################
###### OPERADORES COMUNES ######
################################
print("len() =>", len("key")) # Longitud de una cadena, lista, tupla, etc.
print("type() =>", type(4)) #Tipo de dato
print("map() =>", map(str, [1, 2, 3, 4])) #Aplicar una conversión a un conjunto como una lista:
print("round() =>", round(6.3243, 1)) #Redondear un flotante con x número de decimales:
print("range() =>", range(5)) # Generar un rango en una lista.
print("sum() =>", sum([1, 2, 4])) #Sumar un conjunto:

print("sorted() =>", sorted([5, 2, 1]) ) # Organizar un conjunto:
"""
append, count, extend, index, insert, pop, remove, 
reverse, sort son posibles comandos que puedes aplicar a una lista.
"""
lista = [5, 2, 1]
# print(dir(lista)) #  comandos que le puedes aplicar a x tipo de datos:

# print(help(sorted)) documentación de la función sorted

################################
############ CLASES ############
################################
"""
Clases: es la representación de un objeto. 
Para definir la clase utilizar "class" y el nombre. En caso de tener 
parámetros colocarla entre paréntesis.
"""

class Estudiante(object): 
    def __init__(self,nombre_r,edad_r): 
        self.nombre = nombre_r 
        self.edad = edad_r 

    def hola(self): 
        return "Mi nombre es %s y tengo %i años" % (self.nombre, self.edad) 
 
 #  clase Estudiante y se le envio "Emilio" y el numero entero 18.
e = Estudiante("Emilio", 18) 
print (e.hola())

################################
###### METODOS ESPECIALES ######
################################

"""
cmp(self,otro) Método llamado cuando utilizas los operadores de comparación para 
comprobar si tu objeto es menor, mayor o igual al objeto pasado como parámetro.

len(self) Método llamado para comprobar la longitud del objeto. len(obj)

init(self,otro) Es un constructor de nuestra clase, es decir, es un “método especial” 
que se llama automáticamente cuando se crea un objeto.
"""

################################
######## CONDICIONALES IF ######
################################

"""
La condicional "if" contiene los paréntesis es la comparación que debe cumplir.
"""
a=3
b=3
if ( a > b ):
 	print(a, "Es mayor que", b) 
elif ( a == b ): 
 	print(a, "Es igual que", b)  
else:
 	print(a, "Es menor que", b) 
        
################################
########## BUCLE FOR ##########
################################

"""
El bucle de for recorres una cadena o lista.

En el siguiente ejemplo "i" inicia en 0, por lo
solamente imprime del 0 al 9
"""

for i in range(10):
    print(i)

################################
######### BUCLE WHILE ##########
################################

"""
En este caso while tiene una condición que determina hasta cuándo se ejecutará. 
Dejará de ejecutarse en el momento en que la condición deje de cumplirse. 
"""
x = 0 
while x < 10: 
    print(x)
    x += 1