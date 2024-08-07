import os

input_file = input()

current_directory = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(current_directory, input_file)

with open(input_file, 'r') as f:
    list = [int(x) for x in f]
    n = sorted(list)
    center = n[len(n) // 2]

    count = 0
    for i in n:
        count += abs(i - center)

print(count)

'''Для копирования текста ввода:
numbers.txt'''