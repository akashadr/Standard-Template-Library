def ReplacePattern(words, pattern):
    words_num = []
    result = []
    for i in words:
       words_num.append(convert(i))
    pattern = convert(pattern)
    for i in range(len(words)):
       if words_num[i] == pattern:
          result.append(words[i])
    return result

def convert(word):
    counter = 1
    s = str(1)
    for i in range(1,len(word)):
       j= i -1
       while j>=0:
         if word[i] == word[j]:
             break
         j-=1
       if j >-1:
          s+=s[j]
       else:
          counter+=1
          s+=str(counter)
    return s

if __name__=="__main__":
  
  Words=["abc","deq","mee","aqq","dkd","ccc"]
  
  Pattern="abb"

  print(ReplacePattern(Words,Pattern))