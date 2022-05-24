class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        occupied = list()

        intervals.sort()

        heappush(occupied, [intervals[0][1], intervals[0][0]])
        rooms = 1

        for i in range(1, len(intervals)):
            if occupied[0][0] > intervals[i][0]:
                rooms += 1
            else:
                heappop(occupied)

            heappush(occupied, [intervals[i][1], intervals[i][0]])

        return rooms