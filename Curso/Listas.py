# Listas: SOn estructuras de datos que nos permiten almacenar distintos valores
#  (equivalentes a los arrays en otros lenguajes de programacion)

# Son estructuras dinamicas, pueden MUTAR.

lista1 = ["Mau", 23, 26.3, True, "Dya", 52.9]
print(lista1)
print(lista1[:])  # Toda la lista
print(lista1[2])  # Uno en especifico
print(lista1[-1])  # Uno del final

print(lista1[0:3])  # Accede a una porcion de la lista
print(lista1[:2])  # Desde el inicio hasta el elemento asignado
print(lista1[3:])  # Desde el elemento asignado hasta el final

lista1.append("Madaghost")  # Add un elemento
print(lista1)
lista1.insert(4, "Bolivia")  # Insertar un elemento en una posicion dada
print(lista1)

lista1.extend(["Dayler", 120, False])  # Extender la lista
print(lista1)

print(lista1.index("Mau"))  # Saber en que posicion esta un elemento
lista1.remove(120)  # Elimina un elemento
print(lista1)

lista1.pop()  # Elimina el ultimo elemento de la lista
lista2 = ["Potosi", "Tomas Frias"]  # Unir listas
lista3 = lista1 + lista2
print(lista3)

print(lista2 * 4)
print("Madaghost" in lista1)  # Para ver si un elemento esta en la lista
