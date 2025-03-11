class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0  # i for s, j for t
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move `i`
                i += 1
            j += 1  # Always move `j`
        return i == len(s)