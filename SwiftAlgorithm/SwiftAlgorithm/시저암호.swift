//
//  시저암호.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/19.
//

import Foundation

/// [시저 암호](https://programmers.co.kr/learn/courses/30/lessons/12926)
/// - Parameters:
///   - s: 알파벳이 들어있는 문자열
///   - n: 밀고싶은 범위
/// - Returns: s를 n만큼 민 암호문
/**

먼저 s.utf16을 이용해서 아스키 코드로 변환시킨다.

아스키 코드에서 a~z : 97~122 이고 A~Z : 65~90이다. 공백은 32 이다.

먼저 공백은 그대로 둬야 하기 때문에 32일 때를 제일 먼저 검사해서 그대로 넣어준다.

그리고 i<=90 일 때(대문자)를 검사한 후, n만큼 민 문자열이 범위를 넘어간다면 -26를 해줘서 다시 대문자 앞으로 돌아간다.

그리고 나머지 else 문은 소문자일 때 이고, 대문자와 같이 검사를 한다.
UnicodeScalar를 이용해 다시 아스키코드를 Scalar(스칼라)값으로 바꾸고 String으로 타입 캐스팅 한 후, answer에 더해준다.
 
*/
func solution(_ s:String, _ n:Int) -> String {
    var answer: String = ""
    
    for i in s.utf16 {
        if i == 32 {
            answer += " "
        } else if i <= 90 {
            if Int(i)+n>90 {
                answer += String(UnicodeScalar(Int(i)+n-26) ?? " ")
            } else {
                answer += String(UnicodeScalar(Int(i)+n) ?? " ")
            }
        } else {
            if Int(i)+n>122 {
                answer += String(UnicodeScalar(Int(i)+n-26) ?? " ")
            } else {
                answer += String(UnicodeScalar(Int(i)+n) ?? " ")
            }
        }

    }
    return answer
}
