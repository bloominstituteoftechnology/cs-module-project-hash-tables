# """
# Understand: 
# 1. J = "aA", S = "aAAbbbb" 
# Output: 3

# 2. J = "z", S = "ZZ"
# Output: 0

# 3. J = "z", S = ""
# Output: 0

# Plan:
# brute-force: for each char s in S, see if it is in J
# if it is, then increment result else do not increment it

# better approach: convert J into a set 
# for each char s in S 
#     if s is in j then incremtnt result
#     return result
# """

# class Solution:
#     # J = "aA", S = "aAAbbbb"
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         j = set(list(J)) # set(a, A)
#         numJewels = 0 # 0

#         for s in S: "a"
#             if s in j:
#                  numJewels += 1
#         return numJewels