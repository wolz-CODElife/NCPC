#Page 3
def vowel(word):
    steps = 0
    d_word = word
    trial = 0
    for x in d_word:
        trial += 1
        if x.lower() in "aeiou":
            d_word = d_word.replace(x, "")
            if steps == -1:
                steps += 1
            if trial == 1:
                steps = -1
    r_word = word[::-1]
    for i in r_word:
        if i.lower() in "aeiou":
            d_word = i + d_word
            steps += 1
    return steps
f = open('vowels.in', 'r')
lent = f.readline()
word = f.readline()
# print(vowel(word))
vowel(word)