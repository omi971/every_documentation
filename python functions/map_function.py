"""
Python Map function takes
map(function, iterable)
"""


def square(x):
    return x**2


print(square(3))
nums = [i for i in range(1, 6)]
print(nums)

result = map(square, nums)
print(list(result))

result1 = map(lambda x: x**2, nums)
print(list(result1))

result2 = map(lambda x: x + x, nums)
print(list(result2))
