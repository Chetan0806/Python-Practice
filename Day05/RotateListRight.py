user_input = input("Enter numbers: ")
numbers = [int(x) for x in user_input.split()]

if len(numbers) > 1:
    last_element = numbers[-1]
    
    for i in range(len(numbers) - 1, 0, -1):
        numbers[i] = numbers[i - 1]
        
    numbers[0] = last_element

print("Rotated list:")
if numbers:
    print(*numbers)
else:
    print("")