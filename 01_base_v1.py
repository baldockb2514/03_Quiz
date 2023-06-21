import random
import math


# checks user response is yes/no or easy/normal/hard/mix to a given question
def string_check(question, answer_list, error):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

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


# generate questions
def question_generator(mode, question_type):
    # Set up lists
    numbers = []
    question_outline = []
    mix_modes = ["easy", "normal", "hard"]
    mix_types = ["factorise", "expand"]
    # (put guess / times answered out of component when integrating for scoring purposes)
    solved = ""

    # If the mode/type is mix, for every question generate a random mode/type
    if mode == "mix":
        mode = random.choice(mix_modes)
    if question_type == "mix":
        question_type = random.choice(mix_types)

    # Questions when the mode is easy
    if mode == "easy":
        # Get numbers for the solved string
        in_bracket = random.randint(-10, 9)
        out_of_bracket = random.randint(-10, 9)

        # If either number is 0, make it 10
        if in_bracket == 0:
            in_bracket = 10
        if out_of_bracket == 0:
            out_of_bracket = 10
        # get one of the numbers for the solved string
        final_number = in_bracket * out_of_bracket

        # Add a plus sign for positive numbers, so that the question has a function
        if in_bracket > 0:
            in_bracket = f"+{in_bracket}"
        if final_number > 0:
            final_number = f"+{final_number}"

        # Set answer and question
        solved = f"{out_of_bracket}x{final_number}"
        brackets_outline = f"{out_of_bracket}(x{in_bracket})"
        question_outline.append(brackets_outline)

    elif mode == "normal" or mode == "hard":

        # Get 2 sets of brackets
        for number in range(1, 3):

            # Make sure that both the positive and negative version of a number are both in one question
            while True:
                number = random.randint(-10, 9)
                number_2 = -1 * number
                if number == 0:
                    number = 10
                if number_2 not in numbers:
                    numbers.append(number)
                    break

            if number < 0:
                brackets_outline = f"(x{number})"
            else:
                brackets_outline = f"(x+{number})"
            question_outline.append(brackets_outline)
            if len(question_outline) == 2:
                break

        x_value_one = sum(numbers)
        integer = math.prod(numbers)

        if mode == "normal":
            if x_value_one > 0:
                x_value_one = f"+{x_value_one}"
            if integer > 0:
                integer = f"+{integer}"
            solved = f"x^2{x_value_one}x{integer}"

        else:
            while True:
                # Get the number in the 3rd bracket
                third_number = random.randint(-10, 9)
                # Set any 0's to 10
                if third_number == 0:
                    third_number = 10
                # Don't allow a negative and positive version of the same number in a question to prevent errors
                third_number_2 = -1 * third_number
                if third_number not in numbers and third_number_2 not in numbers:
                    numbers.append(third_number)
                    break

            # if generated number is positive, add a plus symbol in front of the number for printing purposes,
            # also turn it into bracket
            if third_number > 0:
                third_brackets = f"(x+{third_number})"
            else:
                third_brackets = f"(x{third_number})"

            # append bracket to question outline
            question_outline.append(third_brackets)

            # solve the numbers
            final_x_squared_value = x_value_one + third_number
            final_x_value = third_number * x_value_one + integer
            final_integer = integer * third_number

            # If any of the integers are above 0, Add a plus symbol so the user knows the question
            if final_integer > 0:
                final_integer = f"+{final_integer}"
            if final_x_value > 0:
                final_x_value = f"+{final_x_value}"
            if final_x_squared_value > 0:
                final_x_squared_value = f"+{final_x_squared_value}"

            solved = f"X^3{final_x_squared_value}x^2{final_x_value}x{final_integer}"

    # Set questions and answers depending on if the question is a factorising or expanding question
    if question_type == "expand":
        question_tuple = tuple(question_outline)
        question = "".join(question_tuple)
        answer = solved
    else:
        question = solved
        answer_tuple = tuple(question_outline)
        answer = "".join(answer_tuple)

    # Print difficulty and mode for testing purposes
    print()
    print(f"{mode} {question_type} test:")
    # Print the answer for testing purposes
    print(answer)

    print(question)
    return answer



# Main Routine goes here

print()
statement_decorator("Welcome to Quiz Quest!", "*")
print()
# ask the user if they want to see the instructions
print_instructions = string_check("Yes or No? ", ["yes", "no"], "Please answer yes/no.")
# if yes, print the instructions
if print_instructions == "yes":
    instructions()

while True:

    # Set counters and strings for later reference
    questions_answered = 0

    # get the mode
    print()
    question_mode = string_check("Would you like your to answer Factorise questions, Expand questions, or a Mix?? ",
                                 ["factorise", "expand", "mix"], "please answer factorise/expand/mix")
    print(f"Thank you. You will get {question_mode} questions.")

    # get the difficulty
    print()
    difficulty = string_check("Do you want the questions to be Easy, Normal, Hard or Mixed?: ",
                              ["easy", "normal", "hard", "mixed"], "Please enter easy/normal/hard/mixed.")
    print(f"Thank you. Your questions will be {difficulty}.")

    # get the amount of questions
    print()
    max_questions = question_amount()
    if max_questions == "":
        round_mode = "continuous"

    end_game = "no"
    while end_game == "no":

        # Set questions Heading depending on the mode
        print()
        if question_mode == "infinite":
            heading = f"Continuous Mode: Question {questions_answered + 1}"
        else:
            heading = f"Question of {questions_answered + 1} of {max_questions}"

        print(heading)

        # only allow a set amount of incorrect answers
        times_answered = 0

        # Set a list to prevent duplicate answers
        incorrect_answers = []

        while True:
            get_answer = question_generator(difficulty, question_mode)
            user_answer = input(f"Please {question_mode} this equation: ").replace(" ", "")
            times_answered += 1

            # if the answer is a duplicate, print an error and reprint the question
            if get_answer in incorrect_answers:
                print(f"Please give an answer you have not tried before.\n You *still* have {6 - times_answered} tries "
                      f"left. ")
                continue
            # Return whether their answer is correct or incorrect
            if user_answer == get_answer:
                print(f"Well done! You got it in {times_answered}.")
                result = "correct"

            else:
                incorrect_answers.append(user_answer)
                # Allow the user multiple answers
                if times_answered <= 5:
                    try_again = input("Incorrect. Would you like to try again? ").lower()
                    if try_again == "yes":  # Change to yes/no check
                        print(f"You have {6 - times_answered} tries left")
                        continue
                    else:
                        result = "incorrect"

                # Don't allow them more than 5 tries
                else:
                    print("Incorrect. You ran out of tries.")
                    result = "incorrect"

