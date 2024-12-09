class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[[]]

        for n in nums:
            perms=[]
            for perm in output:
                for i in range(len(perm)+1):
                    perm_copy=perm.copy()
                    perm_copy.insert(i, n)
                    perms.append(perm_copy)
            output=perms
        return output