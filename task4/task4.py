input_file = input()
with open(input_file, 'r') as f:
    list = [int(x) for x in f]
    n = sorted(list)
    center = n[len(n) // 2]

    count = 0
    for i in n:
        count += abs(i - center)

print(count)