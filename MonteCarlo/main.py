import math
import random
import pandas as pd
# Tabelke wykonano dzieki bibliotece terminaltables oraz poradnikowi zamieszczonemu na tej stronie: https://pypi.org/project/terminaltables/
from terminaltables import AsciiTable

PI = math.pi
max_power_of_n = 8

table_data = [
    ["Wielkosc probki", "Przyblizenie", "Blad wzgledny przyblizenia"]
]

for n in range(1, max_power_of_n):
    counter = 0
    size = 10 ** n
    for i in range(size):
        x_cord = random.random() 
        y_cord = random.random()
        if math.sqrt(x_cord * x_cord + y_cord * y_cord) <= 1:
            counter += 1
    pi_approximation = 4 * counter / size
    relative_error = "{:.6f}".format((abs(PI - pi_approximation) / PI) * 100) + "%"
    table_data.append([size, pi_approximation, relative_error])

table = AsciiTable(table_data, "Aproksymacja Pi metoda Monte Carlo")
print(table.table)
