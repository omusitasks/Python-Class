
# def capCount(s): 
#   count = 0
#   indices = 0
  
#   for i in s: 
#     if i.isupper(): 
#       count += 1
#       indices += ord(i) - ord('A') + 1
      
#   print(count)
#   print(indices)
  
# capCount('Hello')



# import sys

# def capCount(s): 
#   count = 0
#   indices = 0
  
#   for i in s: 
#     if i.isupper(): 
#       count += 1
#       indices += ord(i) - ord('A') + 1
      
#   print(count)
#   print(indices)

# # Test the function
# if __name__ == '__main__':
#     if len(sys.argv) > 1:
#         s = sys.argv[1]
#         capCount(s)
#     else:
#         print("Please enter a string to count the indices")


import sys

def capCount(string):
  # Initialize a counter to 0
  count = 0
  # Initialize sum to 0
  sum = 0

  # Iterate through each character in the string
  for i in range(len(string)):
    # Check if character is an uppercase letter
    if string[i].isupper():
      # Increase count by 1
      count += 1
      # Increase sum by index of character
      sum += i
  
  # Print the count and sum
  print(count)
  print(sum)

# Test the function
if __name__ == '__main__':
    if len(sys.argv) > 1:
        txt = sys.argv[1]
        capCount(txt)
    else:
        print("Please enter a string")