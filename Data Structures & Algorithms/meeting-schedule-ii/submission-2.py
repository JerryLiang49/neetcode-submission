"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start.sort()
        end.sort()

        count = 0
        s = e = 0
        for s in range(len(intervals)):
            if start[s] < end[e]:
                count += 1
            else:
                e += 1

        return count
