from heapq import heapify, heappop, heappush

class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_backlog = []
        sell_backlog = []
        heapify(buy_backlog)
        heapify(sell_backlog)

        heappush_buy = lambda k: heappush(buy_backlog, [-k[0], k[1]])
        heappeak_buy = lambda: [-buy_backlog[0][0], buy_backlog[0][1]]


        for price, amount, orderType in orders:
            if orderType == 0:                
                while len(sell_backlog)!=0 and sell_backlog[0][0]<=price and amount!=0:
                    if sell_backlog[0][1]<amount:
                        amount-=sell_backlog[0][1]
                        heappop(sell_backlog)
                    else:
                        sell_backlog[0][1]-=amount
                        amount=0
                if amount!=0:
                    heappush_buy([price, amount])
            
            if orderType == 1:
                while len(buy_backlog)!=0 and heappeak_buy()[0]>=price and amount!=0:
                    if heappeak_buy()[1]<amount:
                        amount-=heappeak_buy()[1]
                        heappop(buy_backlog)

                    else:
                        buy_backlog[0][1]-=amount
                        amount=0
                if amount!=0:
                    heappush(sell_backlog, [price, amount])
        return  ( sum([i for _, i in buy_backlog]) + sum([i for _, i in sell_backlog]) ) % ( (10**9) + 7 )
