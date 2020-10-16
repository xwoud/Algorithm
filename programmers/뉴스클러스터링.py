def solution(str1, str2):

    list1 = [str1[n:n+2].lower() for n in range(len(str1)-1) if str1[n:n+2].isalpha()]
    list2 = [str2[n:n+2].lower() for n in range(len(str2)-1) if str2[n:n+2].isalpha()]
    tlist = set(list1) | set(list2)
    res1 = []
    res2 = []

    if tlist:
        for i in tlist:
            res1.extend([i]*max(list1.count(i), list2.count(i)))
            res2.extend([i]*min(list1.count(i), list2.count(i)))
        answer = int(float(len(res2)) / float(len(res1)) * 65536)
        return answer

    else:
        return 65536