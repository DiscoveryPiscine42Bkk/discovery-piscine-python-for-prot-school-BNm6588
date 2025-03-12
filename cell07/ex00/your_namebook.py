def array_of_name(names_dict):
    full_name = []
    for first_name, last_name in names_dict.items():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_name.addend(full_name)
    return full_name
if __name__ == " __main__ ":
    names = { 
            "john": "doe", 
            "jane": "smith", 
            "alice": "johnson"
    }
    print(array_of_name(names))

