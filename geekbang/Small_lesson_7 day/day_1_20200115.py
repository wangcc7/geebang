# -*- coding: utf-8 -*-
# by wangcc
# mail:wangcc_sd@163.com

#算法第一天
class Solution:
    def removeDuplicates(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        return j+1

if __name__ == '__main__':
    S1 = Solution()
    a = S1.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(a)