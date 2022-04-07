#include<bits/stdc++.h>
using namespace std;
class Solution {
public:
    
    int max_len = 1;
    int start=0,end=0;
    int l,r;
    
    int fun(string s, int l, int r){
        while(l>=0 && r<s.length()){
                if(s[l]==s[r]){
                    l--,r++;
                }else{
                    break;
                }
            }
            
            int len = r-l-1;
            if(max_len < len){
                max_len = len;
                start = l+1;
                end = r-1;
            }
        return 0;
    }
   
    string longestPalindrome(string s) {
        if(s.length()<=1) return s;
        
        for(int i=0;i<s.length()-1;++i){
            int l=i,r=i;
            fun(s,l,r);
        }
        
        for(int i=0;i<s.length()-1;++i){
            int l,r,len;
            l = i;
            r = i+1;
            fun(s,l,r);
        }
        return s.substr(start,max_len);
    }
};