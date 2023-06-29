# v1 - recycled from RPS

# Check if a number is an Integer above 0(or "")
def question_amount():
    while True:
        response = input("How many questions?: ")

        round_error = "Please type either <enter> or an integer that is more than(or equal to) 1"

        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    print()
                    continue

            except ValueError:
                print(round_error)
                print()
                continue

        return response


print()
questions = question_amount()
questions_answered = 1
while True:
    print()
    print(f"Round {questions_answered} of {questions}")
    end_round = input("Would you like to end this round?: ")
    if end_round == "y":
        if questions_answered == questions:
            break
        else:
            questions_answered += 1
            continue

print()
print("Thanks for playing!")
