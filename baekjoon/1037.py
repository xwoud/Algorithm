import sys

N = int(sys.stdin.readline())
numbers = list(map(int, input().split()))
numbers.sort()

if len(numbers) == 1 :
    answer = numbers[0] * numbers[0]
else :
    answer = numbers[0] * numbers[-1]

print(answer)