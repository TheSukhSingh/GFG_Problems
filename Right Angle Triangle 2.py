def triangle(s):
    space = 0
    for i in range(s):
        space += 1
        if i == 0 :
            print("*")
            
        elif i == s-1:
            print("* "*s)
            
        else:
            print("*" + (" " * (2*space-2)) + "*")