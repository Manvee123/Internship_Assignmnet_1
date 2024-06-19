def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("Enter the number of Fibonacci numbers to generate: "))
fibonacci(num)