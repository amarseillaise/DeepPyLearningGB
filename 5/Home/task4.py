# ✔ Создайте функцию-генератор чисел Фибоначчи (см. Википедию). Ограничимся первыми 100 числами

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
for i in range(100):
    print(next(fib))
