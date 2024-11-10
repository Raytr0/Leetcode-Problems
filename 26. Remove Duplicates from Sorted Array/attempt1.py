class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = "_"
        print(nums.sort())

#got stuck because I couldn't figure out how to filter out the "_"
