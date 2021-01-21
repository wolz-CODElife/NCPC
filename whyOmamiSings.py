f = open("mult.in", 'r')
x = int(f.readline())

for i in range(x):
    length, ite = f.readline().split(' ')
    line = list(f.readline().split(' '))
    line = [int(item) for item in line]
    line.sort(reverse=True)
    count = 1
    for i in line[0 : int(ite)]:
        count *= i
    print(count)