def multiplication_table(number):
    for i in range(1, 11):
        result = number * i

        print(f"{number} x {i} = {result}")



user_input = int(input("Enter a number: "))

multiplication_table(user_input)