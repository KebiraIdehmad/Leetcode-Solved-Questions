# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,arr, N):
        if N == 1:
            return 1
        # Your code here
        directsum=[arr[0]]
        indirectsum=[0]*N
        indirectsum[-1]=arr[-1]
        i = 1
        j = N-2
        while i<N:
            directsum.append(directsum[-1]+arr[i])
            indirectsum[j]=indirectsum[j+1]+arr[j]
            i += 1
            j -= 1
        for i in range(N-1):
            if i+2 <N and directsum[i]==indirectsum[i+2]:
                return i+2
        
        return -1
                
        
            
            
            
        return -1
            



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends