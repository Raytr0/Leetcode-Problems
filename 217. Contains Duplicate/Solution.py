class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        thiset = set()
        for i in nums:
            if i in thiset:
                return True
            else:
                thiset.add(i)
        return False
