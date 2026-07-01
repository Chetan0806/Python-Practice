numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if len(numbers) == 0:
    print("The list is empty.")
else:
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    print(f"Largest number: {largest}")