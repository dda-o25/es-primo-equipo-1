"""
Alumnos:
Leonardo Jesús Álvarez Fernández
Bruce de Bary Hernández Robles
José María Meléndrez Varela
Akemi Clarissa Olvera Arao
Fecha:07/10/25
Determinar si un número dado es primo
"""

# Declaraciones


# Entradas
numero = int(input("Introduzca un número: "))

# Proceso
# 'x' inicia siendo igual a dos porque todos los números son divisibles entre 1
# 'd' indica la cantidad de números por los que la variable 'numero' es divisble
x = 2
d = 0
primo = f"El número {numero} no es primo"
while x >= 2 and x <= numero:
    if numero % x == 0:
        d += 1
    x += 1
if d == 1:
    primo = f"El número {numero} sí es primo"


# Salidas
print(primo)
