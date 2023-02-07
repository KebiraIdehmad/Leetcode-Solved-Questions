#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        ones = 0
        zeros = 0
       
        for i in range(n):
            if arr[i]==0:
                zeros += 1
            if arr[i]==1:
                ones += 1
        
        for i in range(n):
            if i<zeros:
                arr[i]=0
            elif i>=zeros and i<zeros+ones:
                arr[i]=1
            else:
                arr[i]=2
        return arr



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends