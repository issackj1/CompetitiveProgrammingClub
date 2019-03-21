from sys import stdin

for line in stdin:
    nums = list(map(int, line.split()))
    summ = sum(nums)
    print(summ // 2)
    
