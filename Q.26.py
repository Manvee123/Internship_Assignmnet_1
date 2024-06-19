def check_prefix_suffix():
    user_input = input("Enter a string: ")
    prefix = input("Enter prefix: ")
    suffix = input("Enter suffix: ")
    if user_input.startswith(prefix):
        print(f"The string starts with '{prefix}'.")
    if user_input.endswith(suffix):
        print(f"The string ends with '{suffix}'.")

check_prefix_suffix()