print("🎮 Welcome to Hangman!")

# Step 4: Game loop
while attempts_left > 0 and "_" in guessed_word:
    print("\nWord: ", " ".join(guessed_word))
    print("Attempts left:", attempts_left)
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter!")
    elif guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("✅ Good guess!")
    else:
        attempts_left -= 1
        print("❌ Wrong guess!")
    guessed_letters.append(guess)

# Step 5: End of game
if "_" not in guessed_word:
    print("\n🎉 You win! The word was:", word)
else:
    print("\n😢 You lose! The word was:", word)
