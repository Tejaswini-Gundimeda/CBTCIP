import random

def hint(secret, guess):
    correct_place = sum(s == g for s, g in zip(secret, guess))
    correct_digits = sum(min(secret.count(d), guess.count(d)) for d in set(guess))
    return correct_place, correct_digits - correct_place

def mastermind():
    secret1 = input("Player 1, set a multi-digit number: ")
    print("\n" * 50) 
    attempts2 = 0
    while True:
        guess2 = input("Player 2, guess the number: ")
        attempts2 += 1
        if guess2 == secret1:
            print("Player 2 guessed the number correctly!")
            break
        else:
            correct_place, correct_digits = hint(secret1, guess2)
            print(f"Hint: {correct_place} digits are correct and in the correct place, {correct_digits} digits are correct but in the wrong place.")

    print(f"Player 2 took {attempts2} attempts to guess the number.")
    secret2 = input("Player 2, set a multi-digit number: ")
    print("\n" * 50)
    attempts1 = 0
    while True:
        guess1 = input("Player 1, guess the number: ")
        attempts1 += 1
        if guess1 == secret2:
            print("Player 1 guessed the number correctly!")
            break
        else:
            correct_place, correct_digits = hint(secret2, guess1)
            print(f"Hint: {correct_place} digits are correct and in the correct place, {correct_digits} digits are correct but in the wrong place.")

    print(f"Player 1 took {attempts1} attempts to guess the number.")
    if attempts1 < attempts2:
        print("Player 1 wins and is crowned Mastermind!")
    else:
        print("Player 2 wins and is crowned Mastermind!")
mastermind()
