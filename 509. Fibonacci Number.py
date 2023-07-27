class Solution:
    def fib(self, n: int) -> int:
        if n in map_fib:
            return map_fib[n]
        
        val=self.fib(n-1)+self.fib(n-2)
        map_fib[n]=val
        return val       

map_fib={
    0:0,
    1:1
}