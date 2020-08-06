def solution(bridge_length, weight, truck_weights):
    time = 0
    arr = bridge_length * [0]
    current = 0

    while True:
        current -= arr.pop()

        if (truck_weights[0] + current) <= weight:
            arr.insert(0, truck_weights.pop(0))
            current += arr[0]
        else:
            arr.insert(0, 0)

        time += 1

        if len(truck_weights) == 0:
            break

    return (time + bridge_length)