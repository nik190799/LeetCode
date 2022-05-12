class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        
        for i in range(1,len(intervals)):
            start_1, end_1 = intervals[i-1]
            start_2, end_2 = intervals[i]
            
            if end_1 > start_2: return False
        
        return True