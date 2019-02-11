from sys import stdin

for line in stdin:
    word = list(map(int, line.split()))
    print(abs(word[0] - word[1]))
