from math import floor
import sys

play, win = map(int, sys.stdin.readline().split())
average = floor((win*100) // play)
low, high = 0, 1000000000

if average >= 99:
    print(-1)
else:
    while low <= high:
        mid = (low + high) // 2
        x, y = play + mid, win + mid
        if floor((y*100) // x) > average:
            high = mid - 1
        else:
            low = mid + 1
    print(high + 1)
