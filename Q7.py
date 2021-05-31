def longestSubSeg(a, n, k):
 

    count = 0

    start = 0

    max_len = 0;
 

    for end in range(0, n):

        if a[end] == 0:

            count += 1
 
        while (count > k):

            if a[start] == 0:

                count -= 1

            start += 1

        max_len = max(max_len, end - start + 1);

    return max_len
    

if __name__=="__main__":
  
  a = [1, 1, 0, 0, 0, 1, 1, 1, 1 ]

  k = 2

  n = len(a)

  print(longestSubSeg(a, n, k))