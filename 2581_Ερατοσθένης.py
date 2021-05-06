import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

minority = [False, False] + [True]*(N+1)
primes = []

for i in range(2, N+1):
    if minority[i] and i >= M and i <= N:
        primes.append(i)
    for x in range(i+i, N+1, i):
        minority[x] = False

if primes:
    print(sum(primes))
    print(primes[0])
else:
    print(-1)
