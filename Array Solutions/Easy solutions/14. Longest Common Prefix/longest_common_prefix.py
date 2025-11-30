from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    min_len = min(len(s) for s in strs)
    if min_len == 0:
        return ""
    for i in range(min_len):
        c = strs[0][i]
        if any(s[i] != c for s in strs[1:]):
            return strs[0][:i]
    return strs[0][:min_len]

if __name__ == "__main__":
    # quick manual tests
    print(longestCommonPrefix(["flower","flow","flight"]))  # -> "fl"
    print(longestCommonPrefix(["dog","racecar","car"]))    # -> ""