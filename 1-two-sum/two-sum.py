class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        parsed_nums = {}

        for idx, num in enumerate(nums):
            if target-num not in parsed_nums:
                if num in parsed_nums:
                    parsed_nums[num].append(idx)
                parsed_nums[num] = [idx]
            else:
                return [idx, parsed_nums[target-num][0]]