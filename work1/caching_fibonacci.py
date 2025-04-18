def caching_fibonacci():
    cache = {}

    # Функция вычисления n-го числа Фибоначчи с кэшированием
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Пример использования
fib = caching_fibonacci()
print(fib(10))  
print(fib(15))  