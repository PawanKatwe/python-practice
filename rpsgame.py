from random import randint

user_name = input("what is your name?: ")
print('hello {}'.format(user_name))
print('Lets play rock paper scissor')
print("choose yors from rock,paper or scissor")     
print("you can say 'quit' to stop game anytime")

t=['rock','paper','scissor']




player_r="false"

while player_r=="false":
        computer=t[randint(0,2)]
        player=input("rock,paper,scissor?: ").lower()

        if player==computer:
                print("Tie!")
        elif player=="rock":
                if computer=="paper":
                        print("You lose!",computer,"covers",player)
                else:
                        print("You win!",player,"smashes",computer)
        elif player=="paper":
                if computer=="scissor":
                        print("You lose!",computer,"cut",player)
                else:
                        print("You win!",player,"covers",computer)
        elif player=="scissor":
                if computer=="Rock":
                        print("You lose...",computer,"smashes",player)
                else:
                        print("You win!",player,"cut",computer)
        elif player=="quit":
                print("thanks for playing the game")
                break
        else:
                print("That's not a valid play.Check your spelling!")


