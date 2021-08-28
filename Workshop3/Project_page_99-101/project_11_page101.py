"""
Author: Trần Đình Hoàng
Date: 19/07/2021
Program: project_11_page101.py
Problem:
    11. In the game of Lucky Sevens, the player rolls a pair of dice. If the dots add up to 7, the player wins $4;
        otherwise, the player loses $1. Suppose that, to entice the gullible, a casino tells players that there are
        lots of ways to win: (1, 6), (2, 5), and so on. A little mathematical analysis reveals that there are not
        enough ways to win to make the game worthwhile; however, because many people’s eyes glaze over at the first
        mention of mathematics, your challenge is to write a program that demonstrates the futility of playing the game.
        Your program should take as input the amount of money that the player wants to put into the pot, and play the
        game until the pot is empty. At that point, the program should print the number of rolls it took to break the
        player, as well as maximum amount of money in the pot.

Solution:
    Display result:
        Enter the amount you want to bet: 5

            Turn     Result     Bets     Total money
               1       Lose       -1               4
               2       Lose       -1               3
               3       Lose       -1               2
               4       Lose       -1               1
               5        Win       +4               5
               6       Lose       -1               4
               7       Lose       -1               3
               8       Lose       -1               2
               9       Lose       -1               1
              10       Lose       -1               0

"""
import random

money = int(input("Enter the amount you want to bet: "))
maxMoney = money

print("\n%8s %10s %8s %15s" % ("Turn", "Result", "Bets", "Total money"))

turn = 0
while maxMoney > 0:
    dice01 = random.randint(1, 6)
    dice02 = random.randint(1, 6)
    
    sumDice = dice01 + dice02
    # print(dice01, dice02, sumDice)
    turn += 1
    if sumDice == 7:
        maxMoney += 4
        print("%8s %10s %8s %15s" % (turn, "Win", "+4", maxMoney))
    else:
        maxMoney -= 1
        print("%8s %10s %8s %15s" % (turn, "Lose", "-1", maxMoney))

    

