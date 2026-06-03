"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.
File name: TwoSum.py
"""

class Solution:
    def twoSum(nums, target):
        lst=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    lst.append(i)
                    lst.append(j)#
                    return lst

nums = [3,3]
target = 6
res=Solution.twoSum(nums,target)
print(res)
