class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        prefic=""
        sl=min(len(w)for w in  strs)
        for i in range(sl):
            ch=strs[0][i]
            if all(word[i]==ch for word in strs):
                prefic+=ch
            else:
                break
        
        return prefic