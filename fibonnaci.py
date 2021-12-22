

def determine_fib(n):
    if n == 0: return 0
    if n == 1 or n == 2:
        return 1
    return determine_fib(n - 1) + determine_fib(n - 2)


print(determine_fib(3))
print(determine_fib(4))