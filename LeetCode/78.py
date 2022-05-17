class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return 
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

my = Solution()
print(my.subsets([1,2,3]))