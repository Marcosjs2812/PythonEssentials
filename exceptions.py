# Exceptions management from the cisco course starts here #############################################
def read_int(prompt, min, max):
    flag = 1
    while flag:
        try:
            num = int(input(prompt))
            assert num >= min and num <= max
            return num
        except ValueError:
            print("Error: entrada incorrecta")
        except AssertionError:
            print("Error: el valor no está en el rango permitido")

v = read_int("Ingresa un numero entre -10 a 10: ", min=-10, max=10)
print("El número es:", v)