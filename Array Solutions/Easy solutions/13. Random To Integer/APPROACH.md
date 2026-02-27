# Roman to Integer - Approach

## Problem Statement
Given a Roman numeral string, convert it to an integer.

## Solution Approach

### Method: Left-to-Right Pass with Subtractive Case Handling
**Time Complexity:** O(n) where n is the length of the string  
**Space Complexity:** O(1) - only using a fixed-size dictionary

### Algorithm
1. Create a mapping of Roman numerals to their integer values
2. Iterate through the string from left to right
3. For each character:
   - Check if the current value is less than the next value (subtractive case)
   - If yes, subtract current from next and skip both characters
   - If no, add the current value to the total
4. Return the total

### Key Insight
The subtractive principle only applies when a smaller value appears before a larger value. By checking this condition, we can handle all subtractive cases (IV=4, IX=9, XL=40, XC=90, CD=400, CM=900) in one pass.

### Code
```python
def romanToInt(self, s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    i = 0
    
    while i < len(s):
        if i + 1 < len(s) and roman_values[s[i]] < roman_values[s[i + 1]]:
            total += roman_values[s[i + 1]] - roman_values[s[i]]
            i += 2
        else:
            total += roman_values[s[i]]
            i += 1
    
    return total
```

## Example Walkthroughs

**Example 1:** s = "III"
- i=0: 'I'(1) >= next not less, add 1, total=1, i=1
- i=1: 'I'(1) >= next not less, add 1, total=2, i=2
- i=2: 'I'(1), add 1, total=3, i=3
- Result: 3 ✓

**Example 2:** s = "IV"
- i=0: 'I'(1) < 'V'(5), add 5-1=4, total=4, i=2
- Result: 4 ✓

**Example 3:** s = "XII"
- i=0: 'X'(10), add 10, total=10, i=1
- i=1: 'I'(1) < 'I'(1)? No, add 1, total=11, i=2
- i=2: 'I'(1), add 1, total=12, i=3
- Result: 12 ✓

**Example 4:** s = "XXVII"
- i=0: 'X'(10), add 10, total=10, i=1
- i=1: 'X'(10), add 10, total=20, i=2
- i=2: 'V'(5), add 5, total=25, i=3
- i=3: 'I'(1), add 1, total=26, i=4
- i=4: 'I'(1), add 1, total=27, i=5
- Result: 27 ✓

**Example 5:** s = "MCMXCIV" (1994)
- i=0: 'M'(1000), add 1000, total=1000, i=1
- i=1: 'C'(100) < 'M'(1000), add 1000-100=900, total=1900, i=3
- i=3: 'X'(10) < 'C'(100), add 100-10=90, total=1990, i=5
- i=5: 'I'(1) < 'V'(5), add 5-1=4, total=1994, i=7
- Result: 1994 ✓

## Advantages
- Single pass through the string - O(n) time
- Handles all subtractive cases elegantly
- Minimal space usage
- Clean and readable logic

## Edge Cases Handled
- Single characters (I, V, X, L, C, D, M)
- All subtractive combinations (IV, IX, XL, XC, CD, CM)
- Multiple consecutive same characters (III, XXX, etc.)
- Large Roman numerals (MMMCMXCIX = 3999)
