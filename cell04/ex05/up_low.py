def swap_case(input_string):
    return input_string.swapcase()

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print("Modified string:", swap_case(user_input))