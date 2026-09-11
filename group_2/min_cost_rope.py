# Minimum time to make colorful rope where the same color is not next to each other.
# Link: https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

class Solution:
    def minCost(self, colors: str, neededTime) -> int:
        seen = 0
        result = 0

        for i in range(1, len(colors)):
            if colors[i] == colors[seen]:
                if neededTime[i] > neededTime[seen]:
                    result += neededTime[seen]
                    seen = i
                else:
                    result += neededTime[i]
            else:
                seen = i
        return result

x = Solution()
print(x.minCost("aabaa", [1,2,3,4,1])) #2
print(x.minCost("abc", [1,2,3])) #0
print(x.minCost("abaac", [1,2,3,4,5])) #3
print(x.minCost("aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1])) #26