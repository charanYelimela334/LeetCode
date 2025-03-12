from collections import Counter
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = Counter(arr)
        occurrences = list(c.values())  # Get the frequency of each element
        return len(occurrences) == len(set(occurrences))