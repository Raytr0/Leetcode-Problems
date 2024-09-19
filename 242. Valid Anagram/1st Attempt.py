class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        thisset = set()
        if len(s) != len(t):
            return False
        for i in s:
            thisset.add(i)
        for j in t:
            if j in thisset:
                thisset.remove(j)
        return len(thisset) == 0
#Turns out lists cant contain duplicate characters! I am stupid