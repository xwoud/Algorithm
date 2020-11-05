# 🐣그래프 탐색하기 - BFS, DFS with 민희 🐣

## ⭐️ BFS - 너비 우선 탐색
- 같은 레벨(형제 노드)부터 탐색
- Key - Values의 형태 
- value는 리스트 형태로 제작
- value 순서는 상관 없음
- 시간 복잡도 : O(노드 수 + 간선수)

- ex) 
    
    <img width="218" alt="스크린샷 2020-11-04 오후 4 09 53" src="https://user-images.githubusercontent.com/51286963/98080291-89d22b00-1eb8-11eb-929d-dd2ff8364f88.png">

    | Key  | Value  | 
    | ------------| ------------ | 
    | A  | B, C  | 
    | B  | A, D  | 
    | C  | A, G, H, I  | 
    | D  | B, E, F  | 
    | E  | D | 
    | F  | D  | 
    | G  | C  | 
    | H  | C  | 
    | I  | C, J  | 
    | J  | I  | 
    - 코드 구현
    ``` python
    graph = dict()

    graph['A'] = ['B','C']
    graph['B'] = ['A','D']
    graph['C'] = ['A','G','H','I']
    graph['D'] = ['B','E','F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C','J']
    graph['J'] = ['I']

    # 결과값은 {'A': ['B', 'C'], 'C': ['A', 'G', 'H', 'I'], 'B': ['A', 'D'], 'E': ['D'], 'D': ['B', 'E', 'F'], 'G': ['C'], 'F': ['D'], 'I': ['C', 'J'], 'H': ['C'], 'J': ['I']}
    ```
- 자료구조 큐를 이용해 need_visit 큐(방문이 필요한 노드 정보)와 visited 큐(이미 방문한 노드 순서대로 정보)를 생성
    - need_visit 큐에서 **맨 앞 데이터를 pop(0)** -> visited 큐에 있는지 확인 
    1) 없다면 visited 큐에 push -> 그 데이터의 value 확인 -> need_visit에 순서대로 push : 턴 종료
    2) 있다면 아무것도 안하고 다음 턴으로 넘어가기
    ```python
    def bfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit :
        # need_visit이 비어있다면 노드들을 모두 순회했다고 이해할 수 있다.
        node = need_visit.pop(0)
        if node not in visited:
            # 아직 들리지 않은 노드이면
            visited.append(node)
            need_visit.extend(graph[node])
            #extend는 리스트에 리스트를 붙일 때 사용

    return visited
    # 방문한 노드가 순서대로 정리가 되어있다.
    ```
    : ['A', 'B', 'C', 'D', 'G', 'H', 'I', 'E', 'F', 'J']
    - 큐로 구현해보기 ( 큐로 하면 시간이 더 줄어드는거 같다. 그래서 엄청 간단한 문제 아니면 큐로 구현하는게 좋다고한다 ~)
    ```python
    from collections import deque

    def bfs_d(graph, start_node):
        need_visit = deque([start_node])
        visited = list()
        while need_visit:
            node = need_visit.popleft()
            # 제일 처음 데이터를 pop
            if node not in visited:
                visited.append(node)
                need_visit.extend(graph[node])
        return visited
    ```
    - 조금 다른 방식으로 한번 더 풀어보기
    ``` python
    def bfs_m2(graph, start_node):
        need_visit = deque([start_node])
        visited = list()
        while need_visit:
            node = need_visit.popleft()
            if node not in visited:
                visited.append(node)
                for k in graph[node]:
                #위의 코드와 다른 점
                    if k not in visited :
                        need_visit.append(k)
        return visited
    ```
    : 노드의 자식들을 무조건 방문해야할 리스트에 추가하지 않고, 방문을 안했던 자식들만 넣어주는 방법~
-------------------------------------

<br>

## 🌈 DFS - 깊이 우선 탐색
- 정점의 자식들을 먼저 탐색
- 왼쪽, 오른쪽 방향 순서는 상관 없음
- 시간 복잡도 : O(노드 수 + 간선수)
- ex) 위의 bfs와 같은 그래프 사용


    <img width="230" alt="스크린샷 2020-11-04 오후 4 47 44" src="https://user-images.githubusercontent.com/51286963/98083306-7e353300-1ebd-11eb-97c2-18440be5dea1.png">
- need_visit 스택(방문이 필요한 노드 정보)과 visit 큐(이미 방문한 노드 순서대로 정보)를 사용
    - *BFS는 두개의 큐를 사용하고, DFS는 스택1, 큐1 를 사용한다는 차이점~*
    - need_visit 스택에서 **맨 뒤 데이터를 pop()** -> visited 큐에 있는지 확인 
    1) 없다면 visited 큐에 push -> 그 데이터의 value 확인 -> need_visit에 순서대로 push : 턴 종료
    2) 있다면 아무것도 안하고 다음 턴으로 넘어가기

    ```python
    def dfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        # pop() -> 리스트의 맨 뒤에 있는 데이터를 가지고오고 삭제됨

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited
    ```
    : ['A', 'C', 'I', 'J', 'H', 'G', 'B', 'D', 'F', 'E']

    - 재귀함수를 이용한 dfs 구현해보기
    ``` python
    arr = [[],[2,3],[1,5],[1,4],[3,5],[2,4]]
    dfs(arr,1)
    visited = list()
    need_visit = list()
    def dfs(graph, start_node):
        need_visit.append(start_node)
        # 시작 노드를 제일 먼저 넣어줌
        while need_visit:
            node = need_visit.pop()
            # pop() -> 리스트의 맨 뒤에 있는 데이터를 가지고오고 삭제됨
            visited.append(node)
            # 방문했다는 것을 알려줌
            for i in graph[node]:
            # 방문한 노드의 자식 노드들을 보기
                if i not in visited:
                # 방문하지 않은 노드라면
                    dfs(graph,i)
                    # 재귀함수
    return visited
    ```
    : [1, 2, 5, 4, 3] ([1, 3, 4, 5, 2] 도 같은 결과이다. 왼쪽 오른쪽 순서는 상관 없기 때문에)

