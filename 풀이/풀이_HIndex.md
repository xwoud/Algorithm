# 🐶 프로그래머스 H-Inex 풀이
- Date : 2020.08.25(화)
- Time : 20분

## 풀이

- H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다. 위키백과1에 따르면, H-Index는 다음과 같이 구합니다. 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다. 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

```python
    for c in citations:
        if c > h_index:
            h_index += 1
    # citations을 큰 순으로 정렬한 다음 넘어가는 갯수만큼 h_index를 더해줍니다~ 
    # 앞에서 세는것보다 뒤부터 세는게 빨리 끝나는 경우가 있는것 같아서 뒤부터 시도했습니다!
```
