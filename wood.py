cases = int(input())

for i in range(cases):
    waitTime = 0;
    currentTime = 0;
    customers = int(input())
    order = [0 for _ in range(customers)]
    for j in range(customers):
        nums = list(map(int, input().split()))
        pieces = nums[0]
        nums.remove(pieces);
        nums.sort()
        for k in range(pieces):
            order[j] += nums[k]
    order.sort()
    for j in range(customers):
        currentTime += order[j]
        waitTime += currentTime

    print(waitTime/customers)
