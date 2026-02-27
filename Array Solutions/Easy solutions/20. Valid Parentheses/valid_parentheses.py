def isValid(s: str) -> bool:
    # Mapping of closing brackets to opening brackets
    bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    stack = []
    
    for char in s:
        if char in bracket_map:  # It's a closing bracket
            # Check if stack is empty or top doesn't match
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:  # It's an opening bracket
            stack.append(char)
    
    # Valid only if stack is empty (all brackets matched)
    return len(stack) == 0


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("((", False),
        ("))", False),
        ("(())", True),
        ("([{}])", True),
        ("([)]", False),
    ]
    
    print("Testing Valid Parentheses Solution:\n")
    for s, expected in test_cases:
        result = isValid(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' | Output: {result} | Expected: {expected}")
