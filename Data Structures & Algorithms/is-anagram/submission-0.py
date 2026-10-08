class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # edge case 1: length isnt the same
        if len(s) != len(t):
            return False
        frequency_s = {} #char : count
        for char in s: #looping thru char in string
            if char in frequency_s: # increase count
                frequency_s[char] += 1
            else: # add to dictionary
                frequency_s[char] = 1
        frequency_t = {} #char : count
        for char in t: #looping thru char in string
            if char in frequency_t: # increase count
                frequency_t[char] += 1
            else: # add to dictionary
                frequency_t[char] = 1
        for char,count in frequency_s.items():
            if char not in frequency_t:
                return False
            if frequency_s[char] != frequency_t[char]:
                return False
        return True