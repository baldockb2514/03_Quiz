# Version 3 - efficiency

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


while True:

    print()
    difficulty_check = yn_difficulty("Difficulty? ", "difficulty")

    if difficulty_check == "easy" or difficulty_check == "normal" or difficulty_check == "hard" \
            or difficulty_check == "mix":
        print(f"Response = {difficulty_check}")
        continue

print()
yn_check = yn_difficulty("Yes or No? ", "y_n")

if yn_check == "yes" or yn_check == "no":
    print(f"Response = {yn_check}")



