import matplotlib.pyplot as plt
import numpy as np
import csv

Iteration_one = []
Iteration_multi = []
Economic_damage_one = []
Economic_damage_multi = []
Costs_one = []
Costs_multi = []

with open('GenResults.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        Iteration_one.append(float(row[0]))
        Economic_damage_one.append(float(row[1]))
        Costs_one.append((float(row[2]) + float(row[3])))

with open('GenResultsMulti.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        Iteration_multi.append(float(row[0]))
        Economic_damage_multi.append(float(row[1]))
        Costs_multi.append((float(row[2]) + float(row[3])))

plt.plot(Iteration_one, Economic_damage_one, label='Экономический ущерб (однокритериальная)')
plt.plot(Iteration_multi, Economic_damage_multi, label='Экономический ущерб (многокритериальная)')
plt.title('Изменение экономического ущерба от ненадежности')
plt.xlabel('Итерация')
plt.ylabel('Рубли')
plt.legend(loc="right")
plt.show()

plt.plot(Iteration_one, Costs_one, label='Затраты (однокритериальная)')
plt.plot(Iteration_multi, Costs_multi, label='Затраты (многокритериальная)')
plt.title('Изменение затрат')
plt.xlabel('Итерация')
plt.ylabel('Рубли')
plt.legend(loc="right")
plt.show()

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(Iteration_one, Costs_one, Economic_damage_one, label='parametric curve')
ax.plot(Iteration_multi, Costs_multi, Economic_damage_multi, label='parametric curve')
plt.show()