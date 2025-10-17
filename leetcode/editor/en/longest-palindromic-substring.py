from typing import *
from leetcode.editor.common import *


class LongestPalindromicSubstring:
    # leetcode submit region begin(Prohibit modification and deletion)
    class Solution:
        def longestPalindrome(self, s: str) -> str:
            if len(s) < 2:
                        return s
            start = end = 0
            for i in range(len(s)):
                l1 = self._expand(s, i, i)
                l2 = self._expand(s, i, i + 1)
                length = max(l1, l2)
                if length > end - start + 1:
                    start = i - (length - 1) // 2
                    end = i + length // 2
            return s[start:end + 1]
    # leetcode submit region end(Prohibit modification and deletion)
    def _expand(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

if __name__ == '__main__':
    solution = LongestPalindromicSubstring().Solution()
