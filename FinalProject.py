import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)
result = "a"

print("Guess the characters")

guesses = ''

turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char)

        else:
            print("_")

            failed += 1

    if failed == 0:

        print("You Win")
        result = "game won!"

        print("The word is: ", word)
        break

    guess = input("guess a character:")
    guesses += guess

    if guess not in word:

        turns -= 1

        print("Wrong")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            result = "game lost!"
            print("You Loose")

with open("myGameResults.txt", "w") as f:
    f.write(word)
    f.write("\n")
    f.write(result)