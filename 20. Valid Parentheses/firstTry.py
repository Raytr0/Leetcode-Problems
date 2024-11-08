"""
This didn't work because the brackets need to close, case ([)] isn't accepted even though both are closed, thats what the in order means
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictonary = {}
        for i in s:
            dictonary[i] = dictonary.get(i,0)+1
        if dictonary.get("(") != dictonary.get("(") or dictonary.get("[") != dictonary.get("]") or dictonary.get("{") != dictonary.get("}"):
            return False
        else:
            return True
        