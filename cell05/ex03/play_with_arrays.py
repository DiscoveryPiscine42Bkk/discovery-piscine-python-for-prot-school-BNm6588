# play_with_arrays.py

# Define the original array of numbers
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Create a new array by adding 2 to each value in the original array
new_array = [x + 2 for x in original_array]

# Display both arrays, ensuring duplicates are not shown in the output without altering the arrays
print("Original array:", original_array)
print("New array:", list(dict.fromkeys(new_array)))