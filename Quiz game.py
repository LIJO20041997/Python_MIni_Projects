def new_game():

    guesses = []
    correct_guesses = 0
    question_no = 1

    for key in questions:
        print("----------------------------------")
        print(key)
        for i in options[question_no - 1]:
            print(i)

        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_no += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct! ")
        return 1
    else:
        print("Wrong! ")
        return 0


def display_score(correct_guess, guesses):
    print("------------------------------")
    print("Results: ", end="")
    print("------------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guess/len(questions))*100)
    print(f"Your score is: {score}%")


def play_again():
    response = input("Do you want to play again, (yes/no): ").upper()
    if response == "YES":
        return True
    else :
        return False


questions = {
    '1. 2022 FIFA World Cup host country?': 'C',
    '2.2022 FIFA World Cup Winners?': 'A',
    '3. 2022 Winter Olympics host city?': 'B',
    '4. Cricket World Cup winner 2023?': 'B',
    '5. Indian Premier League (IPL) 2023 champion?': 'B',
    '6. 2023 Ballon d"Or winner?': 'A'
}

options = [
    ['A. America', 'B. India', 'C. Qatar', 'D. Spain'],
    ['A. Argentina', 'B. France', 'C. Brazil', 'D. Croatia'],
    ['A. New York', 'B. Beijing', 'C. London', 'D. Paris'],
    ['A. India', 'B. Australia', 'C. England', 'D. West Indies'],
    ['A. Mumbai Indians', 'B. Chennai Super Kings', 'C. Royal Challengers Bangalore', 'D. Delhi Capitals'],
    ['A. Lionel Messi', 'B. Cristiano Ronaldo', 'C. Robert Lewandowski', 'D. Erling Haaland']
]

new_game()

while play_again():
    new_game()

print("Game Over! ")
