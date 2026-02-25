class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        out = []
        for idx, i in enumerate(nums):
            if i == target:
                out.append(idx)

        return out