import sys

subject = ''

if len(sys.argv) > 1:
  subject = sys.argv[1]

grades = {'Biology':80, 'Physics':88, 'Chemistry':98, 'Math':89, 'English':79, 'Music':67, 'History':68, 'Art':53, 'Economics':95, 'Psychology':88}

total = 0

for key in grades:
  if key != subject:
    total += grades[key]

average = total/9

print(f"{average:.2f}")