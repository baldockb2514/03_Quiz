# checks user response is yes/no or easy/normal/hard/mix to a given question
def yn_difficulty(question, check):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        if check == "yn":
            answer_list = ["yes", "no"]
            error = "Please answer yes / no"
        elif check == "difficulty":
            answer_list = ["easy", "normal", "hard", "mix"]
            error = "Please answer easy, normal, hard or mix."

        while True:
            for item in answer_list:
                if response == item[0] or response == item:
                    return item

            # If not, print error
            else:
                print(error)
                print()
                break


# statement decoration types
def statement_decorator(statement, decoration):
    # Make string with five characters
    sides = decoration * 5

    # add decoration to start and ent of statement
    statement = "{} {} {}".format(sides, statement, sides)
    print(statement)

    return ""


# Displays instructions
def instructions():
    statement_decorator("How to Play", "*")
    print()
    print("Display instructions")
    print()
    return ""


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


# Main Routine goes here

print()
statement_decorator("Welcome to Quiz Quest!", "*")
print()
print_instructions = yn_difficulty("Would you like to see the instructions?: ", "yn")
if print_instructions == "yes":
    instructions()

while True:

    # Set counters and strings for later reference
    questions_answered = 0
    mode = "normal"

    print()
    difficulty = yn_difficulty("Do you want the questions to be Easy, Normal, Hard or a Mix?: ", "difficulty")
    print(f"Thank you. Your questions will be {difficulty}.")

    print()
    max_questions = question_amount()
    if max_questions == "":
        mode = "continuous"

    end_game = "no"
    while end_game == "no":

        # Set questions Heading depending on the mode
        print()
        if mode == "infinite":
            heading = f"Continuous Mode: Round {questions_answered + 1}"
        else:
            heading = f"Round of {questions_answered + 1} of {max_questions}"

        print(heading)
