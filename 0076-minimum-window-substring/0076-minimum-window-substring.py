class Solution:
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        from collections import Counter

        t_count = Counter(t)   # frequency of characters in t
        window = {}

        have = 0
        need = len(t_count)

        left = 0
        res = [-1, -1]
        res_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Check if current char satisfies required frequency
            if char in t_count and window[char] == t_count[char]:
                have += 1

            # Try to shrink window
            while have == need:
                # Update result
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                # Remove left character
                window[s[left]] -= 1
                if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""


# Example usage
obj = Solution()
print(obj.minWindow("ADOBECODEBANC", "ABC"))
        