import random
number = random.randint(1,1000)
if number % 2 == 0:
    print(f'{number} is even')
elif number % 2 != 0:
    print(f'{number} is not even')