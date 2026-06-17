import random

print("🎮 Welcome to Number Guessing Game!")
print("I am thinking of a number between 1 and 10...")

secret_number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"🎉 Correct! You won in {attempts} attempts")
        break
    elif guess < secret_number:
        print("📉 Too low!")
    else:
        print("📈 Too high!")