class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i=0
        min_length=float('inf')
        for s in strs:
            if len(s)<min_length:

                min_length=len(s)
        while i<min_length:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return s[:i]

            i+=1

        return s[:i]
