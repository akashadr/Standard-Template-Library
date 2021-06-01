def fib(N):          #T=O(2^N)
    if N <= 1:

        return N

    return fib(N-1) + fib(N-2)

def DP(N):           #T=O(N)
    steps = [0]*N
    steps[0] = 1
    steps[1] = 1
    for i in range(2,N):
        steps[i] = steps[i-1] + steps[i-2]
    
    return steps[N-1]

if __name__=="__main__":
  
  s = int(input())
  
  if(s==0): print(0)

  else: print(DP(s+1))