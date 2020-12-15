//
//  두개뽑아서더하기.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/16.
//

import Foundation

/// [프로그래머스 - 두 개 뽑아서 더하기](https://programmers.co.kr/learn/courses/30/lessons/68644?language=swift)
/// - Parameter numbers: 수를 뽑을 수 있는 배열(Int형 배열)
/// - Returns: 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순을 리턴
///
/**
set 타입을 구현해서 **중복을 방지**했다.

insert와 remove를 이용해 메소드를 추가, 삭제 할 수 있다.
 
for문 안에 while문으로 기준 인덱스부터 이후의 인덱스끼리 더해주었다.

 */

func solution(_ numbers:[Int]) -> [Int] {
    var arrs: Set<Int> = []
    for i in 0..<numbers.count {
        var count = i+1
        while(count != numbers.count) {
            arrs.insert(numbers[i]+numbers[count])
            count += 1
        }
    }
    return Array(arrs).sorted()
}

