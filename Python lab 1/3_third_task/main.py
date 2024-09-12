file = open("3_third_task/test.txt")
carriage = []
rows = 15
cols = 36

data = file.read().split("\n")
for i in range(rows):
    row = data[i].strip()
    temp_row = row.split(" ")
    carriage.append([int(x) for x in temp_row])

file.close()

sold_seats = []

for row_index, row in enumerate(carriage):
    counter = 0
    for seat_index, seat in enumerate(row):
        if (seat_index + 1) % 2 != 0 and seat == 0:
            counter+=1
    sold_seats.append(counter)
    counter = 0

max_seats = max(sold_seats)
print(sold_seats.index(max_seats)+1)
