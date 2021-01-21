def pali(word):
    fst = word
    sst = word[::-1]
    if fst == sst:
        return True
    else:
        return False


f = open("pla.in", 'r')
x = int(f.readline())
for i in range(x):
    word = f.readline().strip()
    if pali(word) == True:
        print(1)
    else:
        print(0)
