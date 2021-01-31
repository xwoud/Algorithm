//
//  소수만들기.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2021/01/31.
//

import Foundation

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
