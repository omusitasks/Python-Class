import sys

duck_goose = sys.argv[1:]

remaining_list = [word for word in duck_goose if word != 'goose']

print(remaining_list)