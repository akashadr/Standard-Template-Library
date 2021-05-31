if __name__=="__main__":
  
  X,Y=map(str,input().split(','))
  X,Y=X.strip(),Y.strip()
  
  Sum=0
  
  for i in range(len(X)):
    Sum+=(int(Y[i])-int(X[i]))
  
  print(Sum)