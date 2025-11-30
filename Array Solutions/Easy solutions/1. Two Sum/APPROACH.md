Here's the optimal solution for the Two Sum problem:

```python
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
```

**Explanation:**
- Uses a hash map (dictionary) to store numbers and their indices as we iterate
- For each number, checks if its complement (target - current number) exists in the map
- Returns the indices immediately when a match is found (guaranteed to have exactly one solution)
- Time complexity: O(n) (single pass through the array)
- Space complexity: O(n) (worst-case storage for all elements)

This approach efficiently finds the solution in linear time while adhering to the constraint of not using the same element twice.

The line `for i, num in enumerate(nums)` uses Python's `enumerate()` function to iterate through the list `nums` while tracking both the **index (`i`)** and **value (`num`)** of each element.

**How it works:**
- `enumerate(nums)` converts the list into an iterable of `(index, value)` tuples.
- `i, num = ...` unpacks each tuple into variables:
  - `i` = current index (e.g., `0`, `1`, `2`, ...)
  - `num` = current number (e.g., `2`, `7`, `11`, ...)

**Why it's used here:**
- We need to store each number's **index** in the dictionary (`num_map`).
- We also need the **current index** (`i`) to return when a solution is found.
- Without `enumerate`, we'd have to manually track the index (e.g., `for i in range(len(nums))`), which is less clean.

**Example:**
For `nums = [2, 7, 11, 15]`:
- First iteration: `i = 0`, `num = 2`
- Second iteration: `i = 1`, `num = 7`  
*(and so on)*