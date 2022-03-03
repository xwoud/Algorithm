def solution(id_list, report, k):
    answer = {}
    dictionary = {string : 0 for string in id_list}
    for a in set(report):
        victim, offender = a.split()[0], a.split()[1]
        if answer.get(offender) != None : 
            answer[offender] = answer[offender] + [victim]
        else:
            answer[offender] = [victim]

    for mail in filter(lambda x: len(answer[x]) >= k, answer) :
        for count in answer[mail]:
            dictionary[count] = dictionary[count] + 1
    
    return list(dictionary.values())