import random


def guess_the_number():
    number = random.randrange(0,100)
    attempts = 0

    print("Welcome to the 'Guess the number' !")
    print("I am thinking of a number between 1-100.")

    while True:
        try:
            guess = int(input("Guess the number between 0-100 = "))
        except Exception:
            print("Please enter a valid number between 0-100.")
            continue
        attempts += 1        

        if guess < number:
            print("Number is too low.. guess again!!!")
        elif guess > number:
            print("Number is too high.. guess again!!!")
        else:
            print(end='\n')
            print(end='\n')
            print(f"Congratulations!!!! you have guessed the number correctly in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
