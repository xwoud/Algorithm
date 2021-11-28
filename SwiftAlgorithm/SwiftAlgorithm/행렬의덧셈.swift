//
//  행렬의덧셈.swift
//  SwiftAlgorithm
//
//  Created by 미니 on 2021/11/28.
//

import Foundation

/// [행렬의 덧셈](https://programmers.co.kr/learn/courses/30/lessons/12950)
/// - arr1, arr2 : 행렬
/// - Returns: arr1, arr2를 같은 행, 열 끼리 더한 행렬값
///
func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    return  zip(arr1, arr2).map { zip($0, $1).map { $0 + $1 }}}
