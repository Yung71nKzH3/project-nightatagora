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

    def get_user_input(self, prompt="What do you want to do?: "):  # Prompt as parameter | Make sure to define the required data type for exception to work
        while True:
            try:
                user_input = input(prompt).lower()
                return user_input  # Return the input
            except ValueError:  # Handle errors if needed
                print("Invalid input. Please try again.")

    def run(self):
        while True:
            self.main_menu.display_main_menu()
            user_input = self.get_user_input()

            if user_input == "play" or user_input == "1" or user_input == "a" or user_input == "p":
                clear_console()
                self.game.run()
                break  # Exit the loop after valid input
            elif user_input == "settings" or user_input == "2" or user_input == "b" or user_input == "s":
                self.settings.run()
                break  # Exit the loop
            elif user_input == "exit" or user_input == "3" or user_input == "c" or user_input == "e":
                exit()
            else:
                print("\rInvalid choice. Please enter 'play', 'settings', or 'exit' (or 1, 2, or 3).", end="")  # \r and end=""
                input()  # Pause for user to read
                clear_console()  # Clear the console before redisplaying menu
        
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
        
class Intermission:
    
    def __init__(self, game):
        self.game = game
        
        self.money = 0 #TEMP
        
    def run(self): #implement intermission
        self.display_game_prep()
        input()
        
    def display_game_prep(self):
        print(" ____________________________________________________")
        print("|                                                    |")
        print(f"|    Effects|Price                     Cash:{self.money}        |")#money no matter what will require file management (Addition of saves? to allow for different/multiple playthroughs!?!?!)
        print("|----------------------------------------------------|")
        print("|                                                    |")
        print("| 1. Coffee - Increase Speed|Price                   |") #Coffee something extra but helpful in the beginning getting rid of bunches
        print("| 2. Water - Normalise|Price                         |") #Water makes everything technically normal but with everythign with disadvantage it basically is a boost
        print("| 3. Dinner - Increase Speed|Price                   |") #Food hard to make 100% and expensive but if do then POOP (big time loss) BUT food gives large increase to speed
        print("| 4.                                                 |") #
        print("| 5.                                                 |") #
        print("|____________________________________________________|")
        print("| Type: Ready | When you are ready to continue.      |")
        print("|____________________________________________________|")
        
class Game:
    
    def __init__(self,  total_handler):
        self.total_handler = total_handler
        self.intermission = Intermission(self)
        
        self.in_game = False
        
        self.place_a = "a"  # Initialize place variables
        self.place_b = "b"
        self.place_c = "c"
        self.place_d = "d"
        
        #DISHES
        self.done = 0 # Initialize dish count variables
        self.todo = 0
        #WASHING LIQUID
        self.perleftwl = "100%" # Initialize percentage variables
        #HUNGER
        self.perlefth = "100%"
        #THIRST
        self.perleftt = "100%"
        
        self.effect1 = "1" # Initialize effects variables
        self.effect2 = "2"
        self.effect3 = "3"
        self.effect4 = "4"
        
        self.user_input = ""
        
    def run(self):
        self.intermission.run()
        
    def display_game(self):
        print(" ____________________________________________________")
        print("|             Agora                  |     Stats     |")
        print("|   ______________________           |               |")
        print(f"|  |       {self.place_a}   |          |          |  Dishes {self.done}|{self.todo}   |") #A sort of system that will count on the right becoming the total uknown from the start with the amount done on the left
        print(f"|  |           |         {self.place_b}|          |  W.Liq. {self.perleftwl}  |") #A percentage result of how much Washing up liquid is left
        print(f"|  |           |    1     |______    |  Hunger {self.perlefth}  |") #Possible addition?
        print(f"|  |     3     |          |  {self.place_d}   |   |  Thirst {self.perleftt}  |") #Possible addition?
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
                clear_console()
                self.display_game()
                input()
            else:
                clear_console()
                self.run()
        
        else:
            print("bye bye")
        
#     def user_options(self):
        #decide possible user options
        
total_handler = TotalHandler()
total_handler.run()
