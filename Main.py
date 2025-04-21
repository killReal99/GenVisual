import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D as ax
import csv

X = []
Y = []
Z = []

with open('GenResults.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        X.append(float(row[0]))
        Y.append(float(row[1]))
        Z.append(float(row[2]))


plt.plot(X, Y)
plt.title('Line Graph using CSV')
plt.xlabel('X')
plt.ylabel('Y')


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(X, Y, Z, label='parametric curve')

plt.show()