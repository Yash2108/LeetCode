class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        [s1,e1] [s2,e2]

        s1<s2<e1

        s1==s2, pick max(e1, e2)
        s2==e1, (s1, e2)

        '''

        intervals=sorted(intervals)
        
        result=[intervals[0]]

        for s2, e2 in intervals[1:]:
            s1, e1 = result[-1]

            # if s1==s2:
            #     result[-1] = [s1, max(e1, e2)]
            #     continue
            if s1<=s2<=e1:
                result[-1] = [s1, max(e1, e2)]
                continue
            result.append([s2, e2])
        return result