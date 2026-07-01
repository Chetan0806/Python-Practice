user_input = input("Enter numbers: ")
numbers = [int(x) for x in user_input.split()]

start = 0
end = len(numbers) - 1

while start < end:
    temp = numbers[start]
    numbers[start] = numbers[end]
    numbers[end] = temp
    
    start += 1
    end -= 1

print("Reversed list:")
if numbers:
    print(*numbers)
else:
    print("")