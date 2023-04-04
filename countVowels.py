
# def countVowels(string):
#     # Create a set containing all the vowels
#     vowels = set('aeiouAEIOU')

#     # Initialize the counter variable
#     count = 0

#     # Iterate through the string and check if each character is a vowel
#     for character in string:
#         if character in vowels:
#             count += 1
#             # Remove the vowel from the set after counting it
#             vowels.remove(character)

#     # Print the result
#     print(count)
# # countVowels('Data') 
# countVowels('bert') 




import sys
def countVowels(string):
    # Create a set containing all the vowels
    vowels = set('aeiou')

    # Initialize the counter variable
    count = 0

    # Iterate through the string and check if each character is a vowel
    for character in string.lower():
        if character in vowels and character != ' ':
            count += 1
            # Remove the vowel from the set after counting it
            vowels.remove(character)

    # Print the result
    print(count)

# Test the function
if __name__ == '__main__':
    if len(sys.argv) > 1:
        txt = sys.argv[1]
        countVowels(txt)
    else:
        print("Please enter a string to count the vowels")