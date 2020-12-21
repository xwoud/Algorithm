//
//  3진법뒤집기.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/22.
//

import Foundation
/// [3진법 뒤집기](https://programmers.co.kr/learn/courses/30/lessons/68935?language=swift)
/// - Parameter n: 자연수 n
/// - Returns: n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수

/**
 
 n으로 받은 수를 계속 3으로 나눠 나머지를 배열에 저장한다.
 
 이렇게 저장된 arr는 뒤집힌 3진법 숫자가 된다.
 
 그렇기 때문에 for문에서 reversed()를 사용해서 뒤집어준다.
 
 여기서 뒤집힌 3진법 -> 10진법으로 바꾸지 않고 다시 뒤집어 준 이유는
 
 제곱을 할 때 0 인덱스부터 처리하기 위함이다.
 
 그래서 앞에서부터 3을 곱해가며 10진수로 변경해준다.
 
 */
func solution(_ n:Int) -> Int {
    
    var arr: Array<Int> = []
    var num: Int = n
    var result: Int = 0
    var start: Int = 1
    
    while num > 0 {
        arr.append(num%3)
        num /= 3
    }
    
    for i in arr.reversed() {
        result += start * i
        start *= 3
    }
    
    return result
}

// 다른 사람의 좋은 코드
func solutionAnother(_ n:Int) -> Int {
    let flipToThree = String(n,radix: 3)
    // String(n, radix: k)를 하면 n을 10진수에서 k진법으로 바꿔준다.
    let answer = Int(String(flipToThree.reversed()),radix:3)!
    // String(n, radix: k)! 를 하면 n을 k진법에서 10진수로 바꿔준다.
    return answer
    
}
