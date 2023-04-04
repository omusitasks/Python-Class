import sys

relations = {'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law', 'R2D2':'droid', 'Rey':'Padawan', 'Tatooine':'homeworld'}

if len(sys.argv) > 1:
    key = sys.argv[1]
    if key == 'Darth Vader':
        print('No, I am your father')
    else:
        print('Luke, I am your', relations[key])
else:
    print('Please provide an argument')