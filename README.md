 # Python Esencial

 * Python es un lenguaje de programación interpretado o de script que fue creado por Guido Van Rossum, que posee una sintaxis muy limpia, planeado para que cualquier persona pueda aprender a programar.
 
 ### Ventajas:
 * **Legible:** Sintaxis intuitiva y estricta.
 * **Multiplataformas:** Funciona para todo sistema operativo.
 * **Librerías:** Cuenta cuenta con muchas por defecto.
 * **Productivo:** Ahorra mucho código.

 ### Instalación de diferentes versiónes de Python en Linux:
 
```
 sudo apt-get install python[version]
```
* **Ejemplo:**
```
 sudo apt-get install python3.7
```

### REPL (Read-Eval-Print Loop)
* Es un programa que están a la espera de que se le escriba comandos para ser ejecutados continuamente, de ahí el nombre de lectura-evaluación-impresión-bucle.

* **Ingresar en la REPL desde la terminal:**

```
python3
```

* Para salir del REPL ingresar lo siguiente.
```
exit()
```

### Ejecutar código de un archivo.py
* Para ejecutar el archivo con Python 3 ingresar el siguiente comando.
```
python3 archivo.py
```

### Tipos de datos en Python:
* **Enteros (int):** Son todos los números, enteros y long.
    + Ejemplo: **1, 234, -123**
* **Flotantes (float):** Son todos los números decimales.
    + Ejemplo: **1.4, -12.332**
* **Booleanos (bool):** Son los valores Verdadero y Falso.
    + Ejemplo: **False, True**
* **Cadenas (str):** Es una cadena de texto. 
    + Ejemplo: **"Hello, world!"**
* **Listas:** Son un grupo o array de datos, puede contener cualquiera de los tipos de datos anteriores.
    + Ejemplo: **[1, "Hola", True, [1,2,3]]**
* **Tuplas:** Es un grupo de datos igual que una lista con la diferencia que una tupla después de ser creada no puede ser modificada.
    * Ejemplo: **(45, 32, 'hello', 3.1)**
* **Diccionarios:** Son un grupo de datos que se acceden a partir de {"clave":"valor"}:
    + Ejemplo: **{"edad": 15}**


### Programación
* Es una secuencia de instrucciones que describe que debe realizar una computadora.
* Las tareas que casi todos los programas realizan son:
    + Entrada de datos.
    + Salida de datos.
    + Condicionales.
    + Repeticiones.
    + Operaciones mátematicas.


### Instalación de tkinter
* La librería de turtle require la siguiente dependencia.
```
sudo apt-get install python3-tk 
``` 


### Entorno Virtual
* Creacion de entorno virtual.
```
virtualenv --python=python3 venv 
``` 

* Activacion de entorno virtual.
```
source venv/bin/activate 
``` 

### Editable
* Instalacion.
```
pip install --editable . 
``` 

* Which
```
which tv 
``` 

* Help
```
tv --help 
``` 

* Clients Help
```
tv clients --help  
``` 

* Clients Create
```
tv clients create  
``` 

* Clients List
```
tv clients list  
``` 

* Update Client
```
tv clients update <UID>  
``` 
