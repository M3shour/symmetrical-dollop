# https://www.geeksforgeeks.org/problems/union-of-two-arrays3538/1
class Solution:    
    def findUnion(self, a, b):
        a, b = set(a), set(b)
        return a | b
