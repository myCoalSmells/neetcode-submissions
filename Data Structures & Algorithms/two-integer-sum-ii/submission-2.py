class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            left_val = numbers[l]
            right_val = numbers[r]
            curr_sum = left_val + right_val

            if curr_sum == target:
                return [l+1, r+1]
            if curr_sum < target:
                l += 1
            else:
                r -= 1
        return []