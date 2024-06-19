def copy_file():
    src = 'source.txt'
    dest = 'destination.txt'
    with open(src, 'r') as file_src:
        content = file_src.read()
    with open(dest, 'w') as file_dest:
        file_dest.write(content)

copy_file()
