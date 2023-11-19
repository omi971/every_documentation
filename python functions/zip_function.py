"""
Python Zip Function
just zip 2 things together
"""

name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]

# using zip() to map values
x = zip(name, roll_no)
y = zip(roll_no, name)

print(list(x))
print(list(y))

print('=====================================')
"""
x = enumerate()
enumerate just add index of the iterable and 
returns that in a tuple
"""

z = enumerate(zip(name, roll_no))
print(list(z))
