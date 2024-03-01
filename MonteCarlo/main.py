import math
import random

pi = math.pi

# n = int(input("podaj n: "))
n = 1000000
counter = 0

for i in range(n):
    x = random.random() 
    y = random.random()
    if math.sqrt(x*x + y*y) <= 1:
        counter += 1

print(4 * counter / n)

