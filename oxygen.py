#page 10

def calc(length, arr):
    smaller = arr[0]
    bigger = arr[0]
    #get max value
    for i in range(0, length):
        if arr[i] < smaller:
                smaller = arr[i]
        # if arr[i] > bigger:
        #     bigger = arr[i]
        if arr.index(arr[i]) > arr.index(smaller):
            bigger = arr[i]
        if arr[i] < smaller:
            if arr.index(arr[i]) < arr.index(bigger):
                smaller = arr[i]

    if(arr.index(bigger) > arr.index(smaller)):
        if (bigger - smaller) > 0:
            print(arr.index(smaller) + 1, arr.index(bigger) + 1, bigger - smaller)
        else:
            print(-1)
    else:
        print(-1)
f = open("oxy.in", 'r')
x = int(f.readline())
arr = [int(i) for i in f.readline().strip() if i != ' ']
calc(x, arr)
