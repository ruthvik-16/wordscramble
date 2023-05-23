import random

def word_scramble_game():
    domains = {
        'fruits': ['apple', 'banana', 'cherry', 'orange', 'blackberry', 'pineapple', 'grape'],
        'animals': ['cat', 'dog', 'elephant', 'giraffe', 'lion', 'tiger', 'zebra'],
        'colors': ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']
    }

    max_attempts = 3
    score = 0

    print("Welcome to Word Scramble!")

    while True:
        domain = input("Select a word domain (fruits/animals/colors): ").lower()
        if domain not in domains:
            print("Invalid domain. Please choose from 'fruits', 'animals', or 'colors'.")
            continue

        word_list = domains[domain]
        word = random.choice(word_list)
        scrambled_word = ''.join(random.sample(word, len(word)))

        print("\nUnscramble the word:", scrambled_word)

        attempts = 0
        while attempts < max_attempts:
            guess = input("Enter your guess: ").lower()

            if guess == word:
                print("Correct guess!")
                score += 1
                break
            else:
                attempts += 1
                remaining_attempts = max_attempts - attempts
                print("Incorrect guess. Try again. Remaining attempts:", remaining_attempts)

        if attempts == max_attempts:
            print("You ran out of attempts. The correct word was:", word)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Game over! Your score:", score)

word_scramble_game()
