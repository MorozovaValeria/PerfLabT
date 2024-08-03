n = int(input())
m = int(input())

answer = []
first_list = m * list(range(1, n + 1))
second_list = ['']
count = 0

while second_list[-1] != 1:
    second_list.clear()
    for i in range(count, m + count):
        second_list.append(first_list[i])
        count += 1
    answer.append(second_list[0])
    count -= 1

print(''.join(map(str, answer)))