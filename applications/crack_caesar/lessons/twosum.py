class Solution(object):
    def twoSum(self, nums, target):

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_mapping = []

        # go through the nums
        # access to that number
        # target - number
        # if complement is in dictionary
            # return the indicies
        # put number in the dictionary

        for i in range(len(num)):
            curr = nums[i]
            complement = target - curr
            if complement in index_mapping:
                return [index_mapping[complement], i]
            else:
                index_mapping[curr] = i