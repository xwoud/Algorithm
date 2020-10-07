def solution(routes):
   answer = 0
   routes.sort(key=lambda x: x[1])
   camera = -300001
   for j in range(0, len(routes), 1):
       if camera < routes[j][0] :
           camera = routes[j][1]
           answer += 1
   return answer