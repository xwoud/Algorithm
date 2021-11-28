//
//  자릿수더하기.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/11/28.
//

import Foundation

/// [자릿수 더하기](https://programmers.co.kr/learn/courses/30/lessons/12931?language=swift)
/// - N : 자연수
/// - Returns: N의 자릿수를 모두 더한 값

func solution(_ n:Int) -> Int
{
    return String(n).reduce(0) { $0 + Int(String($1))! }
}
