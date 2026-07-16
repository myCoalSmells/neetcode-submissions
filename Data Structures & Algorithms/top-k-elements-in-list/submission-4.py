from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # max frequency is the size of the array.
        # index can be the frequency
        length = len(nums) + 1
        # first get counts of each
        num_to_count = defaultdict(int)
        for n in nums:
            num_to_count[n] += 1
        
        print(num_to_count)

        frequency_to_numbers = [[] for _ in range(length)]
        
        for num, count in num_to_count.items():
            frequency_to_numbers[count].append(num)
        
        res = []
        for i in range(length-1, -1, -1):
            for j in range(len(frequency_to_numbers[i])-1,-1,-1):
                res.append(frequency_to_numbers[i][j])
                if len(res) == k:
                    return res
        return res


        