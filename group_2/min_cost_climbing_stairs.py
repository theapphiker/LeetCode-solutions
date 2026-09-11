# Find the minimum cost of climbing stairs where cost[i] is the cost of the i step.
# You can either climb one or two steps once you pay the cost.
# Link: https://leetcode.com/problems/min-cost-climbing-stairs/description/

class Solution:
    def min_cost_climbing_stairs(self, cost):
        grid = [0 for _ in range(len(cost)+1)]
        grid[0] = 0
        grid[1] = 0

        for i in range(2, len(cost)+1):
            option1 = cost[i-1] + grid[i-1]
            option2 = cost[i-2] + grid[i-2]
            grid[i] = min(option1, option2)
        return grid[-1]

x = Solution()
print(x.min_cost_climbing_stairs([10,15,20])) #15
print(x.min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1])) #6