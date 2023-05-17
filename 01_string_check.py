# checks user response is yes/no to a given question
def yn_difficulty(question, check):
    valid = False
    while not valid:
        response = input(question).lower()
        response = response.replace(" ", "")

        if check == "yn":
            # If the response is valid, return response
            if response == "yes" or response == "y":
                response = "yes"
                return response

            elif response == "no" or response == "n":
                response = "no"
                return response

            # If not, print error
            else:
                print("Please answer yes / no")

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
                print("Please answer easy, normal or hard.")


while True:
    print()
    yn_check = yn_difficulty("Yes or No? ", "yn")

    if yn_check == "yes" or "no":
        print(yn_check)

    difficulty_check = yn_difficulty("Difficulty? ", "difficulty")

    if difficulty_check == "easy" or "normal" or "hard" or "mix":
        print(difficulty_check)

    continue
