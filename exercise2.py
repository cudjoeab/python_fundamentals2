#Define a function called negative that 
# accepts a number as an argument and returns a boolean (true/false)
#  indicating whether that number is negative or not.

def negative(number):
    if  number < 0: 
        return True
    else:
        return False

number = 20
print(negative(number))