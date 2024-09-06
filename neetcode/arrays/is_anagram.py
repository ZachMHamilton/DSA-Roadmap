class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two approaches
        # 1 - iterate thru and count freqs O(n) - BETTER
        # 2 - sort strings and compare O(n log n)
        # check if lens are not the same
        if len(s) != len(t):
            # return false bc they cant be anagrams
            return False
        # create two dict to store freqs of both strings
        s_freq = {}
        t_freq = {}
        # var to store index
        i = 0
        # iterate thru string len
        for char in s:
            # vars to store char at i
            s_char = s[i]
            t_char = t[i]
            # increment the dicts for each char
            if s_char in s_freq:
                s_freq[s_char] += 1
            else:
                s_freq[s_char] = 1
            if t_char in t_freq:
                t_freq[t_char] += 1
            else: 
                t_freq[t_char] = 1

            i+=1

        # check if the two dicts are equal
        return s_freq == t_freq