
import sys

# Get the list of words from the command line argument
duplicated_words = sys.argv[1:]

# Create a set to remove duplicate words
non_duplicated_words = set()

# Iterate through the list and add the words to the set
for word in duplicated_words:
    non_duplicated_words.add(word)

# Sort the set in descending order
sorted_words = sorted(non_duplicated_words, reverse=True)

# Print the sorted words
print(sorted_words)