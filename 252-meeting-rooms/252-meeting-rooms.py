class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        maximum = 0
        minimum = 10000000
        for i in range(len(intervals)):
            maximum = max(int(intervals[i][0]),maximum)
            minimum = min(int(intervals[i][0]),minimum)
            
            maximum = max(int(intervals[i][1]),maximum)
            minimum = min(int(intervals[i][1]),minimum)
        
        arr = [0]*((2*maximum)-minimum+1)
        
        
        for i in range(len(intervals)):
            arr[intervals[i][0]] = 0
            arr[intervals[i][1]] = 0
            for j in range(intervals[i][0],intervals[i][1]+1):
                if arr[j] == 0:
                    arr[j] = 1
                else:
                    return False
        
        return True