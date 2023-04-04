import sys

set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']

# create a set from set_a
set_a_set = set(set_a)

# create a set from set_b
set_b_set = set(set_b)

# find the common words between set_a and set_b
common_words = set_a_set & set_b_set

# print the output in a set format
print(common_words)