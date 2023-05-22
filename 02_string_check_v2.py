# checks user response is yes/no or easy/normal/hard/"" to a given question
def yn_difficulty(question, check):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        if check == "yn":
            answer_list = ["yes", "no"]
            error = "Please answer yes / no"
        elif check == "difficulty":
            answer_list = ["easy", "normal", "hard", "mix"]
            error = "Please answer easy, normal, hard, mix."

        if question == answer_list[0][0]:
            question = answer_list[0]
            print(f"{question}")

        elif question == answer_list[1][0]:
            question = answer_list[1]
            print(f"{question}")

        if check == "difficulty":
            if question == answer_list[2][0]:
                question = answer_list[2]
                print(f"{question}")

            elif question == answer_list[3][0]:
                question = answer_list[3]
                print(f"{question}")

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

