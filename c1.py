import random
x = random.randint(1,100)
y = random.randint(1,100)
print('before swap')
print(f"this is the first x = {x}")
print(f"this is the first y = {y} ")
x = x + y
y = y - x
x = y + x
print("after swap")
print(f"this is the first x = {x}")
print(f"this is the first y = {-y} ")
if x > -y:
    print(f"x is greater than y {x} > {-y}")
elif x < -y :
    print(f'x is lesser than y : {x} < {-y}')
elif x == -y:
    print(f'x and y are equals {x} == {-y}')
