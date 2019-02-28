num_of_inputs = int(input())
nums = list(map(int, input().split()))
min_days = 1
nums.sort()

for i in range(num_of_inputs):
    the_max = nums[len(nums)-1-i]
    if((the_max + i) > min_days):
        min_days = the_max + i

print(min_days+2)
