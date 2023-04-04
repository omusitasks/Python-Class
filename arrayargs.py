import sys
# import numpy as np

# def arrayargs(a, b, c, d):
#   arr = np.array([a,b,c,d])
#   print(type(arr))
#   print(arr.prod())

# arrayargs(4,5,4,1)

import numpy as np

def arrayargs(a, b, c, d):
  arr = np.array([a,b,c,d])
  print(type(arr))
  print(arr.prod())

if __name__ == '__main__':
    if len(sys.argv) == 5:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
        d = int(sys.argv[4])
        arrayargs(a,b,c,d)