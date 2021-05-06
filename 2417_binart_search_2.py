import sys

number = 122333444455555

start, end = 1, number//2
mid = 0

while start <= end:
    mid = (start + end) // 2
    target = mid**2

    if target > number or target <= 0:
        end = mid - 1
    elif target < number:
        start = mid + 1
    else:
        break

if number < target:
    mid += 1

print(mid)
