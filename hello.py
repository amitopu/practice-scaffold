import random
import math
def add(x, y):
    return x + y


num1 = math.floor(random.random() * 1000)
num2 = math.floor(random.random() * 1000)
result = add(num1, num2)
print(f"Sun of {num1} and {num2} is {result}")
