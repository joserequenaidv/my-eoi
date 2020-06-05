'''Script modules'''
import random

#PLAYER 1
player1 = int(input('Rock, paper, scissors, lizard or spock?\n> Rock = 1\n> Paper = 2\n> Scissors = 3\n> Lizard = 4\n> Spock = 5\n'))

def player1_prints(player1):
    '''Print player1's choice'''
    if player1 == 1:
        print("\nPlayer 1: Rock")
    elif player1 == 2:
        print("\nPlayer 1: Paper")
    elif player1 == 3:
        print("\nPlayer 1: Scissors")
    elif player1 == 4:
        print("\nPlayer 1: Lizard")
    elif player1 == 5:
        print("\nPlayer 1: Spock")

player1_prints(player1)

#CPU
cpu = random.randint(1,5)

def cpu_prints(cpu):
    '''Print CPU's random choice'''
    if cpu == 1:
        print("\nCPU: Rock")
    elif cpu == 2:
        print("\nCPU: Paper")
    elif cpu == 3:
        print("\nCPU: Scissors")
    elif cpu == 4:
        print("\nCPU: Lizard")
    elif cpu == 5:
        print("\nCPU: Spock")

cpu_prints(cpu)

#Script Logic
while player1 == cpu:
    '''If there is a draw, the game runs again'''
    print("\nDRAW.")
    print("\nCHOOSE AGAIN!")
    cpu = random.randint(1,5)
    player1 = int(input('Rock, paper, scissors, lizard or spock?\n> Rock = 1\n> Paper = 2\n> Scissors = 3\n> Lizard = 4\n> Spock = 5\n'))
    player1_prints(player1)
    cpu_prints(cpu)
    if player1 != cpu:
        continue
else:
    if player1 == 1 and cpu == 2:
        print("\nPaper covers Rock.\nCPU WINS.")
    elif player1 == 1 and cpu == 5:
        print("\nSpock vaporizes Rock.\nCPU WINS.")
    elif player1 == 2 and cpu == 3:
        print("\nScissors cuts Paper.\nCPU WINS.")
    elif player1 == 2 and cpu == 4:
        print("\nLizard eats Paper.\nCPU WINS.")
    elif player1 == 3 and cpu == 1:
        print("\nRock crushes Scissors.\nCPU WINS.")
    elif player1 == 3 and cpu == 5:
        print("\nSpock smashes Scissors.\nCPU WINS.")
    elif player1 == 4 and cpu == 1:
        print("\nRock crushes Lizard.\nCPU WINS.")
    elif player1 == 4 and cpu == 3:
        print("\nScissors decapitates Lizard.\nCPU WINS.")
    elif player1 == 5 and cpu == 2:
        print("\nPaper disproves Spock.\nCPU WINS.")
    elif player1 == 5 and cpu == 4:
        print("\nLizard poisons Spock.\nCPU WINS.")
    elif player1 == 2 and cpu == 1:
        print("\nPaper covers Rock.\nYOU WIN.")
    elif player1 == 5 and cpu == 1:
        print("\nSpock vaporizes Rock.\nYOU WIN.")
    elif player1 == 3 and cpu == 2:
        print("\nScissors cuts Paper.\nYOU WIN.")
    elif player1 == 4 and cpu == 2:
        print("\nLizard eats Paper.\nYOU WIN.")
    elif player1 == 1 and cpu == 3:
        print("\nRock crushes Scissors.\nYOU WIN.")
    elif player1 == 5 and cpu == 3:
        print("\nSpock smashes Scissors.\nYOU WIN.")
    elif player1 == 1 and cpu == 4:
        print("\nRock crushes Lizard.\nYOU WIN.")
    elif player1 == 3 and cpu == 4:
        print("\nScissors decapitates Lizard.\nYOU WIN.")
    elif player1 == 2 and cpu == 5:
        print("\nPaper disproves Spock.\nYOU WIN.")
    elif player1 == 4 and cpu == 5:
        print("\nLizard poisons Spock.\nYOU WIN.")
