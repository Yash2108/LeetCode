class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output=[]
        intervals=sorted(intervals, key = lambda x:x[0])
        while intervals:
            current = intervals.pop(0)
            if intervals and current[1]>=intervals[0][0]:
                intervals[0][0] = min(current[0], intervals[0][0])
                intervals[0][1] = max(current[1], intervals[0][1])
            else:
                output.append(current)
        return output
