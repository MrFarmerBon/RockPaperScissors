import random
from colorama import Fore, Style
game = "yes"
options = [ "rock","paper","scissors"]









def win ():
    print(Fore.GREEN + "Well Done You win!")
#what happens when you lose
def lose ():

    print(Fore.RED + "Unlucky! You lose")
#what happens when you draw
def draw():
    print("Its A Draw!")
#defining a win or a lose
def win_lose (userInput,computerInput):
    if userInput == "rock" and computerInput == "scissors" :
        #user win
        win()
    if userInput =="scissors" and computerInput == "paper":
        #user win
        win()
    if userInput =="paper" and computerInput == "rock":
        #user win
        win()
    if userInput == "scissors" and computerInput == "rock" :
        #user lose
        lose()
    if userInput =="paper" and computerInput == "scissors":
        #user lose
        lose()
    if userInput =="rock" and computerInput == "paper":
        #user lose
        lose()
    if userInput == computerInput:
        draw()
#draw icons
def icons(input):
    if input == "rock":
        print("______               _    ")
        print("| ___ \             | |   ")
        print("| |_/ /  ___    ___ | | __")
        print("|    /  / _ \  / __|| |/ /")
        print("| |\ \ | (_) || (__ |   < ")
        print("\_| \_| \___/  \___||_|\_/")
        print("                                 ")
    if input == "paper":
        print("______                           ")
        print("| ___ \                          ")
        print("| |_/ /  __ _  _ __    ___  _ __ ")
        print("|  __/  / _` || '_ \  / _ \| '__|")
        print("| |    |__/| |    (_| || |_) ||  ")
        print("\_|     \__,_|| .__/  \___||_|   ")
        print("              | |                ")
    if input == "scissors":
        print(" _____        _                             ")
        print("/  ___|      (_)                            ")
        print("\ `--.   ___  _  ___  ___   ___   _ __  ___ ")
        print(" `--. \ / __|| |/ __|/ __| / _ \ | '__|/ __|")
        print("/\__/ /| (__ | |\__ \u005c__ \| (_) || |   \__ \u005c")
        print("\____/  \___||_||___/|___/ \___/ |_|   |___/")
        print("                                             ")

#main loop   
def play():

    computerInput =random.choice(options)
    userInput = input(Style.RESET_ALL+"What do you Choose! ")
    if userInput in options:
        print("Great!")
        proceed = input()
        icons(userInput)
        proceed == input()
        print(Style.BRIGHT + " VS" )
        proceed == input()
        icons(computerInput)
        proceed = input()
        win_lose(userInput,computerInput)
        proceed=input()
    else:
        print(Fore.RED + Style.BRIGHT+"Unknown Input Detected!")
        game =input(Fore.RESET+"Would you like to play again: ")




print(Fore.RESET + Style.BRIGHT+ "Welcome to Rock Paper Scissors!")

while game == "yes":
    play()
    game =input(Fore.RESET+"Would you like to play again: ")


print(Fore.RED +"Goodbye!")
exit()



