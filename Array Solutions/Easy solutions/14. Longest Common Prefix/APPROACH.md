**Explanation:**
- Compute min_len = length of the shortest string (no need to check past that).
- For each index i from 0 to min_len-1:
    - Take c = strs[0][i].
    - Use any(s[i] != c for s in strs[1:]) to check if any other string differs at i.
    - If a mismatch is found, return strs[0][:i] (prefix up to but not including i).
- If no mismatch found, return the entire first string up to min_len.

**Complexity:**

- Let n = number of strings, L = length of the shortest string.
- Time (worst-case): O(n * L) — for each of L positions you may check up to n strings.
- Time (best-case): O(n) — mismatch at first character requires one pass over the n strings.
- Space: O(1) extra (returned prefix slice is O(k) where k is prefix length).
