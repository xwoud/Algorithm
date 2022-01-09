from itertools import combinations

def intersection_point(line1, line2):
    a,b,e = line1
    c,d,f = line2
    if a*d == b*c:
        return None
    x = (b*f-e*d)/(a*d-b*c)
    y = (e*c-a*f)/(a*d-b*c)
    if x == int(x) and y == int(y):
        return (int(x),int(y))
    
def solution(line):
    N = len(line)
    
    combs = list(combinations(line,2))
    points = set()
    for comb in combs:
        point = intersection_point(comb[0], comb[1])
        if point:
            points.add(point)
            
    xs = [p[0] for p in points]
    x_min = min(xs)
    x_max = max(xs)
    
    ys = [p[1] for p in points]
    y_min = min(ys)
    y_max = max(ys)
    
    answer = ['.' * (x_max-x_min+1)] * (y_max-y_min+1)
    for point in points:
        x,y = point
        answer[y_max-y] = answer[y_max-y][:x-x_min] + '*' + answer[y_max-y][x-x_min+1:]
        
    return [''.join(ans) for ans in answer]