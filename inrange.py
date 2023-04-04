# def inrange(num):
#     result = []
#     for i in range(3000,5001):
#         if (i % num == 0) and (i % (num + 7) == 0) and (i % (num ** 2) == 0):
#             result.append(i)
#     return result

# print(inrange(6))

import sys

def countVowels(string):
    # Create a set containing all the vowels
    vowels = set('aeiouAEIOU')

    # Initialize the counter variable
    count = 0

    # Iterate through the string and check if each character is a vowel
    for character in string:
        if character in vowels:
            count += 1
            # Remove the vowel from the set after counting it
            vowels.discard(character)

    # Print the result
    print(count)

# Test the function
if __name__ == '__main__':
    if len(sys.argv) > 1:
        txt = sys.argv[1]
        countVowels(txt)
    else:
        print("Please enter a string to count the vowels")
