# Valid Parentheses - Solution Approach

## Problem Statement
Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

## Approach: Stack-Based Solution

### How It Works
The key insight is to use a **stack** data structure to match brackets:

1. **Iterate through each character** in the string
2. **If it's an opening bracket** ('(', '{', '['): Push it onto the stack
3. **If it's a closing bracket** (')', '}', ']'): 
   - Check if the stack is empty → Invalid (no matching opening bracket)
   - Check if the top of the stack matches the closing bracket type → Pop from stack
   - If no match → Invalid (mismatched brackets or wrong order)
4. **After iterating**: Check if the stack is empty
   - Empty stack = Valid (all brackets matched)
   - Non-empty stack = Invalid (unclosed opening brackets)

### Why This Works
- **Correct Order**: Stack naturally enforces LIFO (Last In, First Out), which ensures proper nesting order
- **Matching Pairs**: By comparing the closing bracket with the top of the stack, we verify correct pairing
- **Complete Matching**: An empty stack at the end guarantees all brackets are matched

### Example Walkthrough
For input `"([)]"` (invalid - wrong order):
```
Char: '(' → Push '(' | Stack: ['(']
Char: '[' → Push '[' | Stack: ['(', '[']
Char: ')' → Top is '[', expected '(' → INVALID ✗
```

For input `"([{}])"` (valid):
```
Char: '(' → Push '(' | Stack: ['(']
Char: '[' → Push '[' | Stack: ['(', '[']
Char: '{' → Push '{' | Stack: ['(', '[', '{']
Char: '}' → Top is '{', matches → Pop | Stack: ['(', '[']
Char: ']' → Top is '[', matches → Pop | Stack: ['(']
Char: ')' → Top is '(', matches → Pop | Stack: []
Result: Stack empty → VALID ✓
```

## Complexity Analysis
- **Time Complexity**: O(n) - Single pass through the string, each character processed once
- **Space Complexity**: O(n) - Stack can contain up to n/2 opening brackets in worst case

## Code Structure
```python
def isValid(s: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for char in s:
        if char in bracket_map:  # Closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)
    
    return len(stack) == 0
```

## Key Points
- ✓ Simple and efficient
- ✓ Clear and readable logic
- ✓ Handles all edge cases (empty string, single bracket, etc.)
- ✓ No extra string operations, just character comparison
