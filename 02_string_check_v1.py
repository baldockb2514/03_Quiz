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


while True:
    print()
    yn_check = yn_difficulty("Yes or No? ", "yn")

    if yn_check == "yes" or yn_check == "no":
        print(f"Response = {yn_check}")
        print("program continues")
        continue

    elif yn_check == "continue":

        while range(1, 4):

            print()
            difficulty_check = yn_difficulty("Difficulty? ", "difficulty")

            if difficulty_check == "easy" or difficulty_check == "normal"  or difficulty_check == "hard" \
                    or difficulty_check == "mix":
                print(f"Response = {difficulty_check}")
                print("program continues")
                continue

        print("program continues")

