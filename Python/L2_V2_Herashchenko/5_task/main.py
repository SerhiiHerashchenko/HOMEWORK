import numpy as np

file = open("C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L2_V2_Herashchenko\\5_task\\input.csv", 'r')

data = file.read().split(" ")
vector = np.array(data, int)

average = np.sum(vector)/vector.size

max_index = np.argmax(vector)

vector[max_index] = average

file.close()

file = open("C:\\ALL\\OTHER\\GitHub\\HOMEWORK\\Python\\L2_V2_Herashchenko\\5_task\\output.csv", "w")
file.write(str(vector))
file.close