email = input("Enter email: ")

at_count = email.count("@")

if at_count == 1:
    at_index = email.index("@")
    
    domain_part = email[at_index + 1:]
    
    if email.startswith("@"):
        print("Invalid Email")
    elif email.endswith("."):
        print("Invalid Email")
    elif "." not in domain_part:
        print("Invalid Email")
    else:
        print("Valid Email")
else:
    print("Invalid Email")