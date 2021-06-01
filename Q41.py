if __name__=="__main__":
  
  L = list(map(int,input().split(',')))
  S = set(L)
  
  for i in S:
    X=L.count(i)
    print(f"Count of {i} = {X}")