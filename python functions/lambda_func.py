"""
Python lambda function
lambda parameters: operation, (arguments)

for example
x = lambda x: x**2, [1, 2, 3]
print(list(x)
--> gives us [1, 4, 9]
"""


def add(x, y):
    """
    :param x: First Variable
    :param y: Second Variable
    :return: Addition of Two Variable
    """
    return x+y


print(add(69, 1))
print(add(1, 2))

add2 = lambda x, y: x+y
print("Inside Lambda Function:", add2(69, 1))

# or we can do this
print((lambda x, y: x+y)(69, 1))

print('---------------------------------------')


# Let's see the map function
def my_map(my_func, my_iter):
    results = []
    for i in my_iter:
        new_item = my_func(i)
        results.append(new_item)
    return results


nums = [i for i in range(1, 6)]
cubed = my_map(lambda x: x**3, nums)
print(cubed)

print('---------------------------------------')

print('again map')
