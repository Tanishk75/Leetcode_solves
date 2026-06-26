class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        prefic=strs[0]

        for i in strs[1:]:
            while not i.startswith(prefic):
                prefic=prefic[:-1]
            if prefic=="":
                break
        
        return prefic