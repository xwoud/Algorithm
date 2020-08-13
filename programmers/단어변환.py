answer = 0

def check(begin, word):
    for i in range(len(begin)):
        if begin[:i] + begin[i + 1:] == word[:i] + word[i + 1:]:
            return True

def dfs(begin, target, words, cnt):
    global answer
    if begin == target:
        answer = cnt
        return
    else:
        if len(words) == 0:
            return
        for i in range(len(words)):
            if check(begin, words[i]):
                word = words[:i] + words[i + 1:]
                dfs(words[i], target, word, cnt + 1)

def solution(begin, target, words):
    dfs(begin, target, words, 0)
    return answer
