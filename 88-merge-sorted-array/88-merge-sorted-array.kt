class Solution {
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int): Unit {
        var i = m-1
        var j = n-1
        var t = m+n-1
        while(t>=0){
            print("$i   $j\n")
            if(i>=0 && j>=0){
                if(nums1[i]>nums2[j]){
                    nums1[t] = nums1[i]
                    i--
                }else{
                    nums1[t] = nums2[j]
                    j--
                }
            }else{
                if(i>=0){
                    if(j<0){
                        nums1[t] = nums1[i]
                    }
                    else if(nums1[i]>nums2[j]){
                        nums1[t] = nums1[i]
                    }
                    i--
                }
                if(j>=0){
                    if(i<0){
                        nums1[t] = nums2[j]
                    }
                    else if(nums1[i]<=nums2[j]){
                        nums1[t] = nums2[j]
                    }
                    j--
                }
            }
            
            t--
        }
    }
}