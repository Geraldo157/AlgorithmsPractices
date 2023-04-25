class Solution(object):
    def shuffle(self, nums, n):
        a1 = nums[0:n]
        a2 = nums[n::]
        res = []
        for i in range(2*n):
            if i % 2 == 0:
                res.append(a1[i/2])
            else:
                res.append(a2[i/2])
        return res
