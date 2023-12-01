def fibonacci(n):
    
    if n == 1 or n == 2:
        return 1
    
    l = [1,1]
    for i in range(2, n):
        a = l[i-1] + l[i-2]
        l.append(a)
        
    return l[-1]