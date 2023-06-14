# V3 - Add factorise questions
import random
import math


def question_generator(mode, question_type):
    # Set up lists
    numbers = []
    question_outline = []
    mix_modes = ["easy", "normal", "hard"]
    # (put guess / times answered out of component when integrating for scoring purposes)
    times_answered = 1
    solved = ""

    # If the mode is mix, for every question generate a random mode
    if mode == "mix":
        mode = random.choice(mix_modes)

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
    # Set a list to prevent duplicate answers
    incorrect_answers = []
    while True:
        # unpack the list and put the items right nxt to each other
        print(question)
        get_answer = input(f"Please {question_type} this equation: ").replace(" ", "")
        if get_answer in incorrect_answers:
            print(f"Please give an answer you have not tried before.\n You *still* have {6 - times_answered} tries "
                  f"left. ")
            continue
        # Return whether their answer is correct or incorrect
        if get_answer == answer:
            print(f"Well done! You got it in {times_answered}.")
            result = "correct"
            return result
        else:
            incorrect_answers.append(get_answer)
            times_answered += 1
            # Allow the user multiple answers
            if times_answered < 6:
                try_again = input("Incorrect. Would you like to try again? ").lower()
                if try_again == "yes":  # Change to yes/no check
                    print(f"You have {6 - times_answered} tries left")
                    continue
                else:
                    result = "incorrect"
                    return result
            # Don't allow them more than 5 tries
            else:
                print("Incorrect. You ran out of tries.")
                result = "incorrect"
                return result


# Testing
while True:

    mix_test = question_generator("mix", "factorise")

    if mix_test == "incorrect":
        print("Good luck next time.")
