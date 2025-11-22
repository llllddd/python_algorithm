class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cnt = 0
        wordmap = {}
        for word in words:
            if wordmap.get(word) == 1:
                cnt +=1
            elif self.isSubsequnce(word,s): 
                cnt +=1
                wordmap[word] =1
        return cnt

    def isSubsequnce(self,s:str,t:str)->bool:
        m = len(s)
        n = len(t)
        i = 0
        j = 0
        while i<len(s) and j<len(t):
            if s[i] == t[j]:
                i+=1
            j+=1
        return i==m

if __name__ == '__main__':
    solution = Solution()
    s = "sd"
    word = ['s','d']
    r = solution.numMatchingSubseq(s, word)
    print(r)