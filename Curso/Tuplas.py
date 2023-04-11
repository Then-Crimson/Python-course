"""
Tuple:Es una estructura de datos propia de Python que permite almacenar distintos
valores, son inmutables: no cambian una vez inicializadas.
"""

tupla = (1, 2, 3)
print(tupla)
tupla2 = (7, "Mau", True, 230.9, 16 + 7j, "Felicidad", False)
print(tupla2)
tupla3 = (9, 3, (4, 5, 6))
print(tupla3)
print(tupla2[1])
# tupla2[1] = "Maau" esto genera un error
print(tupla2[-1])  # Acceder al ultimo elemento
print(tupla2[0:4])  # Permite ver los elementos desde la fase inicial hasta le valor asignado
print(tupla2[-2])  # permite ver el valor asignado desde la ultima parte

a, b, c = tupla
print(a)
print(b)
print(c)

tuplafinal = tupla + tupla3
print(tuplafinal)  # Es una combinacion de tuplas, para crear una nueva a partir de las anteriores

print(tuplafinal.count(2))  # sirve para contar los elementos respectivos seleccionados
print(tuplafinal.index(3))  # Indicar la primera ocurrencia donde encuentra un valor
