class Solution(object):
    def minPartitions(self, n):
        iterations = 0
        valid = True
        no = '23456789'.split()
        # while valid:
        sub = '1' * len(str(n))
        for i in str(n):
            if i in no:
                n -= sub
                pass
            else:
                valid = True
        iterations += 1
        return sub


print(Solution.minPartitions(5, 10000))
