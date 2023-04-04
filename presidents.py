import pandas as pd
import sys

# Read the president_heights.csv file 
data = pd.read_csv('president_heights.csv')

# Get the start and end index of the slice 
if len(sys.argv) < 3:
    start, end = 0, len(data)
else: 
    start, end = int(sys.argv[1]), int(sys.argv[2])

# Calculate the average height of slice
slice_avg = round(data['height(cm)'][start:end].mean(),2)

# Print the result 
print("The average height of presidents number {} to {} is {}".format(start, end, slice_avg))