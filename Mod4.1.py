# Write a multiplication quiz to ask 10 questions ranging from 0x0 to 9x9
# When the user enters the correct answer, the program displays "Correct!" for 1 second
# The user gets three tries to enter the correct answer before the program moves on
# Eight seconds after first diplaying the question,
# the question is marked as incorrect even if the user enters the correct asnwer after

# Module 4 assignment 1
# Ian Johnson

import pyinputplus as pyip
import random, time

#Variables for the quiz:
numberOfQuestions = 10
correctAnswers = 0

# Itterate the picking random numbers to multiply for how ever many questions there are.
for questionNumber in range(numberOfQuestions):

    # Pick two random numbers for the questions:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    # Write the question.
    #(Books) prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    prompt = f'#{questionNumber + 1}: {num1} x {num2} = '
    
    # Following is for testing: 
    # print (prompt)

    # Ask the user the question.
    # Use try so that exceptions can be made.
    # Use inputNum to ensure the user inputs a number 
    try:
        pyip.inputNum(prompt, 
                      allowRegexes = ['^%s$' % (num1 * num2)],  # If the number entered is correct, it will skip to the else statement
                      blockRegexes = [('.*', 'Incorrect!')],    # Anything else will respond with "Incorrect!"
                      timeout = 8, limit = 3)                   # Set the time to 8 seconds and the retry limit to 3 times.

    # The following exception changes the output if the time exceeds the timeout limit.    
    except pyip.TimeoutException:
        print('Time is up!')
    
    # This exception is the same thing but for the retry limit
    except pyip.RetryLimitException:
        print('Out of Tries')

    # If everything passes i.e. the number is correct, within the limit of tries and within the time limit
    # the output is "correct" and the counter for correct asnwers goes up:
    else:
        print('Correct!')
        correctAnswers += 1

    # Pause to hold the print before the for loop starts again.
    time.sleep(1)

# show the score at the end
# Book: print('Score: %s / %s' % (correctAnswers, numberOfQuestions))2
print(f'Score: {correctAnswers} / {numberOfQuestions}')




