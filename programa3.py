'''
Escribir un programa que muestre al usuario el siguiente menu
'''
while True:
    print('''
    Menu principal

    S. Suma
    R. Resta
    M. Multiplicacion
    D. Division
    A. Salir
    ''')
    opcion_usuario = input("Elige una opcion: ").upper()
    if opcion_usuario == "S" or opcion_usuario == "R" or opcion_usuario == "M" or opcion_usuario == "D":

        num1 = int(input("Dime el primer numero: "))
        num2 = int(input("Dime el segundo numero: "))

        if opcion_usuario == "S":
            print(f"La suma de los numeros es: {num1 + num2}")

        elif opcion_usuario == "R":
            print(f"La resta de los numeros es: {num1 - num2}")

        elif opcion_usuario == "M":
            print(f"La multiplicacion de los numeros es: {num1 * num2}")
    
        elif opcion_usuario == "D":
            print(f"La division de los numeros es: {num1 / num2}")

    elif opcion_usuario == "A":
            print("Saliendo del programa...")
            break
    else:
        if opcion_usuario != "SRMDA":
            print("Opcion invalida")