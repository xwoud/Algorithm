//
//  2016년.swift
//  SwiftAlgorithm
//
//  Created by 김민희 on 2020/12/17.
//

import Foundation
/// [프로그래머스 - 2016년](https://programmers.co.kr/learn/courses/30/lessons/12901)
/// - Parameters:
///   - a: month
///   - b: day
/// - Returns: Day of the week
/**
먼저 day 배열에는 각 달이 며칠까지 차 있는지를 넣어준다.

for문 안에서 현재 달의 이전 달까지의 모든 일 수를 더해준다.

그리고 해당 달의 남은 날을 더해주고 7로 나눠준다.(일주일)
 */
func solution2016(_ a:Int, _ b:Int) -> String {
    let week: Array<String> = ["FRI","SAT","SUN","MON","TUE","WED","THU",]
    let day: Array<Int> = [31,29,31,30,31,30,31,31,30,31,30,31]
    var sum: Int = -1
    for i in 0..<a-1 {
        sum += day[i]
    }
    sum += b
    return week[sum % 7]
}

