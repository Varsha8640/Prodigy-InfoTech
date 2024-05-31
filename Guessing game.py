import random

def guessing_game():
  number = random.randint(1, 100)
  attempts = 0

  print("Welcome to the guessing game!")
  print("I've chosen a number between 1 and 100.")

  while True:
    try:
      guess = int(input("Enter your guess: "))
      attempts += 1
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    if guess < number:
      print("Too low! Try again.")
    elif guess > number:
      print("Too high! Try again.")
    else:
      print(f"Congratulations! You guessed it in {attempts} attempts!")
      break

if __name__ == "__main__":
  guessing_game()