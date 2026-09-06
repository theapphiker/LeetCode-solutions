# Return the maximum amount of money you can rob from houses.
# Adjacent houses have shared security systems so you cannot rob from houses next to each other.
# Link: https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums) -> int:
        grid = [0 for _ in range(len(nums))]

        for i in range(len(grid)):
            if i == 0 or (i == 1 and nums[1] > nums[0]):
                grid[i] = nums[i]
            else:
                if nums[i] + grid[i-2] > grid[i-1]:
                    grid[i] = nums[i] + grid[i-2]
                else:
                    grid[i] = grid[i-1]
        return grid[-1]

x = Solution()
print(x.rob([2,7,9,3,1])) #12
print(x.rob([1,2,3,1])) #4
print(x.rob([200, 3, 500, 1000, 2])) #1200
print(x.rob([1,3,1,3,100])) #103
print(x.rob([8,9,9,4,10,5,6,9,7,9])) #45
                