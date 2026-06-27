class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        ml=0
        mf=0
        f={}
        for r in range(len(s)):
            ch=s[r]
            f[ch]=f.get(ch,0)+1
            mf=max(mf,f[ch])

            replacement=(r-l+1)-mf

            if replacement>k:
                lc=s[l]
                f[lc]-=1
                l+=1
            
            ml=max(ml,r-l+1)
        return ml
