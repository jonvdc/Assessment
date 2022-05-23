from questions import quiz


def check_ans(question, ans, attempts, score):

    # Takes the arguments
    # and confirms if the answer provided by user is correct.
    # Converts all answers to lower case
    # to make sure the quiz is not Case sensitive.

    if quiz[question]['answer'].lower() == ans.lower():
        print(f"That's Correct! Your score is now \n{score + 1}/10")
        return True
    else:
        print(f"Sorry, that's incorrect."
              f" \nYou have {attempts - 1} left! \nTry again...")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])


# enables user to 'skip' the question
# if they aren't confident enough to answer it

# gives the user 3 attempts
# to get the question right
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer "
                           "(To move to the next question, type 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    break

# Tells the user what their final score is
print(f"Your final score is {score}/10!\n\n")
print("Here are the answers: \n")
print_dictionary()
print("Thanks for playing!")
