class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        newnums=sorted(set(nums))
        max=1
        c=1
        for i in range(len(newnums)-1):
            if newnums[i]+1==newnums[i+1]:
                c+=1
                if c>max:
                    max=c
            else:
                c=1
        return max