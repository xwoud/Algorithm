//
//  두정수사이의합.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/18.
//

import Foundation

/// [두 정수 사이의 합](https://programmers.co.kr/learn/courses/30/lessons/12912)
/// - Parameters:
///   - a: 시작 정수
///   - b: 끝나는 정수
/// - Returns: 시작 정수 ~ 끝나는 정수 사이의 숫자 합
/**


a,b 둘 사이의 대소관계과 명확하지 않기 때문에

**min,max**를 이용해서 작은 수부터 큰 수로 for문을 나간다.

그리고 사이 숫자를 sum에 더해서 합을 구한다.

 */

func solution1218(_ a:Int, _ b:Int) -> Int64 {
    var sum: Int = 0
    for i in min(a,b)...max(a,b) {
        sum += i
    }
    return Int64(sum)
}
