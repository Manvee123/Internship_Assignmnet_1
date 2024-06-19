def count_occurrences():
    elements = input("Enter a list of elements separated by spaces: ").split()
    specific_element = input("Enter the element to count: ")
    count = elements.count(specific_element)
    print(f"The element '{specific_element}' occurs {count} times.")

count_occurrences()