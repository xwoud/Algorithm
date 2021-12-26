# 🐽 문자열 내 p와 y의 개수
- Date : 2021.12.26(일)
- Time : 10분
- Language : Swift
<br>

## Problem

- 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

## Constraints
- 문자열 s의 길이 : 50 이하의 자연수
- 문자열 s는 알파벳으로만 이루어져 있습니다.

## Example

- s : "pPoooyY"
- result: true

<br><br>

## 풀이
```swift
func solution(_ s:String) -> Bool {

    let s = s.lowercased()
    let p = s.filter { $0 == "p" }.count
    let y = s.filter { $0 == "y" }.count

    return p == y
}
```
: 쉬운문제 ㅎㅎ 먼저 대소문자를 구분할 필요가 없기 때문에 전부 소문자로 바꿔주었다. 물론 모두 대문자로 바꿔주어도 된다. 그리고 filter라는 고차함수를 이용해서 p,y만 골라서 숫자를 세주었다. 물론 여기서 처음에 대소문자를 구분하지 않고 필터 안에 ```s.filter { $0 == "p" || $0 == "P"}.count``` 라고 사용해주어도 된다. 근데 그냥 나는 통일시켜주었다. 다른 풀이를 보니깐 ```components``` 함수를 사용했다. components는 특정 문자를 기준으로 쪼갠 결과값을 받는다. 그래서 얼마나 쪼갰는지를 비교한거 같다. 근데 나는 여기에는 filter가 더 의도에 맞는거 같다.