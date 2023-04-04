import sys

loop_list = sys.argv[1:]

result = []

for i in range(len(loop_list)):
    result.append(int(loop_list[i]) + i)

print(result)