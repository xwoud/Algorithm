
def solution(genres, plays):
    answer = []
    playGenresTime = {}
    allDict = {}

    # 해시 만들기
    for i in range(len(genres)):
        playGenresTime[genres[i]] = playGenresTime.get(genres[i], 0) + plays[i]
        print(playGenresTime)
        allDict[genres[i]] = allDict.get(genres[i], []) + [(plays[i], i)]

    genreSort = sorted(playGenresTime.items(), key=lambda x: x[1], reverse=True)

    for (genre, totalPlay) in genreSort:
        allDict[genre] = sorted(allDict[genre], key=lambda x: (-x[0], x[1]))
        answer += [idx for (play, idx) in allDict[genre][:2]]

    return answer

