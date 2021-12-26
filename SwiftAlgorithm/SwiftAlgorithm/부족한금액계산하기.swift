//
//  부족한금액계산하기.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/12/26.
//

import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int {
    var answer: Int = 0
    for i in Range(1...count) {
        answer += price * i
    }
    return (answer - money) > 0 ? (answer - money) : 0
}
