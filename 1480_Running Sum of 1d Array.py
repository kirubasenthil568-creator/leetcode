class Solution(object):
    def runningSum(self, nums):
        l1=[]
        sum=0
        for i in nums:
            sum+=i
            l1.append(sum)
        return l1



