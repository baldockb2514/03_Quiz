# checks user response is yes/no or easy/normal/hard/mix to a given question
def yn_difficulty(question, check):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        if check == "y_n":
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


# Check if a number is an Integer above specified bounds
def int_check(question, low=None, exit_code=None):
    # set the situation depending on what parameters were entered
    if low is not None:
        situation = "low"
        error = f"Please enter a number that is higher than (or equal to) {low}"
    else:
        situation = "any integer"
        error = "Please enter an integer"

    while True:

        # Allow "" and the exit code to be a valid input
        response = input(question)
        if exit_code is not None:
            if response == "":
                return response
            if response == exit_code:
                return response

        try:
            response = int(response)

            # checks if a number is higher than low if only lower bounds are specified
            if situation == "low":
                if response >= low:
                    return response

            else:
                return response

            print(error)

        # If input it not an integer, print error and ask question again
        except ValueError:
            print(error)
            continue


lowest = int_check("Any integer: ")
highest = int_check("Above integer: ", lowest + 1)
print("Program continues")
