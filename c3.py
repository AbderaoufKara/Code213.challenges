game = True
while game ==True :
    tempreture = int(input('Type your tempreture in celcius = '))
    choice = int(input("now choose 1 for celcius to kelvin, 2 for celcius to fahrenheit, and 3 to exit "))
    if choice == 1:
        K = tempreture + 273.15
        print(f'Then your tempreture is {K}')
    elif choice == 2:
        F = tempreture*(9/5) + 32
        print(f"Then your tempreture is {F}")
    elif choice == 3:
        print('Good Bye ')
        game = False
    else :
        print("That wasn't an option.")