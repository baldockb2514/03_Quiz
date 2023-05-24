# checks user response is yes/no or easy/normal/hard/"" to a given question
def yn_difficulty(question, check):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        if check == "y_n":
            answer_list = ["yes", "no", "yes", "continue"]
            error = "Please answer yes / no"
        elif check == "difficulty":
            answer_list = ["easy", "normal", "hard", "mix"]
            error = "Please answer easy, normal, hard, mix."

        while True:
            if response in answer_list:
                return response

            elif response == answer_list[0][0]:
                response = answer_list[0]
                return response

            elif response == answer_list[1][0]:
                response = answer_list[1]
                return response

            elif response == answer_list[2][0]:
                response = answer_list[2]
                return response

            elif response == answer_list[3][0]:
                response = answer_list[3]
                return response

            # If not, print error
            else:
                print(error)
                print()
                break


while True:
    print()
    yn_check = yn_difficulty("Yes or No? ", "y_n")

    if yn_check == "yes" or yn_check == "no":
        print(f"Response = {yn_check}")
        print("program continues")
        continue

    elif yn_check == "continue":
        print()
        difficulty_check = yn_difficulty("Difficulty? ", "difficulty")

        if difficulty_check == "easy" or difficulty_check == "normal" or difficulty_check == "hard" \
                or difficulty_check == "mix":
            print(f"Response = {difficulty_check}")
            print("program continues")
            continue




