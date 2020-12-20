//
//  내적.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/20.
//

import Foundation
/// [내적](https://programmers.co.kr/learn/courses/30/lessons/70128)
/// - Parameters:
///   - a: 1차원 배열
///   - b: 1차원 배열
/// - Returns: a와 b의 내적(a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1])
func solution(_ a:[Int], _ b:[Int]) -> Int {
    var result: Int = 0
    for i in 0..<a.count{
        result += a[i]*b[i]
    }
    return result
}
