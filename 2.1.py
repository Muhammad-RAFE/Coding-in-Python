import  random


def guess_number():
    min = 0
    max = 99


    ans= random.randint(min,max)

    False = False

    guess = "Guess a number from 0 - 100".format(min,max)

    while  not False:

        try:

            guess = int(raw_input(guess))
            if guess == ans:
                False=True
                print("U R Right")
            elif guess > answer:
                prompt = "{0} is much more , try lower!".format(guess)
            else:
                prompt = "{0} much few , try big number !! ".format(guess)

        except Exception as ex :
            prompt = "Not an integer number:"

guess_number()