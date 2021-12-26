//
//  숫자문자열과영단어.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/12/26.
//

import Foundation

func solution(_ s:String) -> Int {

    let map = s.map { $0 }
    let number: Dictionary<String, String> = ["zero" : "0", "one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"]

    var answer = ""
    var result = ""
    for index in map {
        if index.isNumber {
            if let number = number[answer] {
                result += number
                answer = ""
            }
            result += String(index)
        } else {
            answer += String(index)
            if let number = number[answer] {
                result += number
                answer = ""
            }
        }

    }
    return Int(result)!
}
