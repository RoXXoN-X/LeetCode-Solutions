from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num  # Calculate the number needed to reach target
            if complement in num_map:  # Check if we've seen this number before
                return [num_map[complement], i]  # Return stored index + current index
            num_map[num] = i  # Store current number's index for future checks

if __name__ == "__main__":
    # example usage — modify inputs as needed
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))
