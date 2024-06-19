def min_max_in_list():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]
    print("Minimum value:", min(numbers))
    print("Maximum value:", max(numbers))

min_max_in_list()