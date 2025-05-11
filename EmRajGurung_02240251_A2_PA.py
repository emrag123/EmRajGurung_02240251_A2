import random

player_scores = {
    "number_guessing": 0,
    "rock_paper_scissors": 0,
    "quiz": 0,
    "pokemon": 0,
    "total": 0
}

def number_guessing_game():
    score = 0
    while True:
        number = random.randint(1, 100)
        attempts = 0
        guessed = False
        
        while not guessed:
            guess = int(input("Enter a number in the range of 1 and 100: "))
            attempts += 1
            
            if guess < number:
                print("Your guess is low, try again with higher values.")
            elif guess > number:
                print("Too high, try again with lower values.")
            else:
                print("Congratulations! You guessed the number.")
                score += 10
                guessed = True
                
        print(f"Your score: {score}")
        player_scores["number_guessing"] = score
        player_scores["total"] = sum(player_scores.values())
        
        play_again = input("Do you want to play the number guessing game again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break

def Rock_Paper_Scissor():
    score = 0
    while True:
        computer_choice = random.choice(["rock", "paper", "scissors"])
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
             print("Invalid choice. Please choose rock, paper, or scissors.")
        else:
            print(f"Computer chose: {computer_choice}")
            if user_choice == computer_choice:
                print("It's a tie!")
                score += 5
            elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
                 print("YOU WIN!")
                 score += 10
            else:
                 print("My bad, You lose!")
        
        print(f"Your score: {score}")
        player_scores["rock_paper_scissors"] = score
        player_scores["total"] = sum(player_scores.values())

        play_again = input("Do you want to attampt again? (yes/no): ").lower()
        if play_again =="yes":
            continue
        elif play_again == "no":
            print("thanks!")
            break

def Multiple_Choice():
    score = 0
    while True:
        user = input("Welcome to the new quiz challenge! Choose your category: \n"
             "1. Space \n"
             "2. Biology \n"
             "3. Inventions \n"
             "4. Bhutan Facts \n"
             "5. Movies \n"
             "6. Computers \n"
             "7. Animals \n"
             "8. Language \n"
             "9. Art & Culture \n"
             "10. Food \n"
             "Enter your choice: \n")
        print("Let's begin!")

        if user == "1":
            print("Since you chose Space, here's a cosmic question!")
            print("Question 1: Which planet has the most moons?")
            print("Options:\n"
                  "A) Jupiter\n"
                  "B) Saturn\n"
                  "C) Mars\n"
                  "D) Uranus")
            answer = input("Your answer: ").lower()
            if answer == "b" or answer == "saturn":
                print("Correct!")
                score += 10
            else:
                print("Incorrect! The correct answer is B. Saturn.")

        elif user == "2":
            print("Since you chose Biology, let's test your knowledge!")
            print("Question 1: What part of the cell is known as the 'powerhouse'?")
            print("Options:\n"
                  "A) Ribosome\n"
                  "B) Nucleus\n"
                  "C) Mitochondria\n"
                  "D) Chloroplast")
            answer = input("Your answer: ").lower()
            if answer == "c" or answer == "mitochondria":
                print("Correct!")
                score += 10
            else:
                print("Incorrect! The correct answer is C. Mitochondria.")

        elif user == "3":
            print("Since you chose Inventions, here's a fun one!")
            print("Question 1: Who invented the light bulb?")
            print("Options:\n"
                  "A) Nikola Tesla\n"
                  "B) Thomas Edison\n"
                  "C) Alexander Graham Bell\n"
                  "D) Isaac Newton")
            answer = input("Your answer: ").lower()
            if answer == "b" or answer == "thomas edison":
                print("Correct!")
                score += 10
            else:
                print("Incorrect! The correct answer is B. Thomas Edison.")

        elif user == "4":
            print("Since you chose Bhutan Facts, let's see what you know!")
            print("Question 1: What is the national animal of Bhutan?")
            print("Options:\n"
                  "A) Snow Leopard\n"
                  "B) Takin\n"
                  "C) Red Panda\n"
                  "D) Golden Langur")
            answer = input("Your answer: ").lower()
            if answer == "b" or answer == "takin":
                print("Correct!")
                score += 10
            else:
                print("Incorrect! The correct answer is B. Takin.")

        elif user == "5":
            print("Since you chose Movies, time for some film trivia!")
            print("Question 1: Which movie features the song 'My Heart Will Go On'?")
            print("Options:\n"
                  "A) Titanic\n"
                  "B) Avatar\n"
                  "C) The Notebook\n"
                  "D) La La Land")
            answer = input("Your answer: ").lower()
            if answer == "a" or answer == "titanic":
                print("Correct!")
                score += 10
            else:
                print("Incorrect! The correct answer is A. Titanic.")

        elif user == "6":
            print("Since you chose Computers, here's your tech question!")
            print("Question 1: What does 'CPU' stand for?")
            print("Options:\n"
                  "A) Central Power Unit\n"
                  "B) Computer Processing Unit\n"
                  "C) Central Processing Unit\n"
                  "D) Core Performance Utility")
            answer = input("Your answer: ").lower()
            if answer == "c" or answer == "central processing unit":
                print("Correct!")
                score += 10
            else:
                print("Incorrect! The correct answer is C. Central Processing Unit.")

        elif user == "7":
            print("Since you chose Animals, here we go!")
            print("Question 1: Which mammal lays eggs?")
            print("Options:\n"
                  "A) Kangaroo\n"
                  "B) Platypus\n"
                  "C) Whale\n"
                  "D) Otter")
            answer = input("Your answer: ").lower()
            if answer == "b" or answer == "platypus":
                print("Correct!")
                score += 10
            else:
                print("Incorrect! The correct answer is B. Platypus.")

        elif user == "8":
            print("Since you chose Language, here's a wordy challenge!")
            print("Question 1: What language has the most native speakers?")
            print("Options:\n"
                  "A) English\n"
                  "B) Spanish\n"
                  "C) Hindi\n"
                  "D) Mandarin Chinese")
            answer = input("Your answer: ").lower()
            if answer == "d" or answer == "mandarin chinese":
                print("Correct!")
                score += 10
            else:
                print("Incorrect! The correct answer is D. Mandarin Chinese.")

        elif user == "9":
            print("Since you chose Art & Culture, enjoy this one!")
            print("Question 1: Which festival in Bhutan features masked dances?")
            print("Options:\n"
                  "A) Losar\n"
                  "B) Tshechu\n"
                  "C) Wang Festival\n"
                  "D) Bumthang Drup")
            answer = input("Your answer: ").lower()
            if answer == "b" or answer == "tshechu":
                print("Correct!")
                score += 10
            else:
                print("Incorrect! The correct answer is B. Tshechu.")

        elif user == "10":
            print("Since you chose Food, let's see your taste in trivia!")
            print("Question 1: What is Bhutan's national dish?")
            print("Options:\n"
                  "A) Ema Datshi\n"
                  "B) Phaksha Paa\n"
                  "C) Hoentay\n"
                  "D) Jasha Maroo")
            answer = input("Your answer: ").lower()
            if answer == "a" or answer == "ema datshi":
                print("Correct!")
                score += 10
            else:
                print("Incorrect! The correct answer is A. Ema Datshi.")
        
        print(f"Your score: {score}")
        player_scores["quiz"] = score
        player_scores["total"] = sum(player_scores.values())

        play_again = input("Do you want to play the quiz again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break



def Overall_Scoring_System():
    print("\n--- Overall Scoring System ---")
    print("Number Guessing Game Score: " + str(player_scores["number_guessing"]))
    print("Rock Paper Scissors Score: " + str(player_scores["rock_paper_scissors"]))
    print("Quiz Score: " + str(player_scores["quiz"]))
    print("Pokemon Card Binder Score: " + str(player_scores["pokemon"]))
    print("Total Score: " + str(player_scores["total"]))
    input("Press Enter to continue...")

while True:
    print("Menu: ")
    print("1. Guess number game")
    print("2. Rock Paper Scissors game")
    print("3. Trivia pursuit quiz with different categories and multiple choices ")
    print("4. Pokemon Card Binder Manager ")
    print("5. Overall Scoring system ")
    print("6.Exit")

    user_choice = int(input("Enter your choice: "))
    if user_choice == 6:
        print("Exited the program: ")
        break
    if user_choice == 1:
        number_guessing_game()
    elif user_choice == 2:
        Rock_Paper_Scissor()
    elif user_choice == 3:
        Multiple_Choice()
    elif user_choice == 4:
        from EmRajGurung_02240251_A2_PA import pokemon_card_binder
        pokemon_card_binder()
    elif user_choice == 5:
        Overall_Scoring_System()
    else:
        print("invalid")