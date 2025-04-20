class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets=set()
        nums=sorted(nums)

        for left in range(len(nums)-1):
            occurred=set()

            for right in range(left+1, len(nums)):

                remainder=-nums[left]-nums[right]
                
                if remainder in occurred:
                    new_triplet=(nums[left], remainder, nums[right])
                    triplets.add(new_triplet)
                else:
                    occurred.add(nums[right])

        return list([list(i) for i in triplets])
