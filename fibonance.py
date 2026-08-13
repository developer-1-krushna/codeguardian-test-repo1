def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    series = [0, 1]
    
    for i in range(2, n):
        next_term = series[-1] + series[-2]
        series.append(next_term)
        
    return series

print(fibonacci_iterative(10))
