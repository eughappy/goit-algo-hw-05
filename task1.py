def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n <= 0: return 0 # Якщо значення 0 - вератємо 0 - умови точки стоп
        elif n == 1: return 1 # Якщо значення 1 - вератємо 1 - умови точки стоп
        elif n in cache: return cache[n] # Якщо значення у "кеші" одразу його достаємо

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Записуємо кожне значення у "кеш", щоб не обчислювати ще раз
        return cache[n]

    return fibonacci

fib = caching_fibonacci()

if __name__ == "__main__":
    while True:
        try:    
            num = int(input())
            print(fib(num))
        except:
            print("Введіть ціле число! Або ваше число занадто велике!")