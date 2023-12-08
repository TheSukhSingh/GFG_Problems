class Solution:
    def checkDistinct(self, A):
        if len(set(A)) == len(A):
            return "Distinct"
        else:
            return "Not Distinct"