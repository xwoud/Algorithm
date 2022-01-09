//
//  괄호변환.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2022/01/02.
//

import Foundation

func pairString(_ p : String) -> Bool {
    if p.isEmpty { return true }
    var p = p
    var stack : [String] = []
    while p.isEmpty == false {
        let x = String(p.removeFirst())
        if stack.isEmpty { stack.append(x) }
        else if stack.last! == "(" && x == ")"
        { stack.removeLast() }
        else { stack.append(x) }
    }
    return stack.isEmpty
}

func solution(_ p : String) -> String {

    if p.isEmpty { return ""}
    else if pairString(p) { return p }

    var v = p
    var u = String(v.removeFirst())

    while u.filter { $0 == "("}.count != u.filter{$0 == ")" }.count {
        let x = v.removeFirst()
        u.append(x)
    }
    if pairString(u) {
        return u + transform(v)
    } else {
        let tmp = "(" + transform(v) + ")"
        u.removeFirst()
        u.removeLast()
        u = u.map {
            if $0 == "(" { return ")" }
            else { return "(" }
        }.reduce("") { $0 + $1 }
        return tmp + u
    }
}
