//
//  체육복.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/25.
//

import Foundation
func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var my = lost
    var res = reserve
    for i in stride(from: lost.count-1, to: -1, by: -1) {
        if reserve.contains(lost[i]+1) || reserve.contains(lost[i]-1){
            my.remove(at: i)
            res.remove(at: i)
            
        }
    }
    return n-my.count
}
