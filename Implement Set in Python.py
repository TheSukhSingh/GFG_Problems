# Function to insert
# no return should be there, and no print statement
def insert(s, element):
    # Your code here
    s.add(element)
    
    
    

# Function to remove element from set
# No return and nothing to print
def remove_from_set(s, element):
    # Your code here
    s.discard(element)
    
    
    
    
# Function to find sum of elements in set
# return value should be there as sum
def sum_set(s):
    # Your code here
    a = 0
    for i in s:
        a += i
    return a
    