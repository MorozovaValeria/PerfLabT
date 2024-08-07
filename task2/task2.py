import os

input_file_1 = input()

current_directory = os.path.dirname(os.path.abspath(__file__))
full_path_1 = os.path.join(current_directory, input_file_1)

with open(full_path_1, 'r') as file_1:
    x_1, y_1 = map(float, file_1.readline().split())
    rad = float(file_1.readline())

input_file_2 = input()
full_path_2 = os.path.join(current_directory, input_file_2)

with open(full_path_2, 'r') as file_2:
    while True:
        l = file_2.readline()
        if not l:
            break
        x_2, y_2 = map(float, l.split())
        dist = ((x_2 - x_1) ** 2 + (
                    y_2 - y_1) ** 2)
        if dist == rad * rad:
            print(0)
        elif dist < rad * rad:
            print(1)
        else:
            print(2)

'''Для копирования текста ввода
1.txt
2.txt'''