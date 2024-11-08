class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        max_len = 0
        left = 0

        for right in range(len(s)):
            #Checks if character in most right is in current substring
            while s[right] in char_set:
                #If it is, remove left characters until character is no longer duplicating
                char_set.remove(s[left])
                left += 1
            #Add character from right
            char_set.add(s[right])
            #Compare and change max length
            max_len = max(max_len, right - left + 1)
        
        return max_len