class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
      #Preprocess s store the char->index[char]
        charToIndexes = [[] for _ in range(26)]
        for i in range(len(s)):
            c = s[i]
            if not charToIndexes[ord(c)-ord('a')]:
                charToIndexes[ord(c)-ord('a')] = []
            charToIndexes[ord(c)-ord('a')].append(i)
        res = 0
        for word in words:
            i = 0
            j = 0
            while i < len(word):
                c = word[i]
                if not charToIndexes[ord(c) - ord('a')]:
                    break
                pos = self.left_bound(charToIndexes[ord(c)-ord('a')],j)
                if pos == len(charToIndexes[ord(c)-ord('a')]):
                    break
                j=charToIndexes[ord(c) - ord('a')][pos]
                j+=1
                i+=1
                if i == len(word):
                    res+=1
        return res
    def left_bound(self, arr:List[int], target:int)->int:
        left,right = 0, len(arr)-1
        while left<= right:
            mid = left + (right-left)//2
            if arr[mid] >= target:
                right = mid -1
            elif arr[mid] < target:
                left = mid +1
            return left
    def _numMatchingSubseq(self, s: str, words: List[str]) -> int:
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
    s = "abcde"
    word = ['a','bb','acd','ace']
    r = solution.numMatchingSubseq(s, word)
    print(r)