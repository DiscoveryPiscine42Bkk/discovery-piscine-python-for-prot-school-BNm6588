def add_one(number):
    return number + 1
def main():
    my_ver = 5
    print(f"Initial value of my_ver: {my_ver}")
    my_ver = add_one(my_ver)
    print(f"Updated value of my_ver after add_one: {my_ver}")
if __name__ == "__main__":
    main()
    