import random
words=['apple','banana','grape','orange','cherry','grapes']
word=random.choice(words)
guesses=[]
wrong_guesses=0
max_wrong=6

print("Welcome to Hangman!")

while wrong_guesses < max_wrong:
    display = ''.join([letter if letter in guesses else '_' for letter in word])
    print(f"Word:{display}")
    
    if display==word:
        print("Congratulations! You guessed the word!")
        break
    
    guess=input("Guess a letter:").lower()
    
    if guess in guesses:
        print("You already guessed that letter.")
        continue
    guesses.append(guess)
    
    if guess not in word:
        wrong_guesses += 1
        print(f"Wrong guess! You have {max_wrong - wrong_guesses} tries left.")
        
        if wrong_guesses == max_wrong:
            print(f"Game Over!The word was:{word}")