import random
symbol="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
d=int(input('Какая длина пароля?'))
password=''
for i in range(d):
    password+=random.choice(symbol)
print(password)