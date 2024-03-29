# 🐽 소수 찾기
- Date : 2021.12.26(일)
- Time : 30분
- Language : Swift
<br>

## Problem

- 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요. 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다. (1은 소수가 아닙니다.)



## Constraints
- n은 2이상 1000000이하의 자연수입니다.


## Example

- n : 10
- result: 4

<br><br>

## 풀이
```swift
func solution(_ n:Int) -> Int {
    var primes = [Bool](repeating: true, count: n+1)
    let m = Int(sqrt(Double(n+1)))

    for i in stride(from: 2, to: m+1, by: 1) {
        if primes[i] {
            for j in stride(from: i+i, to: n+1, by: i) {
                primes[j] = false
            }
        }
    }
    return primes.filter { $0 == true }.count - 2
}
```
: 소수를 찾는 방법 중 에라토스테네스의 체를 이용한 풀이이다. 처음에는 완전 탐색을 이용했었는데 완전 탐색 시에는 시간 초과가 발생하였다. 에라토스테네스의 체 방법이다.
```
1. 내가 원하는 구간에 있는 수를 모두 나열한다
2. 자기 자신을 제외한 2의 배수를 지운다.
3. 자기 자신을 제외한 3의 배수를 지운다.
4. 자기 자신을 제외한 4의 배수를 지운다 -> 2의 배수에서 다 지워졌기 때문에 안 해도 된다.
5. 자기 자신을 제외한 5의 배수를 지운다.
-> 위를 반복하면 소수만 남는다.
```
먼저 모든 구간의 수를 소수라고 판단해둔다 -> True로 설정
이 구간은 0부터 시작되어서 n-1 까지 진행되기 때문에 애초에 getPrime 함수를 부를 때 원하는 구간 +1을 해서 소환했다.
이 이유는 인덱스 값이 숫자가 되기 위함이다 ! (ex. [2] -> 숫자 2가 소수인가 아닌가). for 문의 구간은 n의 제곱근까지 진행한다.
자기 자신은 제외하기 때문에 i+i 를 시작으로 잡고 계속 그 수의 배수만큼 늘려주면서 False 값으로 바꿔준다.
이제 True 인 값은 소수이기 때문에 소수인 인덱스 값만 배열에 저장해서 return 해준다.