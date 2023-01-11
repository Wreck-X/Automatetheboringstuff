
import random
import time

numeberofquestions = 10
correctAnswers = 0
for questionNumber in range(1, numeberofquestions + 1):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = f'{questionNumber}: {num1} x {num2} = '
    check = num1 * num2
    time_ = time.time() 
    input_ = int(input(prompt))
    if time.time() - time_ > 8 or input_ != check:
        if time.time() - time_ >8:
            print('Timed out')
        if input_!= check:
            print('Wrong answer')
        time_ = time.time()
        continue
    print('Correct')
    correctAnswers += 1
print('correct answers: ', correctAnswers)