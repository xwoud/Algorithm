# 🥽 LeetCode 28. Implement strStr()
- Date : 2021.07.25(일)
- Time : 15분
<br>

## Problem

- Implement strStr(). Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
- Clarification:
    - What should we return when needle is an empty string? This is a great question to ask during an interview. For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


 
## Constraints
- 0 <= haystack.length, needle.length <= 5 * 10^4
- haystack and needle consist of only lower-case English characters.



## Example

- Input: haystack = "aaaaa", needle = "bba"
- Output: -1

<br><br>

## 풀이
```python
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) == 0 :
            return 0
        
        return haystack.find(needle)
```
: 생각보다 너무 간단했던 문제라 find와 비슷한 함수들, 바로 문자열을 찾을 수 있는 함수들에 대해 소개를 해보겠다.<br>
1. find() : 특정 문자열의 위치를 찾고 ```시작 위치를 반환```한다. 만약 찾지 못한다면 ```-1을 반환```한다. 리스트, 튜플, 딕셔너리 자료형에서는 find 함수를 사용할 수 없다.
2. rfind() : 특정 문자열의 위치를 찾고 ```끝나는 위치를 반환```한다. 만약 찾지 못한다면 ```-1을 반환```한다.
3. index() : find()와 유사, 역시 ```시작 위치를 반환```한다. 하지만 다른 점은 문자를 찾지 못한다면 ```ValueError 에러```가 발생한다. 문자열, 리스트, 튜플 자료형에서 사용 가능하고 딕셔너리 자료형에는 사용할 수 없다.