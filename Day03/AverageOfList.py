def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    total_sum = sum(numbers)
    count = len(numbers)

    return total_sum / count


total_numbers = int(input("How many numbers do you want to enter? "))

user_list = []

for i in range(total_numbers):
    num = float(input(f"Enter number {i + 1}: "))
    user_list.append(num)


average_result = calculate_average(user_list)


print(f"\nThe numbers you entered: {user_list}")
print(f"The average of the list is: {average_result}")