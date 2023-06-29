# Version 3 - increase versatility

# checks user response is yes/no or easy/normal/hard/mix to a given question
def string_check(question, answer_list, error):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        while True:
            for item in answer_list:
                if response == item[0] or response == item:
                    return item

            # If not, print error
            else:
                print(error)
                print()
                break


# Testing
while True:

    print()
    check = string_check("Yes or No? ", ["yes", "no"], "Please answer yes/no.")

    # if answer valid, print what the answer is (change for integration)
    if check == "yes" or check == "no":
        print(f"Response = {check}")

print()
check = string_check("Question Type? ", ["factorise", "expand", "mix"], "please answer factorise/expand/mix")

# if answer valid, print what the answer is (change for integration)
if check == "factorise" or check == "expand" or check == "mix":
    print(f"Response = {check}")

print()
check = string_check("Difficulty? ", ["easy", "normal", "hard", "mix"], "Please enter easy/normal/hard/mix.")

# if answer valid, print what the answer is (change for integration)
if check == "easy" or check == "normal" or check == "hard" \
        or check == "mix":
    print(f"Response = {check}")

