num_of_inputs = int(input())
nums = list(map(int, input().split()))
min_days = 1

for i in range(num_of_inputs):
    the_max = max(nums)
    nums.remove(the_max)
    if((the_max + i) > min_days):
        min_days = the_max + i

print(min_days+2)
