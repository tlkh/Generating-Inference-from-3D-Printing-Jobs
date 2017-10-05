from preprocess import *
import csv

with open('merged.csv', 'r') as f:
      reader = csv.reader(f)
      data = list(reader)

matrix = obtain_data_matrix(data)
print(matrix)
