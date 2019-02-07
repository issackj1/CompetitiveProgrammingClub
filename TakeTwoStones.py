
num = int(input())
i =0
while(i+2 <= num):
    i+=2

num = num - i
if num % 2 == 0:
    print ("Bob")
else:
    print ("Alice")
