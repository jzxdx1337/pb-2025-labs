nums = [5, 2, 8, 3, 1, 9, 4, 7, 6, 10]
print(nums)
if 3 in nums:
    index = nums.index(3)
    nums[index] = 30

print('Измененный список:', nums)