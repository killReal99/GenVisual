import matplotlib.pyplot as plt
import numpy as np
import csv

Iteration_convolution = []
Iteration_convolution_direct = []
Iteration_convolution_reverse = []
Iteration_main = []
Iteration_target = []

Economic_damage_convolution = []
Economic_damage_convolution_direct = []
Economic_damage_convolution_reverse = []
Economic_damage_main = []
Economic_damage_target = []

Costs_convolution = []
Costs_convolution_direct = []
Costs_convolution_reverse = []
Costs_main = []
Costs_target = []

Iteration_test = []
Economic_damage_test = []
Costs_test = []

with open('OneYear\\Convolution1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        Iteration_convolution.append(float(row[0]))
        Economic_damage_convolution.append(float(row[1]))
        Costs_convolution.append((float(row[2]) + float(row[3])))

with open('OneYear\\Convolution1Direct.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        Iteration_convolution_direct.append(float(row[0]))
        Economic_damage_convolution_direct.append(float(row[1]))
        Costs_convolution_direct.append((float(row[2]) + float(row[3])))

with open('OneYear\\Convolution1Reverse.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        Iteration_convolution_reverse.append(float(row[0]))
        Economic_damage_convolution_reverse.append(float(row[1]))
        Costs_convolution_reverse.append((float(row[2]) + float(row[3])))

with open('OneYear\\MainCriteria1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        Iteration_main.append(float(row[0]))
        Economic_damage_main.append(float(row[1]))
        Costs_main.append((float(row[2]) + float(row[3])))

with open('OneYear\\Target1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        Iteration_target.append(float(row[0]))
        Economic_damage_target.append(float(row[1]))
        Costs_target.append((float(row[2]) + float(row[3])))

with open('OneYear\\GenTest1.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        Iteration_test.append(float(row[0]))
        Economic_damage_test.append(float(row[1]))
        Costs_test.append((float(row[2]) + float(row[3])))
plt.plot(Iteration_convolution, Economic_damage_convolution, label='Метод свертки (равные веса)')
plt.plot(Iteration_convolution_direct, Economic_damage_convolution_direct, label='Метод свертки (прямо пропорциональные веса)')
plt.plot(Iteration_convolution_reverse, Economic_damage_convolution_reverse, label='Метод свертки (обратно пропорциональные веса)')
plt.title('Изменение экономического ущерба от ненадежности (1 атака в год)')
plt.xlabel('Итерация')
plt.ylabel('Рубли')
plt.legend(loc="right")
plt.show()

plt.plot(Iteration_convolution, Costs_convolution, label='Метод свертки (равные веса)')
plt.plot(Iteration_convolution_direct, Costs_convolution_direct, label='Метод свертки (прямо пропорциональные веса)')
plt.plot(Iteration_convolution_reverse, Costs_convolution_reverse, label='Метод свертки (обратно пропорциональные  веса)')
plt.title('Изменение затрат (1 атака в год)')
plt.xlabel('Итерация')
plt.ylabel('Рубли')
plt.legend(loc="right")
plt.show()

plt.plot(Iteration_convolution, Economic_damage_convolution, label='Метод свертки')
plt.plot(Iteration_main, Economic_damage_main, label='Метод главного критерия')
plt.plot(Iteration_target, Economic_damage_target, label='Метод целевого программирования')
plt.title('Изменение экономического ущерба от ненадежности (1 атака в год)')
plt.xlabel('Итерация')
plt.ylabel('Рубли')
plt.legend(loc="right")
plt.show()

plt.plot(Iteration_convolution, Costs_convolution, label='Метод свертки')
plt.plot(Iteration_main, Costs_main, label='Метод главного критерия')
plt.plot(Iteration_target, Costs_target, label='Метод целевого программирования')
plt.title('Изменение затрат (1 атака в год)')
plt.xlabel('Итерация')
plt.ylabel('Рубли')
plt.legend(loc="right")
plt.show()


# Преобразуем в numpy-массивы для удобства
x = np.array(Iteration_convolution)
y = np.array(Costs_convolution)
z = np.array(Economic_damage_convolution)
x1 = np.array(Iteration_main)
y1 = np.array(Costs_main)
z1 = np.array(Economic_damage_main)

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

# Преобразуем в numpy-массивы для удобства
x2 = np.array(Iteration_test)
y2 = np.array(Costs_test)
z2 = np.array(Economic_damage_test)

# Создаём 3D-график
fig = plt.figure(figsize=(9, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot_trisurf(x2, y2, z2, cmap='viridis', alpha=0.7)

# Подписи осей
ax.set_xlabel('Итерация')
ax.set_ylabel('Суммарные затраты на стр-во. и рек-ю.')
ax.set_zlabel('Экономический ущерб')

# Цветовая шкала
plt.title("3D Визуализация данных")
plt.show()