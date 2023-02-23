class Solution:
    def fib(self, n: int) -> int:
        dic = {0:0, 1:1}
        if n <2 : return n
        if n in dic : return dic[n]
        result = self.fib(n-1) + self.fib(n-2)
        dic[n]=result
        return result