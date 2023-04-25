class Solution(object):
    def maximumWealth(self, accounts):
        rich = 0
        for i in accounts:
            soma = sum(i)
            if soma > rich: rich = soma
        return rich
