import sys

N = int(sys.stdin.readline())
counting = {}
item = [input() for _ in range(N)]

for i in item:
    try: counting[i] += 1
    except: counting[i]=1

book_max = max(counting.values())
answer = []

for book, number in counting.items():
    if number == book_max:
        answer.append(book)

print(sorted(answer)[0])
