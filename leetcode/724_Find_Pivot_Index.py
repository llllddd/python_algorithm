from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        #1. Calculate sumleft and save them to an array
        #2. Calculate sumright and save them to another array
        #3. Find the index such that sumleft[i] = sumright[i]
        sumleft = [0]
        sumright = []
        for i in range(1,len(nums)):
            sumleft.append(sum(nums[0:i]))
        for i in range(len(nums)-1):
            sumright.append(sum(nums[i+1:len(nums)]))
        sumright.append(0)
        for i in range(len(sumleft)):
            if sumleft[i] == sumright[i]:
                return i
        return -1
if __name__ == '__main__':
    solution = Solution()
    nums = [2,1,-1]
    re= solution.pivotIndex(nums)
    print(re)