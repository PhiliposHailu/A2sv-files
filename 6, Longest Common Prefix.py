class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        
        for i in range(len(strs[0])):
            for p in strs:
                if i == len(p) or p[i] != strs[0][i]:
                    return common
                
            common += strs[0][i]
        return common
        
