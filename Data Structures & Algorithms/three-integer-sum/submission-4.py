class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, v in enumerate(nums):
            if v > 0:
                break # the minimum already > 0
            if i > 0 and v == nums[i -1]:
                continue #skip the same element, we are only listing all unique answers
            left, right = i + 1, len(nums) - 1
            while left < right:
                threesum = v + nums[left] + nums[right]
                if threesum > 0:
                    right -= 1
                elif threesum < 0:
                    left += 1
                else:
                    res.append([v, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    while nums[right] == nums[right + 1] and right > left:
                        right -= 1
        return res
