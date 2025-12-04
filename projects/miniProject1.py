def quiz():
    print("Enter 0 to start the quiz")
    selection = input()
    if int(selection) == 0:
        print("The quiz is starting")
        print("Question 1: What is 2+4?")
    questionOne = input()
    if int(questionOne) == 6:
        print("correct + 1 Point")
    else:
        print("incorrect the answer was 6")
    print("Question 2: What is 10 + 10?")
    questionTwo = input()
    if int(questionTwo) == 20:
        print("correct + 1 Point")
        scoreTracker = 1
    else: 
        print("incorrect the answer was 20")
    print("Question 3: what is 35+15?")
    questionThree = input()
    if int(questionThree) == 50:
        print("correct + 1 Point")
        scoreTracker = 2
    else: 
        print("incorrect the answer was 50")
    print("question 4: what is 100+400?")
    questionFour = input()
    if int(questionFour) == 500:
        print("correct + 1 Point")
        scoreTracker = 3
    else:
        print("incorrect the answer was 500")
    print("Question 5: what is 500+1000?")
    questionFive = input()
    if int(questionFive) == 1500:
        print("correct + 1 point")
        scoreTracker = 5
    else:
        print("incorrect the answer was 1500")
    print("Question 6: what is 25+75?")
    questionSix = input()
    if int(questionSix) == 100:
            print("correct + 1 point")
            scoreTracker = 6
    else:
            print("incorrect the answer was 100")
    print("Question 7: what is 9+10?")
    questionSeven = input()
    if int(questionSeven) == 19:
            print("incorrect the answer was 21. (im just playing) + 1 point")
            scoreTracker = 7
    else:
            print("incorrect the answer was 19")
    print("Question 8: what is 3000+6000?")
    questionEight = input()
    if int(questionEight) == 9000:
            print("correct + 1 point")
            scoreTracker = 8
    else:
            print("incorrect the answer was 9000")
    print("Question 9: what is 10000 + 10000?")
    questionNine = input()
    if int(questionNine) == 20000:
            print("correct + 1 point")
            scoreTracker = 9
    else:
            print("incorrect the answer was 20000")
    print("Question 10: what is 5x5?")
    questionTen = input()
    if int(questionTen) == 25:
            print("correct + 1 point")
            scoreTracker = 10
    else:
        print("incorrect the answer was 25")
    print("the quiz is finished thank you for playing")
    print("your final score is " + str(scoreTracker) + " out of 10")

quiz()








