def read_from_file():
    with open("output.txt", "r") as file:
        content = file.read()
    print(content)

read_from_file()