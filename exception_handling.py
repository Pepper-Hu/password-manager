
try:
    # FileNotFoundError
    file = open("a_file.txt","r")

    # KeyError
    a_dictionary = {"key": "value"}
    print(a_dictionary["not_existing_key"])
except FileNotFoundError:
    file = open("a_file.txt","a")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("The file has been closed")