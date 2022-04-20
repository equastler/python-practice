def two_sum(nums, target):
    inds = {}
    for i in range(len(nums)):
        if target - nums[i] in inds:
            return inds[target - nums[i]], i
        inds[nums[i]] = i

nums = [2,3,4,6,8]
target = 5
print(two_sum(nums, target))