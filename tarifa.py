data = int(input())
months = int(input())
total = 0

for i in range(months):
    total = total + (data - int(input()))

print (total+data)