def solution(nums):
    
    maxPocket = len(nums) // 2
    nums = set(nums)
    if len(nums) >= maxPocket:
        return maxPocket
    else:
        return len(nums)
