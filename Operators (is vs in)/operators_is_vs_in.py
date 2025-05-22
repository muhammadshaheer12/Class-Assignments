# -------- is Operator Example --------

# Creating two lists with the same content
x = [1, 2, 3]
y = [1, 2, 3]

# Assigning x to z (both now point to the same object in memory)
z = x

# Equality check (do x and y have the same content?)
print("x == y:", x == y)   

# Identity check (are x and y the same object in memory?)
print("x is y:", x is y)   

# Identity check (are x and z the same object?)
print("x is z:", x is z)   


# -------- in Operator Example --------

# Create a list
my_list = [10, 20, 30, 40]

# Check if 20 is in the list
print("20 in my_list:", 20 in my_list)  

# Check if 50 is in the list
print("50 in my_list:", 50 in my_list)  

# Create a string
my_string = "Python"

# Check if 'P' is in the string
print("'P' in my_string:", 'P' in my_string)  

# Check if 'z' is in the string
print("'z' in my_string:", 'z' in my_string)
