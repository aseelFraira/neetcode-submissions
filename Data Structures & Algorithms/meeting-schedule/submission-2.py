"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        stack = []
        
        for interval in sorted_intervals:
            if stack and interval.start < stack[-1].end:
                return False
            else:
                stack.append(interval) 
        return True
            
