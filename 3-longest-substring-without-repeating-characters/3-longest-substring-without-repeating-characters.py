class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        max_c = 0
        count = 0
        l= 0
        while l<len(s):
            if s[l] not in m:
                m[s[l]] = l
                l += 1
                count += 1
                max_c = max(max_c,count)
            else:
                l = m[s[l]] + 1
                max_c = max(max_c,count)
                count = 0
                m = {}
                
        return max_c