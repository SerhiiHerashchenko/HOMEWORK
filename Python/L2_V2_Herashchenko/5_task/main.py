import numpy as np

file = open("C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L2_V2_Herashchenko\\5_task\\input.csv", 'r')

data = file.read().split(" ")
vector = np.array(data, int)



print(vector)