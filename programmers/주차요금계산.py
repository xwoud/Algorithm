import math

def timeConvert(time):
    a, b = time.split(':')
    return int(a) * 60 + int(b)
    
def solution(fees, records):

    def parkingAccount(account):
        if account <= fees[0] : return fees[1]
        account = account - fees[0]
        return math.ceil(account / fees[2]) * fees[3] + fees[1]

    answer = []
    records = list(map(lambda x: x.split(' '), records))
    records.sort(key= lambda x: (x[1], x[0]))

    fee_dictionary = {string[1] : 0 for string in records}

    for i in records:
        if i[2] == "IN": 
            answer.append(i)
        else: 
            a = answer.pop()
            time = timeConvert(i[0]) - timeConvert(a[0])
            fee_dictionary[i[1]] += time
        
    for i in answer:
        time = timeConvert("23:59") - timeConvert(i[0])
        fee_dictionary[i[1]] += time
    answer = list(map(lambda x: parkingAccount(x), fee_dictionary.values()))
    
    return answer