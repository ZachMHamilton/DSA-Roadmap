from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # first step is to find all of the anagrams
            # iterate thru each string and count the freq
        # sort them into groups 
        # dict to store the sorted anagram as they key and the words as values
        # build new dicts of the values as sub arrays in the output

        # create dict to store anagrams and their words
        anagrams = {}
        # iterate thru the list of strs
        for str in strs:
            # sort the str
            sorted_str = ''.join(sorted(str))
            # check if the sorted str exists in our dict
            if sorted_str in anagrams:
                # add the unsorted string as a value 
                anagrams[sorted_str].append(str)
            # otherwise we add the sorted str as a key with the unsorted as value
            else:
                anagrams[sorted_str] = [str]
        # return array containing the values of the dict
        return anagrams.values()