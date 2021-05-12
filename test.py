import sys
ite = int(sys.stdin.readline().strip())
word = [sys.stdin.readline().strip() for _ in range(ite)]

word = sorted(set(word), key=lambda x: (len(x), x))
for w in word:
    print(w)
