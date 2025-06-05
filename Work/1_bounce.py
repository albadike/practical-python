# 1_bounce.py
#
# Exercise 1.5

height = 100  # initial height in meters
bounce_factor = 3/5  # bounce factor
count = 1

while count <= 10:
    height *= bounce_factor
    print(f"After bounce {count}, height: {round(height, 4)} meters.")
    count += 1
