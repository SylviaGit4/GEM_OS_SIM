import random
import os
import time
import sympy as sp

#Very Basic Text Based OS in python.
#Commands List:
# -help : Provides list of commands.

#Username & Password
username = "user"
password = "pass1"

#Simulated 'files'. Add dictionary entries here for persistence.
simFiles = {
    "system": ["runtime|theme.txt|sysreset"],
    "devInfo": ["GemOS.txt"],
    "notepad": ["Blank..."],
}

loggedIn = False
#Boot & Login
print("Booting GemOS V1.0.0 \n")
time.sleep(2)
while loggedIn == False:
    login1 = input("Username: ")
    login2 = input("Password: ")
    if login1 != username or login2 != password:
        time.sleep(1)
        print("Incorrect Username or Password. Try again. \n")
    else:
        time.sleep(1)
        print("Login successful. Welcome to GemOS V1.0.0 ALPHA BUILD\n")
        loggedIn = True


# Display login message
print("Type 'help' for list of commands.")
print(username + ": GemOS V1.0.0")

# Define functions/commands

# -help
def help_command():
    print(""" -help : Provides List of Commands.
 -calc : Opens calculator 'program' for simple inputs.
 -shutdown : Shuts down the OS. 
 -fileM : Opens the file management system. 
 -fileL : Lists files.
 -ErieFetch : Outputs device info.
 -RockPaperScissors : Rock paper scissors game!
 -clr : Clears the terminal.""")

# -calc (example calculator program)
def calc():
    while True:
        expression =  input("Calculator (type 'exit' to quit): ")
        if expression.lower() == 'exit':
            break
        try:
            result = sp.sympify(expression)
            print(f"Result: {result}")
        except Exception as e:
            print("Error:", e)

# -shutdown
def shutdown():
    global loggedIn
    loggedIn = False
    print("Shutting down...")
    time.sleep(2)

# -file manager (read/write)
def file_cmd():
    print("| GemOS V1.0.0 File Manager |")
    while True:
        action = input("Would you like to read or write files, or exit the file manager: ").lower()

        if action == "exit":
            print("Exitting...")
            time.sleep(1)
            break

        elif action == "read":
            while True:
                fileSelect = input("What file would you like to select: ")
                if fileSelect in simFiles:
                    output = simFiles.get(fileSelect)
                    print("-",output)
                    time.sleep(2)
                    break
                else:
                    print("File Not Found.")
                    time.sleep(1)
                    break

        elif action == "write":
            while True:
                fileName = input("What would you like to name the file: ")
                fileContent = input("Content to be written: ")
                simFiles.update({fileName: fileContent})
                time.sleep(1)
                print("File Written.")
                time.sleep(0.5)
                break

        else:
            print("Invalid command.")


# -list files
def list_files():
    print("Listing all files.")
    time.sleep(0.5)
    for files in simFiles.keys():
        print("-",files) 

# -Neofetch Esque command.
def erie_fetch():
    memUse = random.randint(1,1024)
    cpuUse = random.randint(1,100)
    gpuUse = random.randint(1,100)
    print(f""" .................... user@GemOS
 .........@@......... -----------------
 ......@@@.@@@=...... OS: GemOS_v1.0.0 ALPHA
 .....@.@...@.@...... Terminal: GemKonsole
 .....@.@...@.@...... Kernel: Genux 1.0.0 
 .....@.@...@.@...... CPU: WM01A Core | {cpuUse}% Usage
 .....@.@...@.@...... GPU: WGrphcs02I | {gpuUse}% Usage
 .......@@.@@........ Memory: {memUse}MiB / 1024MiB
 .................... """)
    
# - Rock paper scissors
def rock_paper_scissors():
    time.sleep(0.5)
    print("Loading rock_paper_scissors.exe...")
    while True:
        time.sleep(1)
        print("""\n ~ Rock Paper Scissors! ~
 Pick between rock, paper and scissors.
 Rock trumps Scissors, Scissors trumps Paper and Paper trumps Rock.\n""")

        print(" Rock.")
        time.sleep(1)
        print(" Paper.")
        time.sleep(1)
        print(" Scissors.")
        time.sleep(1)
        playerChoice = input(" Shoot! ").lower()
        
        time.sleep(2)
        compChoice = random.randint(1,3)
        # 1 = Rock, 2 = Paper, 3 = Scissors.

        if compChoice == 1:
            if playerChoice == "rock":
                print(" Computer chose [ROCK], tie.")
            elif playerChoice == "paper":
                print(" Computer chose [ROCK], Player wins!")
            elif playerChoice == "scissors":
                print(" Computer chose [ROCK], Computer wins!")
            else:
                print(" Invalid input, Computer chose [ROCK], Computer wins!")
        
        if compChoice == 2:
            if playerChoice == "paper":
                print(" Computer chose [PAPER], Tie.")
            elif playerChoice == "scissors":
                print(" Computer chose [PAPER], Player wins!")
            elif playerChoice == "rock":
                print(" Computer chose [PAPER], Computer wins!")
            else:
                print(" Invalid input, Computer chose [PAPER], Computer wins!")

        if compChoice == 3:
            if playerChoice == "scisssors":
                print(" Computer chose [SCISSORS], Tie.")
            elif playerChoice == "paper":
                print(" Computer chose [SCISSORS]s, Player wins!")
            elif playerChoice == "rock":
                print(" Computer chose [SCISSORS], Computer wins!")
            else:
                print(" Invalid input, Computer chose [SCISSORS], Computer wins!")

        playAgain = input("\n Type 'exit' to quit, or anything else to play again. ").lower()
        if playAgain == "exit":
            break
        else:
            print(" Playing again.")

# Clears the terminal.
def clear_terminal():
    print("Clearing...")
    time.sleep(0.5)
    os.system('cls')
    
# Dictionary to map commands to functions
commands = {
    'help': help_command,
    'calc': calc,
    'shutdown': shutdown,
    'fileM': file_cmd,
    'fileL': list_files,
    'ErieFetch': erie_fetch,
    'RockPaperScissors': rock_paper_scissors,
    'clr': clear_terminal,
}

# Main loop
while loggedIn:
    cmd = input(username + ": ")
    # Check if the command exists in the dictionary and call the function
    if cmd in commands:
        commands[cmd]()
    else:
        print("Command not found. Type 'help' for a list of commands.")