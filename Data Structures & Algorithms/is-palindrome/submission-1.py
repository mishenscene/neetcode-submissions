class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = [c.lower() for c in s]
        l,r=0,len(new)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while r>l and not s[r].isalnum():
                r-=1
            if new[l] != new[r]:
                return False
            l+=1
            r-=1
        return True