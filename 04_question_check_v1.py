# v1 - recycled from RPS

# Check if a number is an Integer between or equal to 1 - 10 or is "" for continuous mode
def question_amount():
    while True:
        response = input("How many questions?: ")

        round_error = "Please type either an integer that is between(or equal to) 1 - 10 or <enter> for continuous " \
                      "mode."

        if response != "":
            try:
                response = int(response)

                # If the response is not between or equal to 1 - 10 output error and re-ask question
                if response < 1:
                    print(round_error)
                    print()
                    continue

                elif response > 10:
                    print(round_error)
                    print()
                    continue

            except ValueError:
                print(round_error)
                print()
                continue

        return response


while True:
    print()
    questions = question_amount()
    if questions != "":
        print(f"Question amount = {questions}")
    else:
        print("Continuous mode")

    continue
