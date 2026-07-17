class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set(nums)
        res = 1
        for left_edge in nums:
            if left_edge-1 in nums:
                continue
            right_edge = left_edge + 1
            window = 1
            while right_edge in nums:
                window += 1
                right_edge += 1
            res = max(window, res)
        return res
                
