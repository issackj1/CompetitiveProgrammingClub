def find(pillars):
    if(pillars <= 3):
        return 1
    else:
        return 1 + find(pillars - 1)

num = int(input())

result = find(num)

print(result)