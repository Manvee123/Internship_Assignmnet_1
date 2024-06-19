def read_lines():
    print("Enter lines of text (enter an empty line to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    print("You entered:")
    for line in lines:
        print(line)

read_lines()