//
//  가운데글자가져오기.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/11/21.
//

import Foundation

/// [가운데 글자 가져오기](https://programmers.co.kr/learn/courses/30/lessons/12903)
/// - numbers: 단어
/// - Returns: 단어 s의 가운데 글자


func solution(_ s:String) -> String {
    let lists = s.map { "\($0)" }

    let k = s.count / 2
    if s.count % 2 == 0 {
        return "\(lists[k-1])\(lists[k])"
    } else {
        return "\(lists[k])"
    }
}
