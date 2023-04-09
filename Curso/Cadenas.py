texto = "Bienvenidos a las pruebas de cadenas feat Mau"

print(texto)
print(texto.lower()) #Imprime todo el contenido en minusculas
print(texto.upper()) #Imprime todo el contenido en mayusculas
print(texto.title()) #imprime el contenido con mayusculas al inicio de cada palabra

print(texto.find("au")) #indica la posicion de donde esta ese caracter
print(texto.count("a")) #indica cuantas veces se esta repitiendo ese caracter

textoFinal = texto.replace("e", "3")
print(textoFinal)       #reemplaza una cadena

valor = texto.isnumeric() #Arroja true o false dependiendo si es un numero
print(valor)

cadenaSeparada = texto.split(" ") #separa mediante un valor, parametro o cadena de texto la funcion split
print(cadenaSeparada)