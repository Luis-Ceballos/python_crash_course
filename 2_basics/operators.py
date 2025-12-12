# Basic math operators 
print(1 + 2) # Addition operator
print(10 - 5) # Subtraction operator
print(5 * 3) # Multiplication operator 
print(4 / 2) # Division operator 
print(10 % 3) # Modulous operator gives you the remainder (3 goes into 10, 3 times with a remainder of 1)
print(9 ** 2) # Exponential powers operator raises to whatever power (9^2 -> 81)
print(10 // 3) # Floor division will only return the integer value not the float value -> 3

#Reassignment operators
a: int = 5
b: int = 10

a += 5 # Adds 5 to value of the variable 
# Any math operator can be used for reassignment (place operator before = sign)

# Comparison Operators 
print(10 == 10) # Returns True
print(10 == 5) # Returns False 
print(10 != 5) # Returns True
print(20 != 20) # Returns False
print(100 > 50) # Returns True
print(50 > 100) #Returns False
print(10 >= 10) # Returns True
print(10 <= 5) #Returns False

c: int = 24
d: int = 8
print(c > d and d < c) # Prints True since both statements are true
print(c > d or 2 < 1) # Will print True since one or the other has to be True
print(c < d or 2 < 1) # Will print False because neither statement is true

print(not(c < d or 2 < 1)) # Will print True because none of the statements are true
print(not(c > d or 2 < 1)) # Will print False because one statement is true 

e: int = 5
f: int = 10
g: int = 5
print(e is f) # Will print False 
print(e is g) # Will print True
print(e is not f) # Will print True

numbers: list[int] = [1, 2, 3, 4]
print(1 in numbers) # Will result to True
print(10 in numbers) # Will result in False
print(10 not in numbers) # Will result in True