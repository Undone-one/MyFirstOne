# 1. Escriba un algoritmo para calcular la factorial de un número. Recuerda que la factorial de un número n es el producto de todos los números enteros positivos desde 1 hasta n.

number=int(input('Digite un número entero:'))
factorial=1
if number <0: 
    for i in range(1,number+1):
        factorial=factorial*i
        
print("CALCULADORA DE FACTORIAL")
print('Factorial:',factorial)
if number <0:
    print('Número no valido, el factorial de un número negativo no existe, ya que solo se trabajan en base a los números naturales, intente de nuevo')
