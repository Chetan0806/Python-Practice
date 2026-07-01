numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if len(numbers) < 2:
    print("Not enough distinct numbers.")
else:
    largest = None
    second_largest = None

    for num in numbers:
        if largest is None:
            largest = num
        
        elif num > largest:
            second_largest = largest
            largest = num
            
        elif num != largest and (second_largest is None or num > second_largest):
            second_largest = num

    if second_largest is None:
        print("Not enough distinct numbers.")
    else:
        print(f"Second largest number: {second_largest}")