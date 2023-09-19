class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        visits={i:0 for i in range(1,n+1)}
        visits[rounds[0]]=1
        
        for i in range(1, len(rounds)):
            if rounds[i-1]<rounds[i]:
                for j in range(rounds[i-1]+1, rounds[i]+1):
                    visits[j]+=1
            else:
                for j in range(rounds[i-1]+1, n+1):
                    visits[j]+=1
                for j in range(1, rounds[i]+1):
                    visits[j]+=1

        ls = sorted(visits.items(), key=lambda k: k[1], reverse=True)
        return [i[0] for i in ls if i[1]==ls[0][1]]