# 소스코드수정중

import random

num1 = int(input("하나를 선택하세요 : 가위(0), 바위(1), 보(2) :"))
num2 = random.randrange(0, 3)

if num2 == 0:
    print("컴퓨터는 가위를 냈습니다. AI Scissors")
elif num2 == 1:
    print("컴퓨터는 바위를 냈습니다. AI rocks")
else:
    print("컴퓨터는 보를 냈습니다.AI papers")

if num1 == 0:
    if num2 == 1:
        print("컴퓨터가 이겼습니다 Computer Wins!")
    elif num2 == 2:
        print("당신이 이겼습니다. You Win!")
    else:
        print("비겼습니다.Draw!")
elif num1 == 1:
    if num2 == 0:
        print("당신이 이겼습니다.You Win!")
    elif num2 == 2:
        print("컴퓨터가 이겼습니다.Computer Wins!")
    else:
        print("비겼습니다.Draw")
else:
    if num2 == 0:
        print("컴퓨터가 이겼습니다")
    elif num2 == 1:
        print("당신이 이겼습니다.")
    else:
        print("비겼습니다.")
