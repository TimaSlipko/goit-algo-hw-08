import heapq

def cable_sort(cables):
    h = [cable for cable in cables]
    heapq.heapify(h)

    total = 0

    while len(h) > 1:
        cost = heapq.heappop(h) + heapq.heappop(h)
        total += cost
        heapq.heappush(h, cost)

    return total

def main():
    arr = [1, 20, 5, 10, 2]
    cost = cable_sort(arr)
    print(cost)

    arr = [2, 3, 4, 6]
    cost = cable_sort(arr)
    print(cost)

if __name__ == '__main__':
    main()
