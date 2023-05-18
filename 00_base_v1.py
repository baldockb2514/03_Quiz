# checks user response is yes/no or easy/normal/hard/"" to a given question
def yn_difficulty(question, check):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        # If the check parameter is yn, valid answers are yes and no
        if check == "yn":
            # If the response is valid, return response
            if response == "yes" or response == "y":
                response = "yes"
                return response

            elif response == "no" or response == "n":
                response = "no"
                return response

            elif response == "continue":
                response = "continue"
                return response

            # If not, print error
            else:
                print("Please answer yes / no")
                print()

        # If the check parameter is difficulty, valid answers are easy, normal, hard, or ""
        elif check == "difficulty":
            # If the response is valid, return response
            if response == "easy" or response == "e":
                response = "easy"
                return response

            elif response == "normal" or response == "n":
                response = "normal"
                return response

            elif response == "hard" or response == "h":
                response = "hard"
                return response

            elif response == "":
                response = "mix"
                return response

            # If not, print error
            else:
                print("Please answer easy, normal, hard, or <enter> for mix.")
                print()


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
