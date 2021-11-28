//
//  평균구하기.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/11/28.
//

import Foundation

/// [평균 구하기](https://programmers.co.kr/learn/courses/30/lessons/12944)
/// - arr : int가 들어있는 배열
/// - Returns: 배열의 평균값

func solution(_ arr:[Int]) -> Double {
    return Double(arr.reduce(0) { $0 + $1 }) / Double(arr.count)
}
