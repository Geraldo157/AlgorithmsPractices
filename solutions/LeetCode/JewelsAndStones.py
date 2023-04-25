class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        valid = 0
        for i in stones:
            if i in jewels: valid +=1

        return valid
