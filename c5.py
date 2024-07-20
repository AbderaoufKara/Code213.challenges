password = input("please write your password ")
if len(password) >= 8 :
    is_digit = False
    is_char = False
    for check in password:
        if check.isalpha():
            is_char = True
        if check.isdigit():
            is_digit = True 
    if is_char and is_digit:
        print('strong password')
    else:
        print('weak password')
else:
    print('weak password')