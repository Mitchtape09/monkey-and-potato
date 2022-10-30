import random

mitch = 0
taylor = 0

options = ["monkey", "potato"]

while True:
    user_input = input("Type monkey or potato or q to quit: ")
    if user_input == "q":
        break

    if user_input in ["monkey", "potato"]:

        random_number = random.randint(0, 1)
        # money: 0, potato: 1

    taylor_pick = options[random_number]
    print("taylor picked", taylor_pick + "!")

    if user_input == "monkey" and taylor_pick == "monkey":
        print("Two monkeys are bananas")

    if user_input == "monkey" and taylor_pick == "potato":
        print("Your monkey throws the potato, great job!!")

    if user_input == "potato" and taylor_pick == "potato":
        print("Two potatoes are just silly")
    if user_input == "potato" and taylor_pick == "money":
        print("Taylors monkey throws your potato, didn't do good")
