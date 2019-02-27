import random
words = {1:"dolphin", 2: "cat",3: "dog", 4:"parrot"}
chosen_word = random.choice(list(words.values()))
progress = list("*" * len(chosen_word))
wrongs = 0
while progress != list(chosen_word):
    if wrongs < 5:
        print("Guess a letter:")
        guess = input()
        if guess in chosen_word:
            print("Right!")
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    progress[i] = guess
                    print("".join(progress))
        else:
            wrongs += 1
            print("Mistake", wrongs, "out of 5")
    elif wrongs == 5:
        print("U lost the game...")
        break
if progress == list(chosen_word):
    print("U win, luckydog")