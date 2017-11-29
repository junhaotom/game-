sb = 666
guess = int(input("Guess a number: "))
if guess > 666:
    print("The guess is bigger than the number")
    print("The number is smaller than", guess)
if guess < 666:
    print("The guess is smaller than the number")
    print("The number is bigger than", guess)
if guess == 666:
    print("You are right")
