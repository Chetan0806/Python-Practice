user_input = input("Enter numbers: ")
numbers = [int(x) for x in user_input.split()]

if len(numbers) > 1:
    first_element = numbers[0]
    
    for i in range(len(numbers) - 1):
        numbers[i] = numbers[i + 1]
        
    numbers[-1] = first_element

print("Rotated list:")
print(*(numbers))