from sqlStuff import highscores, writeInDb
from random import randrange


def generate_question():
    a = randrange(200)
    b = randrange(200)
    action = randrange(4)
    if action == 0:
        answer = a + b
        question = "What is the answer to %d + %d?" % (a, b)
        return (question, answer)
    elif action == 1:
        answer = a - b
        question = "What is the answer to %d - %d?" % (a, b)
        return (question, answer)
    elif action == 2:
        answer = a * b
        question = "What is the answer to %d * %d?" % (a, b)
        return (question, answer)
    elif action == 3:
        answer = a // b
        question = "What is the answer to %d / %d?" % (a, b)
        return (question, answer)


def main():
    user_input = input("Welcome to the \"Do you even math?\" game!\nHere are your options:\n- start\n- highscores\n")
    if user_input == "highscores":
        highscores()
    elif user_input == "start":
        username = input("Enter your playername>")
        print("Welcome %s! Let the game begin!" % (username,))
        correctAnswers = 0
        while(True):
            questionInfo = generate_question()
            answer = questionInfo[1]
            userAnswer = int(input(questionInfo[0]))
            if answer == userAnswer:
                print("correct!\n")
                correctAnswers += 1
            else:
                points = correctAnswers**2
                print("Incorrect! Ending game. You score is: %d" % (points,))
                writeInDb(username, points)
                break


if __name__ == "__main__":
    main()
