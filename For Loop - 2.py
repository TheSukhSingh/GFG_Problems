def utility():
    s=input().strip()
    a = len(s)
    
    
    for i in range(a): 
        if i % 2 == 0:
            print(s[i], end="")