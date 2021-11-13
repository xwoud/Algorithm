//
//  Maximum Subarray.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/11/14.
//

import Foundation

/// [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
/// - Parameter nums: 숫자 배열
/// - Returns: 합이 가장 큰 연속 하위 배열의 합


func maxSubArray(_ nums: [Int]) -> Int {
    if nums.isEmpty {
        return 0
    }
    
    var result = nums[0]
    var maxSub = nums[0]
    for i in nums[1..<nums.count] {
        maxSub = max(i, maxSub+i)
        result = max(maxSub, result)
    }
    return result
}
