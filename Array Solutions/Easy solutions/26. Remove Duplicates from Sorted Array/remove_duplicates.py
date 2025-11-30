from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        prev = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur != prev:
                nums[write] = cur
                write += 1
                prev = cur
        return write
    
if __name__ == "__main__":
    # quick manual tests
    print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))  # -> 5
 
