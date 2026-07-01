numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if len(numbers) == 0:
    print("The list is empty. Cannot find the smallest number.")
else:
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    print(f"Smallest number: {smallest}")