import sys
import random 
import simpleEval

digits = [1,2,3,4,5,6,7,8,9]
toTwenty = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

fourDigits = []

evaluate = simpleEval.simple_eval

for _ in range(4):
    choice = random.choice(digits)
    fourDigits.append(choice)
    digits.remove(choice)

print(fourDigits)
print("enter 'q' at anytime to quit")

for n in range(1,21):
    solved = False
    while solved == False:
        print("make {} using the digits {}, {}, {}, and {}:".format(n, fourDigits[0], fourDigits[1], fourDigits[2], fourDigits[3]))
        mathString = input()
        if mathString == 'q':
            sys.exit()
        elif str(fourDigits[0]) in mathString and str(fourDigits[1]) in mathString and str(fourDigits[2]) in mathString and str(fourDigits[3]) in mathString: 
            e = evaluate(mathString)
            if e == n:
                solved = True
            else:
                print("equals ",e)
                print("incorrect, try again")
        else:
            print("use the digits {}, {}, {}, and {} in your expression".format(fourDigits[0], fourDigits[1], fourDigits[2], fourDigits[3]))

        

print("Success! You completed a round of Magoosh's Number Game")
