#El siguiente codigo representa la sintaxis basica de las estructuras de comando de python#

#Variables#

# Asignación de variables
print("Imprimiremos una cadena con variables reutilizables")

nombre = "Javier"        # Cadena (str)
edad = 27              # Entero (int)
altura = 1.82          # Flotante (float)
es_estudiante = True   # Booleano (bool)


# 1.  Imprimir valores

print(f"Hola, soy {nombre} y tengo {edad} años.")

# Estructura básica
if edad >= 18:
    print("Eres mayor de edad.")
elif 13 <= edad < 18:
    print("Eres un adolescente.")
else:
    print("Eres menor de edad.")

# 2. Condicional anidado
if es_estudiante:
    print("Eres estudiante.")


# Operadores comunes:

# ==: igual a
# !=: diferente de
# <, >, <=, >=: comparadores
# and, or, not: operadores lógicos


# 3. Ciclos

#Repeticion de un bloque de codigo

# For

# Iterar sobre una lista
frutas = ["manzana", "plátano", "naranja"]
for fruta in frutas:
    print(fruta)

# Usar range()
for i in range(1, 6):  # Del 1 al 5
    print(i)

# while

contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1  # Incrementar contador

# break: Termina el ciclo
# continue:  Salta a la siguiente iteración

for i in range(10):
    if i == 5:
        break  # Detener el ciclo cuando i sea 5
    if i % 2 == 0:
        continue  # Saltar números pares
    print(i)


# Funciones 

# Las funciones agrupan un conjunto de instrucciones que se puedan reutilizar.

# Definición de una función
def saludar(nombre):
    print(f"Hola, {nombre}")

# Llamar la función
saludar("Luis")

# Función con retorno
def suma(a, b):
    return a + b

resultado = suma(5, 3)
print(f"El resultado es: {resultado}")

# Función con valores por defecto
def presentar(nombre, edad=18):
    print(f"Soy {nombre} y tengo {edad} años.")

presentar("Ana")  # Usa el valor por defecto de edad
presentar("Mario", 25)
