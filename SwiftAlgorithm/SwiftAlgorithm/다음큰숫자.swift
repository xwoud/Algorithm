//
//  소수만들기.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2021/01/31.
//

import Foundation

/// [다음 큰 숫자](https://programmers.co.kr/learn/courses/30/lessons/12911)
/// - Parameter n: 기준 숫자
/// - Returns: 2진수로 변환 시 n과 1의 갯수가 같은 n 다음으로 큰 수

/**
 
 먼저 기준이 되는 n의 2진수로 변환 시 1의 갯수를 세어서 저장해준다.
 
 그리고 while문은 처음에는 그냥 true문으로 돌고 if 문으로 검사 후에 break문을 걸려고 했으나,
 
 그냥 while문 자체에서 검사를 해주는 것이 낫다고 판단해서 while문에서 1의 갯수가 같은지 판단했다.
 
 number의 숫자를 계속 +1 해주면서 2진수로 바꿔가며 1의 갯수를 파악했다.
 
 */
func solution(_ n:Int) -> Int
{
    var answer: Int = 0
    var count: Int = 0
    
    let binary = String(n, radix: 2)
    
    for i in binary {
        if i == "1" {
            count += 1
        }
    }
    
    var number = n
    
    while answer != count {
        number += 1
        answer = 0
        for k in String(number, radix: 2) {
            if k == "1" {
                answer += 1
            }
        }
    }
    
    return number
}
