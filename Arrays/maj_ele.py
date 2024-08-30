class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # create a dict to store nums and freqs
        freq_dict = {}
        # create an arr to store current maj
        curr_maj = [0, 0]
        # iterate thru the nums
        for num in nums:
            # if the num already exists in dict
            if num in freq_dict:
                # increment freq
                freq_dict[num] += 1
                # if freq is greater than current maj freq
                if freq_dict[num] >= curr_maj[1]:
                    # update current maj
                    curr_maj[0] = num
                    curr_maj[1] = freq_dict[num]
            # otherwise add it with freq of 1
            else:
                freq_dict[num] = 1
        # return current maj
        return curr_maj[0]