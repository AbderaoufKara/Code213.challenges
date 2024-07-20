calc = True
while calc == True :
    x = int(input("enter a number = "))
    y = int(input("enter other number = "))
    print("Enter 1 to add your numbers")
    print("Enter 2 to subtract your numbers")
    print("Enter 3 to mutiply your numbers")
    print("Enter 4 to divide your numbers")
    print("Enter 5 to exit the program")
    choice = int(input("Enter your choice"))
    if choice == 1 :
        sum = x + y
        print(sum)
    elif choice == 2:
        sum = x - y
        print(sum)
    elif choice == 3:
        sum = x * y
        print(sum)
    elif choice == 4 and y != 0:
        sum = x / y
        print(sum)
    elif choice == 4 and y == 0:
        print("that ain't possible")
    elif choice == 5:
        print("good bye")
        calc = False