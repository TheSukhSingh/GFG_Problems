def insert_dict(key, value, dict):
    
    # Your code here
    dict[key] = value
    

# deleting from dictionary
def del_dict(key, dict):
    
    # Your code here
    dict.pop(key)
    
    
    

# print marks of required name
def print_dict(key, dict):
    
    # Your code here
    if key in dict:
        print("Marks of",key,"is",dict.get(key))
    else:
        print(-1)