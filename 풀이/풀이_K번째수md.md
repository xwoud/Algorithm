# 🐶 프로그래머스 K번째 수 풀이
- Date : 2020.08.27(목)
- Time : 10분

## 풀이

- 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다. 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

```python
    answer1 = array[commands[i][0]-1:commands[i][1]]
    # i ~ j까지 잘라준 후
    answer1.sort()
    # 정렬시켜줍니다.
    answer2.insert(i,answer1[commands[i][2]-1])
    #그 후 k번째 숫자를 답 정렬에 추가해줍니다~
```