//
//  나누어떨어지는숫자배열.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/19.
//

import Foundation
/// [나누어 떨어지는 숫자 배열](https://programmers.co.kr/learn/courses/30/lessons/12910)
/// - Parameters:
///   - arr: 배열(Int, 길이 1 이상)
///   - divisor: 나눌 수(자연수)
/// - Returns: array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환
/**

 
arr에 있는 모든 숫자를 divisor로 나눠서 나머지가 0인 숫자만 answer에 저장한다.

 
그리고 return 시 answer이 비어있는지 검사하여 비어있다면 [-1] 아니라면 answer배열을 오름차순 정렬한 것을 리턴한다.
 */
func solution1219(_ arr:[Int], _ divisor:Int) -> [Int] {
    var answer: Array<Int> = []
    for i in arr {
        if (i % divisor) == 0 {
            answer.append(i)
        }
    }
    return answer.isEmpty ? [-1] : answer.sorted()
}
