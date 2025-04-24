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


# Преобразуем в numpy-массивы для удобства
x = np.array(Iteration_one)
y = np.array(Costs_one)
z = np.array(Economic_damage_one)
x1 = np.array(Iteration_multi)
y1 = np.array(Costs_multi)
z1 = np.array(Economic_damage_multi)

# Создаём 3D-график
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

# Точечный график с цветовой картой (цвет зависит от Z)
scatter = ax.scatter(x, y, z, c=z, cmap='Blues', s=50)
scatter1 = ax.scatter(x1, y1, z1, c=z, cmap='Oranges', s=50)
# ax.plot_trisurf(x, y, z, cmap='viridis', alpha=0.7)

# Подписи осей
ax.set_xlabel('Итерация')
ax.set_ylabel('Суммарные затраты на стр-во. и рек-ю.')
ax.set_zlabel('Экономический ущерб')

# Цветовая шкала
plt.colorbar(scatter, label='Затраты однокритериальная')
plt.colorbar(scatter1, label='Затраты многокритериальная')


plt.title("3D Визуализация данных")
plt.show()