from random import randint

drawn_num = randint(1, 100)
print(drawn_num)
while True:
    try:
        user_num = int(input('Guess the number'))
        if user_num == drawn_num:
                print('You win')
                break
        elif user_num < drawn_num:
                print('To small')
                continue
        else:
                print('To big')
                continue
    except ValueError:
        print('It\'s not a number')
        continue







