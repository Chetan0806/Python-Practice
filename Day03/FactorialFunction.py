def factorial(number):
    if number == 0:
        return 1

    result = 1
    for i in range(1, number + 1):
        result = result * i

    return result


num_to_check = int(input("Enter a number: "))
final_answer = factorial(num_to_check)

print(f"The factorial of {num_to_check} is {final_answer}")