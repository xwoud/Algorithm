//
//  문자열을정수로바꾸기.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/11/28.
//

import Foundation

/// [문자열을 정수로 바꾸기](https://programmers.co.kr/learn/courses/30/lessons/12925)
/// - s : 정수로 바꾸고자 하는 문자
/// - Returns: s를 정수로 바꾼 값


func solution(_ s:String) -> Int {
    guard let num = Int(s) else {
        if s.starts(with: "-") {
            return Int(s.dropFirst())! * -1
        } else {
            return Int(s.dropFirst())!
        }
    }
    return num
}
