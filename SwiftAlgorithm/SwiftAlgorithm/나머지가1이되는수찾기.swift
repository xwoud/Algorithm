//
//  나머지가1이되는수찾기.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/11/21.
//

import Foundation

/// [나머지가 1이 되는 수 찾기](https://programmers.co.kr/learn/courses/30/lessons/87389)
/// - numbers: 자연수
/// - Returns: n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수


func solution(_ n:Int) -> Int {

    return (1..<n).filter { n % $0 == 1 }[0]
}
