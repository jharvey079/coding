def quiz():
    print("Enter 0 to start the quiz")
    selection = input()
    if int(selection) == 0:
        print("The quiz is starting")
        print("what is def?")
        print("A: a function?")
        print("B: ?")
        print("C: ?")
        print("D: ?")
    questionOne = input()
    if (questionOne) == "A":
        print("correct + 1 Point")
    else:
        print("incorrect the answer was a function")
        print("what is a for loop?")
        print("A: ?")
        print("B: A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).?")
        print("C: ?")
        print("D:?")
    questionTwo = input()
    if (questionTwo) == "B":
        print("correct + 1 Point")
        scoreTracker = 1
    else: 
        print("incorrect the answer was B")
        print("...?")
        print("A: ?")
        print("B: ?")
        print("C: ?")
        print("D: ?")
    questionThree = input()
    if (questionThree) == "D":
        print("correct + 1 Point")
        scoreTracker = 2
    else: 
        print("...?")
        print("A: ?")
        print("B: ?")
        print("C: ?")
        print("D: ?")
        print("incorrect the answer was D")
    print("...?")
    print("A: ?")
    print("B: ?")
    print("C: ?")
    print("D: ?")
    questionFour = input()
    if int(questionFour) == 500:
        print("correct + 1 Point")
        scoreTracker = 3
    else:
        print("incorrect the answer was 500")
    print("...?")
    print("A: ?")
    print("B: ?")
    print("C: ?")
    print("D: ?")
    questionFive = input()
    if int(questionFive) == 1500:
        print("correct + 1 point")
        scoreTracker = 5
    else:
        print("incorrect the answer was 1500")
    print("...?")
    print("A: ?")
    print("B: ?")
    print("C: ?")
    print("D: ?")
    questionSix = input()
    if int(questionSix) == 100:
            print("correct + 1 point")
            scoreTracker = 6
    else:
            print("incorrect the answer was 100")
    print("...?")
    print("A: ?")
    print("B: ?")
    print("C: ?")
    print("D: ?")
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