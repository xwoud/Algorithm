//
//  K번째수.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/16.
//

import Foundation

/// [프로그래머스 - K번째수](https://programmers.co.kr/learn/courses/30/lessons/42748?language=swift)
/// - Parameters:
///   - array: k번째 수를 배출할 배열
///   - commands: slice 할 범위와 k가 들어있는 배열
/// - Returns: K번째 수들의 집합
/**
 배열을 슬라이싱 하게되면 Array 형태로 저장되지 않고 **ArraySlice**의 형태로 저장된다.

 ArraySlice는 새로운 저장공간을 할당하는 것이 아니라 기존 Array에서 끌어와서 보여준다.

(기존 배열에 대한 참조)
 
 그렇기 때문에 ArraySlice의 시작 인덱스는 항상 0이 아니다.
 
 이런 문제로 슬라이싱 한 후에 Array로 형변환을 시켜주었다.
 
 그 이후 k번째 숫자를 answer 배열에 append 해줘서 return 해주었다.
 
 */
func solutionK(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    
    var answer: Array<Int> = []
    var sliceArray: Array<Int> = []
    
    for i in 0...commands.count-1 {
        
        sliceArray = Array(array[(commands[i][0]-1)...(commands[i][1]-1)]).sorted()
        answer.append(sliceArray[commands[i][2] - 1])
    }
    return answer
}
