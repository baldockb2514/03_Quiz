# v1 - recycled from RPS

# Check if a number is an Integer above 0(or "")
def question_amount():
    while True:
        response = input("How many rounds?: ")

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
rounds = check_rounds()
print("Program continues")
