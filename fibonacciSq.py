# Fibonacci sequence starts here ################################################
import time
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum

start = time.time()
for n in range(1, 200):  # probando
    print(n, "->", fib(n))
end = time.time()
print("Tiempo de ejecución: ", end - start, "segundos")
# Fibonacci sequence ends here ##################################################
