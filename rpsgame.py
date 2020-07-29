import random
user_name = input("what is your name?: ")
print('hello {}'.format(user_name))
print('Lets play rock paper seasor')

user_input = input('choose yours: ').lower()
'''
r = str("rock")
p = str("paper")
s = str("seasor")
'''

com_input = ['rock', 'paper', 'seasor']
print(random.choice(com_input))

while user_input == "rock":
        if com_input == "rock":
            print("it is a draw")
        elif com_input == "paper":
            print("You loose")
        elif com_input == "seasor":
            print("You Win")
        break
else: print('thanks for playing')
    

'''
while user_input == "seasor":
        if com_input == "rock":
            print("You loose")
        elif com_input == "paper":
            print("You Win")
        elif com_input == "seasor":
            print("It is draw")
        break
else: print('thanks for playing')

while user_input == "paper":
        if com_input == "rock":
            print("You WIn")
        elif com_input == "paper":
            print("It is a draw")
        elif com_input == "seasor":
            print("You loose")
        break
else: print('thanks for playing')
'''
