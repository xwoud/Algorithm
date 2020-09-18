def solution(n, times):
    answer = 0

    left = 1
    right = (len(times)+1) * max(times)

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for j in times:
            count += mid // j
            if count >= n: break

        if count >= n:
            answer = mid
            right = mid - 1

        elif count < n:
            left = mid + 1

    return answer

print(solution(6,[7, 10]))
