def sum_of_list():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = [float(num) for num in numbers]
    print("The sum of the list is:", sum(numbers))

sum_of_list()