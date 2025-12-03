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
    print("the quiz is finished thank you for playing")
    print("your final score is " + str(scoreTracker) + " out of 5")

quiz()








