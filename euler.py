# 3. Dado que el valor de ex se puede calcular por aproximación de la siguiente suma:
# e^x = 1 + x + x^2/2! + x^3/3! + x^4/4! + x^5/5! + ...

# El usuario ingresa x
x = float(input("Ingrese un número x: "))

suma = 1
termino = 1

for i in range(1, 10):  
    termino = termino * x / i
    suma = suma + termino

print("El valor aproximado de euler es:", suma)

