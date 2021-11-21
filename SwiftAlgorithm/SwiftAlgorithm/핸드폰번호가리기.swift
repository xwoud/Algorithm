//
//  핸드폰번호가리기.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/11/21.
//

import Foundation

/// [핸드폰 번호 가리기](https://programmers.co.kr/learn/courses/30/lessons/12948)
/// - phone_number: 핸드폰 번호
/// - Returns: 가린 후 핸드폰 번호


func solution(_ phone_number:String) -> String {

    let changeNumber = phone_number.enumerated().map { (offset, element) -> String in
        if offset < (phone_number.count - 4) { return "*" }
        else { return "\(element)" }
    }

    return changeNumber.reduce("",+)

}
