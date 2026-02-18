# https://www.geeksforgeeks.org/problems/array-subset-of-another-array2317/1
from collections import Counter
class Solution:
    def isSubset(self, a, b):
        return Counter(a) & Counter(b) == Counter(b)
