quiz_summary = []
quiz_score = []

incorrect_questions = 0
correct_questions = 0
questions_answered = 5
outcome = ()
score = 0
result = ""

for item in range(0, 5):

    quiz_result = input("choose result: ")

    if quiz_result == "incorrect":
        incorrect_questions += 1
        score = 6
        outcome = "Round {}:\n Result: Incorrect".format(item + 1)
    elif quiz_result == "correct":
        correct_questions += 1
        score = int(input("choose score: "))
        outcome = "Round {}:\n Result: Correct. Score: {}".format(item + 1, score)

    quiz_summary.append(outcome)
    quiz_score.append(score)

# Calculate game stats
percent_correct = correct_questions / questions_answered * 100
percent_incorrect = incorrect_questions / questions_answered * 100
highest_score = min(quiz_score)
lowest_score = max(quiz_score)
ave_score = (sum(quiz_score)) / len(quiz_score)


print()
print("***** Quiz History *****")
for outcome in quiz_summary:
    print(outcome)

print()

# displays game stats with % values to the nearest whole number
print("******* Quiz  Statistics *******")
print("Correct: {}, ({:.0f}%)\nIncorrect: {}, "
      "({:.0f}%)".format(correct_questions, percent_correct, incorrect_questions, percent_incorrect))
print(f"Best Score: {highest_score:.0f}\nWorst Score: {lowest_score:.0f}\nAverage Score: {ave_score:.2f}")
print()
