from preprocess import *
import csv

# to combine csv files: $ cat *.csv > merged.csv

with open('/Users/timothy/Desktop/data/merged.csv', 'r') as f:
      reader = csv.reader(f)
      data = list(reader)

matrix = obtain_data_matrix(data)
samples = len(matrix)
print("Number of samples: " + str(samples))
#print(matrix[0]) #[[2680 1 0 0 0 0 0 0 4.9481 72 5 0]]

filament = matrix[:,[8]]
time = matrix[:,[9]]
satisfaction = matrix[:,[10]]
result = matrix[:,[11]]

cat_gift = matrix[:,[6]]

import numpy as np
import matplotlib.pyplot as plt

'''
#3D Plot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter([filament], [time], [satisfaction])'''

plt.figure(1)
plt.subplot(212)
plt.xlabel('Print Time (mins)')
plt.ylabel('Filament (m)')
plt.title('Filament Use')
plt.scatter([filament], [time])

plt.subplot(221)
plt.xlabel('Print Time (mins)')
plt.title('Rating')
plt.scatter([time], [satisfaction])

plt.subplot(222)
plt.xlabel('Print Time (mins)')
plt.title('Success / Fail / NIL')
plt.scatter([time], [result])

plt.tight_layout()
plt.show()


