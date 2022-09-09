import random, time

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
     # Pick two random numbers:
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)

    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)

    try:
        timeout=8
        limit=3
        start_time = time.time()
        while True:
            try:
                if int(input(prompt)) == num1 * num2:
                    break
                raise Exception()
            except:
                print('Incorrect!')
                limit -=1

                if limit <= 0:
                    raise Exception(('Out of tries!'))
            finally:    
                if time.time() > start_time + timeout:
                    raise Exception('Out of time!')
    except Exception as exception:
        print(exception.args[0])
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1

time.sleep(1) # Brief pause to let user see the result.
print('Score: %s / %s' % (correctAnswers, numberOfQuestions))