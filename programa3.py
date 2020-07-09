'''
Escribir un programa que muestre al usuario el siguiente menu
'''

switch_menu = True

while switch_menu == True:
    print('''
    Menu principal

    S. suma
    R. Resta
    M. Multiplicacion
    D. Division
    A. Salir
    ''')
    opcion_usuario = input("Elige una opcion: ").upper()

    if opcion_usuario == "S":
        num1 = int(input("Dime el primer numero: "))
        num2 = int(input("Dime el segundo numero: "))
        print(f"La suma de los numeros es: {num1 + num2}")

    elif opcion_usuario == "R":
        num1 = int(input("Dime el primer numero: "))
        num2 = int(input("Dime el segundo numero: "))
        print(f"La resta de los numeros es: {num1 - num2}")

    elif opcion_usuario == "M":
        num1 = int(input("Dime el primer numero: "))
        num2 = int(input("Dime el segundo numero: "))
        print(f"La multiplicacion de los numeros es: {num1 * num2}")
    
    elif opcion_usuario == "D":
        num1 = int(input("Dime el primer numero: "))
        num2 = int(input("Dime el segundo numero: "))
        print(f"La division de los numeros es: {num1 / num2}")

    elif opcion_usuario == "A":
        print("Saliendo del programa...")
        switch_menu = False
    
    else: 
        print("Digite una opcion valida")