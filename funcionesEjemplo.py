'''
Escribir un programa que pida al usuario un texto y un entero. 
Mandar a imprimir en pantalla el texto repitido las veces indicado por el numero.
Hacer el programa usando una funcion

Ingresa un texto: Hola
Ingresa un numero: 4
Hola
Hola
Hola
Hola
'''

def repetir(texto,numero):
    texto += '\n'
    print(texto * numero)

t = input("Ingresa el texto: ")
n = int(input("Ingresa el numero de veces a repetir: "))

repetir(t,n)
