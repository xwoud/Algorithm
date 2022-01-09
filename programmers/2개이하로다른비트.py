def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            bin_number = format(number, "b")
            point = bin_number.rfind("01")
            if point == -1:
                bin_number = "10" + bin_number[1:]
                answer.append(int(bin_number, 2))
            else:
                bin_number = bin_number[:point] + "10" + bin_number[point + 2:]
                answer.append(int(bin_number, 2))

    return answer