class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output=[]
        seen={}
        for i in strs:
            s="".join(sorted(i))
            if s not in seen:
                seen[s]=[]
            seen[s].append(i)
        for i in seen:
            output.append(seen[i])
        return output
            
        