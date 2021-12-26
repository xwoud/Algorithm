//
//  소수찾기.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/12/26.
//

import Foundation

/// [소수 찾기](https://programmers.co.kr/learn/courses/30/lessons/12921?language=swift)
/// - n : 최대값
/// - Returns: 1~n 사이의 소수의 개수

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
