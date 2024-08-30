class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # create dict to store freqs
        dict = {}
        # iterate over nums
        for num in nums:
            if num in dict:
                return True
            else:
                dict[num] = 1
        return False