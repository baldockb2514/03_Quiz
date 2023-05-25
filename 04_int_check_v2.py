# v1 - recycled from higher lower

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

