def prime(n):
    
    
    if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
        return True
    
    if n == 1 or n %2 == 0 or n % 3 == 0  or n % 5 == 0 or n % 7 == 0:
        return False
    
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count+= 1
            if count > 2:
                return False
    
    if count > 2:
        return False
    else:
        return True