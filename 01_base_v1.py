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
    statement_decorator("How to Play", "~")
    print()
    print("For each game you play, you will be asked to choose a mode and difficulty.")
    print()
    print("The modes you can choose are factorise questions, and expand questions. "
          "You can also enter \"mix\", which means the mode for each question is random. ")
    print()
    print("The Difficulties you can choose from are easy, normal, hard and mix.")
    print(" - Easy questions have 1 bracket, eg. 2(x-1)")
    print(" - Normal questions have 2 brackets, eg. (x+1)(x-2)")
    print(" - Hard questions will have 3 brackets, eg. (x-1)(x+2)(x-3).")
    print(" - If you choose mix, every question will have a random difficulty.")
    print()
    print("Then you can choose how many questions you want to be asked. If you don't want a limit,"
          " you can press <enter> for continuous mode")
    print()
    print("You will then be given a question and asked to answer it.")
    print("!! If a answer includes exponents, please use the ^ symbol, eg. x^2 !!")
    print()
    print("You will have 5 tries to get the answer correct, but you can choose to give up earlier.")
    print()
    print("To exit the game, you can enter \"xxx\" when asked for your answer.")
    print()
    print("Enjoy!")
    print()
    return ""


# Check if a number is an Integer above 0(or "")
def question_amount():
    while True:
        response = input("How many questions?: ")

        round_error = "Please type either an integer that is more than(or equal to) 1 or <enter> for continuous mode."

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


# generate questions and answers
def question_generator(mode, question_type):
    # Set up lists and strings
    numbers = []
    question_outline = []
    mix_modes = ["easy", "normal", "hard"]
    mix_types = ["factorise", "expand"]
    solved = ""
    answer = ""
    question = ""

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
        x_value = random.randint(-10, 9)

        # don't allow all numbers to be negative to avoid confusing the user
        if in_bracket < 0 and out_of_bracket < 0 and x_value < 0:
            in_bracket = in_bracket * -1
            out_of_bracket = out_of_bracket * -1
            x_value = x_value * -1

        # If either number is 0, make it 10
        if in_bracket == 0:
            in_bracket = 10
        if out_of_bracket == 0:
            out_of_bracket = 10
        if x_value == 0:
            x_value = 10

        # get the numbers for the solved string
        final_number = in_bracket * out_of_bracket
        easy_x_value = x_value * out_of_bracket

        # Add a plus sign for positive numbers, so that the question has a function
        if in_bracket > 0:
            in_bracket = f"+{in_bracket}"
        if final_number > 0:
            final_number = f"+{final_number}"

        # Set answer and question
        solved = f"{easy_x_value}x{final_number}"
        if x_value != 1:
            brackets_outline = f"{out_of_bracket}({x_value}x{in_bracket})"
        else:
            brackets_outline = f"{out_of_bracket}(x{in_bracket})"
        question_outline.append(brackets_outline)

    elif mode == "normal" or mode == "hard":

        # Get 2 sets of brackets
        for number in range(1, 3):

            # Make sure that both the positive and negative version of a number aren't both in the same question
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
    elif question_type == "factorise":
        question = solved
        answer_tuple = tuple(question_outline)
        answer = "".join(answer_tuple)
    # return answer and question as list
    return [answer, question]


# Main Routine goes here
print()
statement_decorator("Welcome to Quiz Quest!", "*")
print()
# ask the user if they want to see the instructions
print_instructions = string_check("Would you like to see the instructions?: ", ["yes", "no"], "Please answer yes/no.")
# if yes, print the instructions
if print_instructions == "yes":
    print()
    print()
    instructions()

