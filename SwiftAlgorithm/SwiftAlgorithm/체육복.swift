//
//  체육복.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/25.
//

import Foundation
func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var newreserve = reserve
    var newlost = lost
    var studentnumber = n - lost.count
    for i in 0...reserve.count-1{
        for k in 0...lost.count-1{
        if newlost[k] == newreserve[i] {
            newreserve[i] = 0
            newlost[k] = 0
            studentnumber = studentnumber + 1
            break
        }
        }
    }
        
        for j in 0...newlost.count-1{
            for i in 0...newreserve.count-1 {
            if newreserve[i] == 0 || newlost[j] == 0 {
              continue
            }else if newlost[j] - 1 == newreserve[i] || newlost[j] + 1 == newreserve[i]{
                        newreserve[i] = 0
                        newlost[j] = 0
                studentnumber += 1
                break
                    }
                }
            }
    return studentnumber
}
