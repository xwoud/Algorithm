//
//  서울에서김서방찾기.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2021/01/24.
//

import Foundation

/// [서울에서 김서방 찾기](https://programmers.co.kr/learn/courses/30/lessons/12919?language=swift)
/// - Parameter seoul: Kim이 포함되어 있는 이름 배열
/// - Returns: seoul 배열에서의 Kim의 위치

/**
 
 for 문은 index를 찾아야함으로 숫자로 돌림
 
 
 그래서 만약 Kim을 찾으면 index를 저장한 후 break를 걸어서
 
 for문을 불필요하게 더 돌리지 않게 만듦.
 
 그리고 마지막에 return문에 index를 넣어서 출력함.
 
 
 */
func solution(_ seoul:[String]) -> String {
    
    var indexs = 0
    
    for i in 0..<seoul.count {
        if seoul[i] == "Kim" {
            indexs = i
            break
        }
    }
    return "김서방은 \(indexs)에 있다"
}
