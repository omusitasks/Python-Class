# import numpy as np

# np.random.seed(42)

# def reallyrandom(size, multiplicand, index):
    
#     #Generate random numbers from 0 to 10 of size 'size'
#     numbers = np.random.randint(low=0, high=10, size=size)
    
#     #Multiply the random numbers by the multiplicand
#     multiplied_numbers = numbers * multiplicand
    
#     #Index the multiplied numbers
#     indexed_number = multiplied_numbers[index]
    
#     #Print the indexed number
#     print("Your random value is", indexed_number)
    
# reallyrandom(59, 2, 7)

import sys
import numpy as np

np.random.seed(42)

def reallyrandom(size, multiplicand, index):
    
    #Generate random numbers from 0 to 10 of size 'size'
    numbers = np.random.randint(low=0, high=10, size=size)
    
    #Multiply the random numbers by the multiplicand
    multiplied_numbers = numbers * multiplicand
    
    #Index the multiplied numbers
    indexed_number = multiplied_numbers[index]
    
    #Print the indexed number
    print("Your random value is", indexed_number)
    
if __name__ == '__main__':
    if len(sys.argv) == 4:
        size = int(sys.argv[1])
        multiplicand = int(sys.argv[2])
        index = int(sys.argv[3])
        
        if index < size:
            reallyrandom(size, multiplicand, index)
        else:
            print('Index out of bounds.')
    else:
        print('Invalid number of arguments!')