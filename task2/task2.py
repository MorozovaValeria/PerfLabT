input_file_1 = input()
with open(input_file_1, 'r') as file_1:
    x_1, y_1 = map(float, file_1.readline().split())
    rad = float(file_1.readline())

input_file_2 = input()
with open(input_file_2, 'r') as file_2:
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