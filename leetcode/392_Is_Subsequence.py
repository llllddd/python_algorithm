class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        i = 0
        j = 0
        while i < m and j < n:
            if t[j] != s[i]:
                j+=1
            else:
                j +=1
                i +=1
        if i == m:
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    s = ""
    t = "SDFSFS"
    r=solution.isSubsequence(s,t)
    print(r)