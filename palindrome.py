# def is_palindrome(text): 
#   clean_text = ''.join(c for c in text if c.isalnum())
#   clean_text_rev = clean_text[::-1]
  
#   if clean_text == clean_text_rev:
#     print("It's a palindrome!")
#   else:
#     print("It’s not a palindrome! ")

# # is_palindrome('This is DTSC-575') 
# is_palindrome('racecar') 


import sys

def is_palindrome(text): 
  clean_text = ''.join(c for c in text.lower() if c.isalnum())
  clean_text_rev = clean_text[::-1]
  
  if clean_text == clean_text_rev:
    print("It's a palindrome!")
  else:
    print("It's not a palindrome! ")

# Test the function
if __name__ == '__main__':
    if len(sys.argv) > 1:
        txt = sys.argv[1]
        is_palindrome(txt)
    else:
        print("Please enter a string to check if it is a palindrome")