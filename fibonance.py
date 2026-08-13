def fibonacci_recursive(n):
    
    if n <= 1:
        return n
    
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n_terms = 10
series = [fibonacci_recursive(i) for i in range(n_terms)]

print(series)

