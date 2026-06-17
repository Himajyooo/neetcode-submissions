class Solution:

    def encode(self, strs: List[str]) -> str:
        strr=""
        t=""
        for i in strs:
            strr+=i
            strr+="."
        return(strr)

    def decode(self, s: str) -> List[str]:
        strr=[]
        ss=""
        for i in s:
            if i==".":
                strr.append(ss)
                ss=""
            else:
                ss+=i
        return(strr)