-------------
## ✏️ 기초 문제 풀어보기

1) [백준 1260번](https://www.acmicpc.net/problem/1260)
    - 난이도 : 하
    - 추천 풀이 시간 : 30분
    - 직접 위의 코드 이용해보기
    ``` python
    import sys
    def bfs(graph, start_node):
        for i in graph:
            i.sort()
            # 문제에서 정점 번호가 작은것을 먼저 방문한다고 했기 때문에 오름차순 정렬을 해주었다. 
        visited = list()
        need_visit = list()

        need_visit.append(start_node)

        while need_visit :
            node = need_visit.pop(0)
            if node not in visited:
                visited.append(node)
            need_visit.extend(graph[node])

        return visited

    def dfs(graph, start_node):
        for i in graph:
            i.sort(reverse=True)
            # 내림차순 정렬을 한 이유는 dfs는 리스트 맨 뒤에서부터 데이터를 가져오기 때문에 뒤에가 작은 숫자가 들어가야지 작은 정점이 먼저 방문하게 되기 때문이다.
        visited = list()
        need_visit = list()

        need_visit.append(start_node)

        while need_visit:
            node = need_visit.pop()
            if node not in visited:
                visited.append(node)
                need_visit.extend(graph[node])

        return visited


    N, M, V = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        x, y = map(int, sys.stdin.readline().split())
        arr[x].append(y)
        arr[y].append(x)
        # 방향이 있는 노드가 아니기 때문에 이렇게 두개 다 넣어줘야한다.
    # arr = [[], [2, 3], [5, 1], [4, 1], [5, 3], [4, 2]]
    # 0에는 아무것도 안들어가는 이유는 인덱스가 key의 역할을 하기 때문이다. 
    for i in dfs(arr,V):
        print(i,end=" ")
    print()
    for i in bfs(arr,V):
        print(i,end=" ")
    ```
    - queue를 이용한 선생님 코드
    ```python
    from collections import deque

    def dfs(v):
        print(v, end=' ')
        # 시작 노드 출력
        visited[v] = True
        # 시작 노드는 들린 노드라고 표시함
        for e in adj[v]:
        # 연결되어있는 자식 노드를 보며
            if not(visited[e]):
            # 자식 노드를 들리지 않았다면 
                dfs(e)
                #재귀를 이용해서 계속 시작 노드를 출력함

    def bfs(v):
        q = deque([v])
        while q:
            v = q.popleft()
            if not(visited[v]):
                visited[v] = True
                print(v, end=' ')
                for e in adj[v]:
                    if not visited[e]:
                        q.append(e)

    n, m, v = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, sys.stdin.readline().split())
        adj[x].append(y)
        adj[y].append(x)

    for e in adj:
        e.sort()
        # 먼저 정렬을 해주고 시작함.
    # adf = [[], [2, 3], [1, 5], [1, 4], [3, 5], [2, 4]]
    visited = [False] * (n + 1)
    # 각 노드에 대해 방문했는지를 True , False 로 나타내줌. 만약 visited[1] == True 라면 노드 1은 방문했다는 뜻.
    dfs(v)
    print()
    visited = [False] * (n + 1)
    bfs(v)
    ```

2) [백준 1697번](https://www.acmicpc.net/problem/1697)
    - 난이도 : 하
    - 추천 풀이 시간 : 30분
    ```python
    import sys
    from collections import deque

    MAX = 100001
    n, k = map(int, sys.stdin.readline().split())
    # n : 현재 위치, k : 도착해야하는 위치
    count = [0] * MAX
    # 현재 점의 최대값까지 만들어줌 -> N 조건 : 0 ≤ N ≤ 100,000
    # 100001 인 이유는 우리는 인덱스 0은 버리기 때문에 뒤에 1을 해준 것~
    def bfs():
        need_visit = deque([n])
        # 큐로 생성해줌. 이거 큐로 안풀고 그냥 리스트로 하면 런타임오류..
        while need_visit:
        # 방문해야할 리스트가 아직 남아있다면 
            now_pos = need_visit.popleft()
            # 현재 위치를 제일 왼쪽에서 pop 해주세요.
            if now_pos == k:
            # 현재 위치가 도착해야하는 위치라면
                return count[now_pos]
                #몇번째만에 왔는지 출력
            for next_pos in (now_pos - 1, now_pos + 1, now_pos * 2):
            #순간이동의 3가지 경우를 모두 본다
                if 0 <= next_pos < MAX and not count[next_pos]:
                #크기가 N조건을 넘지도 않고, 아직 가보지 않은 곳이라면(0이라면)
                    count[next_pos] = count[now_pos] + 1
                    # 현재 위치에서 1초 이동했다라는 뜻으로 +1을 해준다
                    need_visit.append(next_pos)
                    # 그리고 방문해야할 리스트에 노드를 넣어준다~
    ```