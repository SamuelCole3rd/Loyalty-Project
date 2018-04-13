import Points_Trade
import time
import random
import sys

print("""Hello there, welcome to the Reward Shop.
Here you can trade the number points that was generated.""")
time.sleep(4)
print("The total points that you have is...")
time.sleep(3)
print(random.randint(1000,10000))
time.sleep(2)
print("Would you like to buy something?")
answer = input().lower()
if answer == "yes":
    print("What would you like to buy?")
    time.sleep(2)
    print("Heres a list of items.")
    time.sleep(2)
    print("""Head Sets = 1000
    Mouse = 1000
    Keyboard = 2000
    Graphic Card = 3000
    Virtual Reality Headset = 4000 
    Tv = 5000
    Alienware = 7000
    PS4 = 7000
    Xbox One = 7000
    Action_Replay_Device = 8000
    Game Genie Device = 8000
    Game Shark Device = 8000
    Waifu Pillow = 9000
    Ticket to LA = 10000""")
elif answer == "no":
    quit()