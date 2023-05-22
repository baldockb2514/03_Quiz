answer_list = ["yes", "no"]

while True:
    question = input("Yes or no?: ")

    if question == answer_list[0][0]:
        question = answer_list[0]
        print(f"{question}")

    elif question == answer_list[1][0]:
        question = answer_list[1]
        print(f"{question}")

    elif question == answer_list[2][0]:
        question = answer_list[1]
        print(f"{question}")

    elif ValueError:
        print("not valid")
        continue
