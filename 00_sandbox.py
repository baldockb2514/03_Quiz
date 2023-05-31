import random

def question_generator():

    functions = ["+", "-"]

    first_numbers = []
    question_outline = []

    for number in range(1, 2):

        number = random.randint(-10, 9)
        if number == 0:
            number = 10
        first_numbers.append(number)
        if number < 0:
            brackets_outline = f"(x{number}"
        else:
            brackets_outline = f"(x+{number}"
        question_outline.append(brackets_outline)
        if len(question_outline) == 2:
            break

    x_value_one = sum(first_numbers)
    integer = first_numbers[0] * first_numbers[1]

    third_number = random.randint(-10, 9)
    if third_number == 0:
        third_number = 10

    if third_number > 0:
        third_brackets = f"(x+{third_number}"
    else:
        third_brackets = f"(x{third_number}"

    question_outline.append(third_brackets)
    print(question_outline)

    final_x_squared_value = x_value_one + third_number
    final_x_value = third_number * x_value_one + integer
    final_integer = integer * third_number

    if final_integer > 0:
        final_integer = f"+{final_integer}"





