'''
Escribir un programa que pida al usuario 2 numeros enteros y calcular la suma desde el numero 1 hasta el numero 2.
Imprimir el resultado de la suma
'''

num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero: "))
num2 += 1
res = 0

for num in range(num1, num2):
    res += num

print(res)
