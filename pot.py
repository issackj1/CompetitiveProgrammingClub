
num= int(input())

counter = 0
for i in range(num):
    num1 = input()
    num2 = len(num1)
    pw = int(num1[num2-1])
    num3 = int(num1[:num2-1])
    counter =  counter + pow(num3, pw)


print (counter)