while True:

    # Set counters and strings for later reference
    questions_answered = 1
    incorrect_answers = 0
    correct_questions = 0
    incorrect_questions = 0
    score = 0
    quiz_summary = []
    quiz_score = []
    outcome = ""

    # get the mode
    print()
    question_mode = string_check("Would you like factorise questions, expand questions, or a mix of both? ",
                                 ["factorise", "expand", "mix"], "please answer factorise/expand/mixed")
    print(f"Thank you. Your question type is {question_mode}.")

    # get the difficulty
    print()
    difficulty = string_check("Do you want the questions to be Easy, Normal, Hard or a Mix?: ",
                              ["easy", "normal", "hard", "mix"], "Please enter easy/normal/hard/mix.")
    print(f"Thank you. Your questions will be {difficulty}.")

    # get the amount of questions
    print()
    quiz_mode = ""
    max_questions = question_amount()
    if max_questions == "":
        quiz_mode = "continuous"

    end_game = "no"
    while end_game == "no":

        # Set questions Heading depending on the mode
        print()
        if quiz_mode == "continuous":
            heading = f"Continuous Mode: Question {questions_answered}"
        else:
            heading = f"Question of {questions_answered} of {max_questions}"

        statement_decorator(heading, "-")

        # Set a list to prevent duplicate answers
        incorrect_answers = []

        # set a counter for the amount of times answered
        times_answered = 0

        # generate the question and answer
        get_question = question_generator(difficulty, question_mode)

        while True:
            quiz_question = get_question[1]
            quiz_answer = get_question[0]
            print()
            print(quiz_question)
            print(quiz_answer)
            if "(" in quiz_answer:
                user_answer = input(f"Please factorise this equation: ").replace(" ", "").lower()
            else:
                user_answer = input(f"Please expand this equation: ").replace(" ", "").lower()
            times_answered += 1

            # If user inputs xxx, end game
            if user_answer == "xxx":
                end_game = "yes"
                break

            # if the answer is a duplicate, print an error and reprint the question
            elif user_answer in incorrect_answers:
                print(f"Please give an answer you have not tried before.\n You *still* have {6 - times_answered}"
                      f" tries left. ")
                continue
            # Different outcomes for correct and incorrect questions
            elif user_answer == quiz_answer:
                statement_decorator(f"Well done! You got it in {times_answered}.", "*")
                score = times_answered
                outcome = f"Round: {questions_answered}\n You got it in {score}.\n"
                correct_questions += 1
                break

            else:
                incorrect_answers.append(user_answer)
                # Allow the user multiple answers
                if times_answered <= 4:
                    try_again = string_check("Incorrect. Would you like to try again? ", ["yes", "no"],
                                             "Please answer yes/no").lower()
                    if try_again == "yes":
                        statement_decorator(f"You have {5 - times_answered} tries left", "!")
                        continue
                    # let the user choose to give up on the question
                    else:
                        statement_decorator("Good luck next time.", "~")
                        outcome = f"Round: {questions_answered}\n Incorrect.\n"
                        score = 6
                        incorrect_questions += 1
                        break

                # Don't let the user have more than 5 tries to get it right
                else:
                    print("Incorrect. You ran out of tries.")
                    outcome = f"Round: {questions_answered}\n You ran out of tries.\n"
                    incorrect_questions += 1
                    score = 6
                    break

        # If the exit code was entered, don't append the outcome. Otherwise, add the outcome to the list
        if user_answer != "xxx":
            quiz_summary.append(outcome)
            quiz_score.append(score)
            questions_answered += 1
            # if the number of questions is more than questions answered or the mode is continuous, continue quiz
            if quiz_mode == "continuous" or max_questions >= questions_answered:
                continue
            # otherwise, end quiz
            else:
                break

    # if at least one question has been answered, ask the user if they want to see a summary of their quiz,
    if questions_answered != 0:
        print()
        see_summary = string_check("Would you like to see the summary of your game? ", ["yes", "no"],
                                   "Please answer yes/no")
        if see_summary == "yes":
            # Calculate quiz statistics (Best score, worst score average, percentage correct and incorrect)
            percent_correct = correct_questions / questions_answered * 100
            percent_incorrect = incorrect_questions / questions_answered * 100
            best_score = min(quiz_score)
            worst_score = max(quiz_score)
            ave_score = (sum(quiz_score)) / len(quiz_score)

            # print quiz summary heading
            print()
            print("***** Quiz History *****")
            print()
            for outcome in quiz_summary:
                # Print the outcome of each round
                print(outcome)

            # displays quiz stats with % values to the nearest whole number
            statement_decorator("Quiz Statistics", "=")
            print("Correct: {}, ({:.0f}%)\nIncorrect: {}, "
                  "({:.0f}%)".format(correct_questions, percent_correct, incorrect_questions, percent_incorrect))
            # displays the best, worst and average score
            print(f"Best Score: {best_score:.0f}\nWorst Score: {worst_score:.0f}\nAverage Score: {ave_score:.2f}")

    # Asks if the user wants to replay the quiz
    print()
    replay = string_check("Would you like to play again?: ", ["yes", "no"], "Please answer yes/no")

    # If yes, Replay quiz
    if replay == "yes":
        continue
    # Else, end program
    else:
        break

# Thanks the user for playing
print()
print("Thank you for playing!!")
