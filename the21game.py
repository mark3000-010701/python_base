'''
import random
GAME_LIMIT = 21

def main():
    user_points = 0
    computer_points = 0
    print("Welcome to the game of 21! May the odds be ever in your favor...")
    print()
    answer = get_response()
    while answer == "y":
        points, comp_points = roll_dice()
        user_points += points
        computer_points += comp_points
        print("Points:", user_points)
        if user_points == GAME_LIMIT:
            print("User's Points:", user_points)
            print("Computer's Points:", computer_points)
            if computer_points == GAME_LIMIT:
                print("Tie Game!")
            else:
                print("User Wins!")
        if user_points > GAME_LIMIT:
            print("User's Points:", user_points)
            print("Computer's Points:", computer_points)
            if computer_points < GAME_LIMIT:
                print("Computer Wins!")
            elif computer_points == GAME_LIMIT:
                print("Computer Wins!")
            else:
                print("Tie Game!")

        answer = get_response()

    if answer == "n":
        print("User's Points:", user_points)
        print("Computer's Points:", computer_points)
        if computer_points == GAME_LIMIT:
            print("Computer Wins!")
        elif computer_points > GAME_LIMIT:
            print("User Wins!")
        elif computer_points == user_points:
            print("Tie Game!")
        elif computer_points < GAME_LIMIT:
            if user_points < computer_points:
                print("Computer Wins!")
            else:
                print("User Wins!")


def roll_dice():
    user_roll = random.randint(1,3) + random.randint(1,3)
    computer_roll = random.randint(1,3) + random.randint(1,3)
    return user_roll, computer_roll

def get_response():
    response = input("Do you want to roll? (y/n): ")
    return response

main()
'''

n = int(input("nhập cấp bậc bảng cửu chương"))

# Su dung cau truc re nhanh xu ly truong hop n nam ngoai (1:9)
if n < 1 or n > 9:
    print("Chi tinh duoc bang cuu chuong 1 den 9 thoi!")
else:
    # Su dung vong lap for voi 1 <= i <= 9
    for i in range(1, 10):
        # Xuat theo dinh dang de bai yeu cau
        print("{} x {} = {}".format(n, i, n * i))
