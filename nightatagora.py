import os
import random
import time

def clear_console():
    os.system('cls')

class TotalHandler:
    
    def __init__(self):
        self.main_menu = MainMenu(self)
        self.game = Game(self)
        self.settings = Settings(self)
        
    def get_menu_choice(self):
        self.main_menu.display_main_menu()
        choice = self.main_menu.get_choice()
        return choice
        
    def run(self):
        choice = self.get_menu_choice()
        if choice == "play":
            clear_console()
            self.game.run()
        elif choice == "settings":
            self.settings.run()
        elif choice == "exit":
            exit()
        
class MainMenu:
    
    def __init__(self, total_handler): 
        self.total_handler = total_handler
        self.options = ["Play", "Settings", "Exit"]
        
    def display_main_menu(self):
        print(" ____________________________________________________")
        print("|                                                    |")
        print("|                                                    |")
        print("|               ┳┓•  ┓  ┏   ┏━┓                      |")
        print("|               ┃┃┓┏┓┣┓╋┃┏  ┃┗┛┏┓┏┓┏┓┏┓              |")
        print("|               ┛┗┗┗┫┛┗┗┛┛  ┗━┛┗┫┗┛┛ ┗┻              |")
        print("|                   ┛           ┛                    |")
        print("|                                                    |")
        print("|                     1. Play                        |")
        print("|                     2. Settings                    |")
        print("|                     3. Exit                        |")
        print("|                                                    |")
        print("|                                                    |")
        print("|____________________________________________________|")
        
    def get_choice(self):
        while True:  # Input validation loop
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(self.options):
                    return self.options[choice - 1].lower()
                else:
                    print(f"Invalid choice. Please enter a number between 1 and {len(self.options)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
#     def handle_choice(self, choice):
#         if choice == "play":
#             self.total_handler.game.run()  # Start the actual game
#         elif choice == "settings":
#             self.total_handler.settings.run()  # Run the options menu
#         elif choice == "exit":
#             exit()
        
class Settings:
    
    def __init__(self, total_handler):
        self.total_handler = total_handler
        
class Game:
    
    def __init__(self,  total_handler):
        self.total_handler = total_handler
        
        self.in_game = False
        
        self.place_a = "a"  # Initialize place variables
        self.place_b = "b"
        self.place_c = "c"
        self.place_d = "d"
        
        self.done = 0 # Initialize dish count variables
        self.todo = 0
        
        self.perleftwl = "100%" # Initialize percentage variables
        self.perleftsp = "100%"
        self.perleftsc = "100%"
        
        self.effect1 = "1" # Initialize effects variables
        self.effect2 = "2"
        self.effect3 = "3"
        self.effect4 = "4"
        
        self.money = 0
        
        self.user_input = ""
        
    def run(self):
        self.display_game_prep()
        self.process_game_action(self.get_user_input())
        
    def display_game_prep(self):
        print(" ____________________________________________________")
        print("|                                                    |")
        print(f"|    Effects|Price                     Cash:{self.money}        |")
        print("|----------------------------------------------------|")
        print("|                                                    |")
        print("| 1. Coffee - Increase efficency|Price               |")
        print("| 2. Water - Normalise BUT toilet|Price              |")
        print("| 3.                                                 |")
        print("| 4.                                                 |")
        print("| 5.                                                 |")
        print("|____________________________________________________|")
        print("| Type: Ready | When you are ready to continue.      |")
        print("|____________________________________________________|")
        
    def display_game(self):
        print(" ____________________________________________________")
        print("|             Agora                  |     Stats     |")
        print("|   ______________________           |               |")
        print(f"|  |       {self.place_a}   |          |          |  Dishes {self.done}|{self.todo}   |") #A sort of system that will count on the right becoming the total uknown from the start with the amount done on the left
        print(f"|  |           |         {self.place_b}|          |  W.Liq. {self.perleftwl}  |") #A percentage result of how much Washing up liquid is left
        print(f"|  |           |    1     |______    |  Sponge {self.perleftsp}  |") #Possible addition?
        print(f"|  |     3     |          |  {self.place_d}   |   |  Scrubb {self.perleftsc}  |") #Possible addition?
        print("|  |           |___   ____|      |   |_______________|")
        print("|  |                      |      |   |    Effects    |")
        print(f"|  |___________|          |  4   |   |  {self.effect1}            |") 
        print(f"|  |                      |      |   |  {self.effect2}            |") #Coffee? After a while begin to crash
        print(f"|              2    {self.place_c}            |   |  {self.effect3}            |") #Free Food/Drink
        print(f"|  |______________________|______|   |  {self.effect4}            |") #Water if no water effect things will take longer to complete no matter the task
        print("|____________________________________|_______________|") #Require the toilet
        print(" What do you want to do?:")                             #Such issues etc. will be displayed here in the effect menu.
        print(".Option A") #Only showing options relevant possible. Secret options always possible TEMP
        print(".Option B")
        print(".Option C")
        
    def get_user_input(self):
        self.user_input = input("What do you want to do?: ")
        return self.user_input.lower()
    
    def process_game_action(self, user_input):
        if self.in_game == False:
            if user_input == "ready":
                print("TEST")
                input()
        
        else:
            print("bye bye")
            
        
        
        
#     def user_options(self):
        #decide possible user options
        
total_handler = TotalHandler()
total_handler.run()
