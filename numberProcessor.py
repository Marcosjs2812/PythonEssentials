#Procesador de Números.

line = input("Ingresa una línea de números: ")
total = 0
try:
    for num in line:
        total += float(num)
    print("El total es:", total)
except:
    print(num, "no es un numero.")