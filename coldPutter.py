
num= int(input())

num2 = input().split()

counter = 0
for i in range(num):
    if(int(num2[i]) < 0):
        counter += 1


print (counter)
