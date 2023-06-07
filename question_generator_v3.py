import random
import numpy


def unpack(*list_unpack):
    unpacked = f"{list_unpack}".replace(",", "").replace("'", "").replace(" ", "")
    return unpacked


def question_generator(mode, question_type):
    # Set up lists
    numbers = []
    question_outline = []
    mix_modes = ["easy", "normal", "hard"]
    times_answered = 0

    # If the mode is mix, for every question generate a random mode
    if mode == "mix":
        mode = random.choice(mix_modes)

    # Questions when the mode is easy
    if mode == "easy":
        # Get numbers
        in_bracket = random.randint(-10, 9)
        out_of_bracket = random.randint(-10, 9)
        # If either number is 0, make it 10
        if in_bracket == 0:
            in_bracket = 10
        if out_of_bracket == 0:
            out_of_bracket = 10
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
        for number in range(1, 3):

            # Get 2 sets of brackets
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
        integer = numpy.prod(numbers)

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

            # if generated number is positive, add a add symbol infront for printing purposes, also turn it into bracket
            if third_number > 0:
                third_brackets = f"(x+{third_number})"
            else:
                third_brackets = f"(x{third_number})"

            # append bracket to question outline
            question_outline.append(third_brackets)

            final_x_squared_value = x_value_one + third_number
            final_x_value = third_number * x_value_one + integer
            final_integer = integer * third_number

            if final_integer > 0:
                final_integer = f"+{final_integer}"
            if final_x_value > 0:
                final_x_value = f"+{final_x_value}"
            if final_x_squared_value > 0:
                final_x_squared_value = f"+{final_x_squared_value}"

            solved = f"X^3{final_x_squared_value}x^2{final_x_value}x{final_integer}"

    if question_type == "expand":
        question = unpack(*question_outline)
        answer = solved
    else:
        question = solved
        answer = unpack(*question_outline)
    print()
    print(f"{mode} {question_type} test:")
    # Print the answer for testing purposes
    print(answer)
    incorrect_answers = []
    while True:
        # unpack the list and put the items right nxt to each other
        print(question)
        get_answer = input(f"Please {question_type} this equation: ")
        if get_answer in incorrect_answers:
            print("Please give an answer you have not tried before. ")
            continue
        # Return whether their answer is correct or incorrect
        if get_answer == answer:
            times_answered += 1
            print(f"Well done! You got it in {times_answered}.")
            result = "correct"
            return result
            break
        else:
            incorrect_answers.append(get_answer)
            times_answered += 1
            try_again = input("Incorrect. Would you like to try again? ").lower()
            if try_again == "yes":
                continue
            else:
                break


while True:

    factorise_test = question_generator("mix", "factorise")

    if factorise_test != "correct":
        print("Good luck next time.")

    expand_test = question_generator("mix", "expand")

    if expand_test != "correct":
        print("Good luck next time.")
