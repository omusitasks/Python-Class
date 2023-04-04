import sys

def counter(s): 
  dic = {}
  
  for i in s: 
    if i not in dic: 
      dic[i] = 1
    else: 
      dic[i] += 1
      
  print(dic)

# Test the function
if __name__ == '__main__':
    if len(sys.argv) > 1:
        n = sys.argv[1]
        counter(n)
    else:
        print("Please enter a number")