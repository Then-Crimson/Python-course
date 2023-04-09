#primea forma de concatenacion

texto1 = "Hola"
texto2 = "Mundo"
textofinal = texto1 + " " + texto2
print(textofinal)

#segunda forma mediante comodines

print("El saludo es: %s %s" % (texto1, texto2))

#tercera forma mediante uso format

saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
print(saludoFinal)

#cuarta forma (seudonimo)

saludoFinal2 = "Saludo: {x} {y}" .format(x=texto1, y=texto2)
print(saludoFinal2)

