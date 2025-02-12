file = open("C:\\Users\\tiko1\\Documents\\GitHub\\HOMEWORK\\Python lab 1\\tasks\\4_fourth_task\\input.txt")

data = file.read().split("\n")

return_text = ""

for row in data:
    words = row.split(" ")
    for word in words:
        if len(word) > 3:
            return_text += word
            if words.index(word) != len(words) - 1:
                return_text += ' '
    if data.index(row) != len(data) - 1:
        return_text +="\n"
file.close()
file = open("C:\\Users\\tiko1\\Documents\\GitHub\\HOMEWORK\\Python lab 1\\tasks\\4_fourth_task\\output.txt", "w")
file.write(return_text)
file.close()