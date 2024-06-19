def are_anagrams():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    if sorted(str1) == sorted(str2):
        print(f"'{str1}' and '{str2}' are anagrams.")
    else:
        print(f"'{str1}' and '{str2}' are not anagrams.")

are_anagrams()