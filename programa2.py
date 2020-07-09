'''
Escribir un programa que pida al usuario 2 numeros enteros y calcular la suma desde el numero 1 hasta el numero 2.
Imprimir el resultado de la suma
'''

num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))
res = 0

for num in range(num1, num2 + 1):
    res += num

print(f"El resultado de la suma es: {res}")
