import math
import random
import pandas as pd
import matplotlib.pyplot as plt
# Tabelke wykonano dzieki bibliotece terminaltables oraz poradnikowi zamieszczonemu na tej stronie: https://pypi.org/project/terminaltables/
from terminaltables import AsciiTable

PI = math.pi
max_power_of_n = 6

table_data = [
    ["Wielkosc probki", "Przyblizenie", "Blad wzgledny przyblizenia"]
]

plot_data = []
plot_estimates = []

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
    plot_data.append(size)
    plot_estimates.append(pi_approximation)

table = AsciiTable(table_data, "Aproksymacja Pi metoda Monte Carlo")
plt.figure(figsize=(10, 10))  

plt.plot(plot_data, plot_estimates, color='blue', label='Wyestymowane Pi')

plt.axhline(y=PI, color="red", linestyle="-", label="Wartosc pi")

plt.xlabel('Wielkosc probki')
plt.ylabel('Przyblizenie PI')
plt.title('Estymacja Pi Metoda Monte Carlo')

plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()

print(table.table)

