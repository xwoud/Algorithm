//
//  x만큼간격이있는n개의숫자.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/23.
//

import Foundation
/// [x만큼 간격이 있는 n개의 숫자](https://programmers.co.kr/learn/courses/30/lessons/12954)
/// - Parameters:
///   - x: 시작 숫자, 증가 수
///   - n: 총 리스트 갯수
/// - Returns: x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트
/**

 
for 문으로도 구현할 수 있지만 while문으로 특정 갯수 이전까지 돌게 구현함

while 문 안에서 count에 x만큼을 더해 계속 증가하게 만듦.

 */
func solution(_ x:Int, _ n:Int) -> [Int64] {
    var answer : Array<Int64> = []
    var count: Int64 = Int64(x)
    while answer.count != n {
        answer.append(count)
        count += Int64(x)
    }
    return answer
}
