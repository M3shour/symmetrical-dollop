# https://www.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1
from collections import Counter
class Solution:
    def checkEqual(self, a, b) -> bool:
        return Counter(a) == Counter(b)
