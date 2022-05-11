# yes/no checking function
def yes_no(question_text):
    while True:

        # Ask the user if they would like to start the quiz
        answer = input(question_text).lower()

        # If they say yes, program continues
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, end the program
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # Otherwise, show error
        else:
            print("Please use either 'yes' or 'no'")


# Function to end the program
def end_quiz():
    print("Program Ends/restarts")


# Main Routine
played_before = yes_no("Would you like to start the quiz? ")

if played_before == "No":
    end_quiz()
else:
    print("Program continues")
