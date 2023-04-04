import sys

set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']

diff_set = set(set_a).difference(set_b)

print(diff_set)