//
//  문자열다루기기본.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2021/01/23.
//

import Foundation

/// [문자열 다루기 기본](https://programmers.co.kr/learn/courses/30/lessons/12918)
/// - Parameter s: 문자열
/// - Returns: 숫자로만 구성돼있는지 여부
/**
 
 길이는 혹 이므로 or로 표시, 숫자는 && 로 검사
 
 한번에 검사할 수도 있지만, 숫자부터 검사해
 count가 애초에 만족되지 않으면 if 문을 들어오지 않게 만듦었다.
 
 
 */

func solution(_ s:String) -> Bool {
    
    if s.count == 4 || s.count == 6 {
        if Int(s) != nil  {
            return true
        }
    }
    return false
}
