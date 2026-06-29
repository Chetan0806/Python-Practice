password = input("Enter a password: ")

special_chars = "@#$%!&*_"

has_upper = False
has_lower = False
has_digit = False
has_special = False

password_length = len(password)

if password_length < 8:
    print("Password Strength: Weak")
else:
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True

        if has_upper and has_lower and has_digit and has_special:
            break

    if has_upper and has_lower and has_digit and has_special:
        print("Password Strength: Strong")
    else:
        print("Password Strength: Medium")