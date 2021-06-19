def solution(inputString):

    exArray = []

    for i in inputString:

        if i == "0" :
            # 만약 들어온 수가 0이라면
            frontNumber = str(exArray[-1])
            # 그 앞에까지 나열된 숫자를 본다
            if len(frontNumber) == 1 :
                # 만약 나열된 숫자가 한자리면 수라면
                exArray = list(range(1, 11))
                # 현재 수는 10이라는 것을 알 수 있다

            else :
                # 만약 앞에 나열된 숫자가 두자리 수 이상이라면
                frontNumber = frontNumber[:-1] + i
                # 맨 뒤에 숫자를 뺀 앞자리 수를 가져온다
                exArray = list(range(1, int(frontNumber)+1))
                # 앞자리 수에 +1을 한 수에 맨 뒤에 0을 합성한게 이 수의 최소값이 된다.
                #(ex. 앞자리 수가 989이고 0이 나왔다면 98+1 하고 0을 합성한 990이 된)다

        elif int(i) not in exArray:
            # 만약 들어온 수가 0이 아니고, 현재 배열에도 없는 수라면( 한자리 수만 가능 )
            exArray = list(range(1,int(i)+1))

        else :
            # 한자리 수로는 존재한다면(두자리 수 이상이 되야하는 수)

            for k in range(1,99):
                # n은 1000미만이므로 세자리수에서 앞 두자리는 최대 99까지 가능

                exString = str(k) + i
                if int(exString) not in exArray:
                    exArray = list(range(1, int(exString) + 1))
                    break

    return exArray[-1]

print(solution("2349101"))