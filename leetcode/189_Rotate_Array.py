from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        r = k%len(nums)
        new = nums[0:n-r]
        nums[0:n-r] = []
        nums.extend(new)
if __name__ == '__main__':
    solution = Solution()
    nums = [-1,-100,3,99]
    k = 2
    solution.rotate(nums,2)
    print(nums)