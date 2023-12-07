import os 

path = os.path.join(os.getcwd(), 'day_03/input/input')
with open(path) as file:
    text = file.readlines()


mat = []
for i, word in enumerate(text):
    row_list = []
    for j in word:
        row_list.append(text[3 * int(len(word)) + j])
    mat.append(row_list)
print(mat)