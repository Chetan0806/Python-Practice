def is_prime(number):
    
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


num_to_test = int(input("Enter a Number: "))

if is_prime(num_to_test):
    print(f"{num_to_test} is a prime number.")
else:
    print(f"{num_to_test} is not a prime number.")