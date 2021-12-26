//
//  문자열내p와y의개수.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/12/26.
//

import Foundation

func solution(_ s:String) -> Bool {

    let s = s.lowercased()
    let p = s.filter { $0 == "p" }.count
    let y = s.filter { $0 == "y" }.count

    return p == y
}
