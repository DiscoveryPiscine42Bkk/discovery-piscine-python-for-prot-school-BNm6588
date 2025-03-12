def create_2d_array():
    arr_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return arr_2d
if __name__ == "__main__":
    array = create_2d_array()
    print("Created 2D Array:")
    for row in array:
        print(row)