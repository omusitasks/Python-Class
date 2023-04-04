import sys 

def shortest(string):
    words = string.split(" ")
    shortest_word = min(words, key=len)
    print("The shortest word is " + shortest_word.upper())

# Test the function
if __name__ == '__main__':
    if len(sys.argv) > 1:
        txt = sys.argv[1]
        shortest(txt)
    else:
        print("Please enter a string to find the shortest")