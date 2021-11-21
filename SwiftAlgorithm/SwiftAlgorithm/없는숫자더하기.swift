//
//  없는숫자더하기.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/11/21.
//

import Foundation

/// [없는 숫자 더하기](https://programmers.co.kr/learn/courses/30/lessons/86051?language=swift)
/// - numbers: 숫자 배열
/// - Returns: numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수


func solution(_ numbers:[Int]) -> Int {
    let sum = (0..<10).reduce(0) { $0 + $1 }
    let numbersSum = numbers.reduce(0) { $0 + $1 }
    // numbers.reduce(0, +)
    return sum - numbersSum
}
