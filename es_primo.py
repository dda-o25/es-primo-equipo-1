"""
Alumnos:

Fecha:07/10/25
Determinar si un número dado es primo
"""

# Declaraciones


# Entradas
numero = int(input("Introduzca un número: "))

# Proceso
x = 2
p = 0
primo = f"El número {numero} no es primo"
while x >= 2 and x <= numero:
    if numero % x == 0:
        p += 1
    x += 1
if p > 1:
    primo
elif p == 1:
    primo = f"El número {numero} sí es primo"


# Salidas
print(primo)
