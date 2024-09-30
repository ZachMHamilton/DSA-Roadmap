import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove spaces and special characters
        str = re.sub('[^A-Za-z0-9]+', '', s).lower()
        # two pointers, start and end
        start = 0
        end = len(str) - 1
        # iterate while start is less than end
        while start < end:
            # if the letters at those two positions are not the same then return false
            if str[start] != str[end]:
                return False
            start += 1
            end -= 1
        # otherwise return true after iterating thru all letters
        return True