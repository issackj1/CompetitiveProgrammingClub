cases = int(input())

for i in range(cases):
    visited = set()
    cities = int(input())
    count = 0
    for j in range (cities):
        city = input()
        if city not in visited:
            count = count + 1
            visited.add(city)
    print(count)

