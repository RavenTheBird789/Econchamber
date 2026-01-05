# Econchamber Source Code

# Import os module
import os

# Import time module
import time

# Import list of different economic systems
import econsystems

# Import list of different tax systems
import taxsystems

# Econchamber Tax Rate Formula Import
import tax_rate

# Econchamber US Debt Clock Import
import US_Debt_Clock  # type: ignore

def green(text: str) -> str: 
    # Wrap text in ANSI codes for green color
    return f"\033[92m{text}\033[0m"

def bold(text: str) -> str: 
    # Wrap text in ANSI codes for bold formatting
    return f"\033[1m{text}\033[0m"

# Definition of Economics
def econ_def():
    econ_def = "Economics is the social science that studies the production, distribution, and consumption of goods and services. \nIt focuses on how individuals, businesses, governments, and nations make choices about allocating resources to satisfy their needs and wants."
    print(green(econ_def));

# Prompt user to return to main menu or exit
def user_prompt():
    prompt = input(green("Would you like to return to the main menu? (yes/no): "));
    if prompt.lower() in ['yes', 'y']:
        os.system('clear');
        options();
    elif prompt.upper() in ['YES', 'Y']:
        os.system('clear');
        options();
    elif prompt == 'Yes':
        os.system('clear');
        options();
    elif prompt.lower() in ['no', 'n']:
        os.system('clear');
        print(green("Thank you for visiting the Econchamber! Goodbye!"));
        os.close(fd=0);
    elif prompt.upper() in ['NO', 'N']:
        os.system('clear');
        print(green("Thank you for visiting the Econchamber! Goodbye!"));
        os.close(fd=0);
    elif prompt == 'No':
        os.system('clear');
        print(green("Thank you for visiting the Econchamber! Goodbye!"));
        os.close(fd=0);
    else:
        os.system('clear');
        print(green("Thank you for visiting the Econchamber! Goodbye!"));
        os.close(fd=0);

def main():
    # Money Symbol
    money = " $ "

    # Construct Econchamber Art
    art = [
        "  ___   ___   ____         ___         ___            ___   ___  ___",
        " |     |     |    | |\\  | |    |    | |   | |\\    /| |   | |    |___| ",
        " |---  | $   |    | | \\ | | ¢  |----| |---| | \\  / | |---  |--- |  \\",
        " |___  |___  |____| |  \\| |___ |    | |   | |  \\/  | |___| |___ |   \\",
    ]
    
    # Opening statement
    opening_statement = "Welcome to the Econchamber! Where economic information and education echos endlessly. \n Please choose an option below:"
    
    # Print the artwork in green, then opening statement in green and bold
    print()
    for line in art:
        print(green(line))
    print()
    print((bold(green(money))) + (green(opening_statement)))
    print()
if __name__ == "__main__":
    main();

# Options displayed in green
def options():
    opts = [
        "            $ Options             ",
        "-----------------------------------",
        "1. What is economics?",
        "2. Find tax rate percentage after a purchase",
        "3. View different tax systems",
        "4. View different economic systems",
        "5. View the U.S. Debt Clock",
        "6. Exit Econchamber",
    ]
    for opt in opts:
        print(green(opt));
    user_choice = input(green("Please enter the number of your choice: "));

    # Handles user choice
    if user_choice == '1':
        os.system('clear');
        econ_def();
        time.sleep(1);
        user_prompt();
    elif user_choice == '2':
        os.system('clear');
        tax_rate.tax_rate();
        user_prompt();
    elif user_choice == '3':
        os.system('clear');
        taxsystems.list();
        user_prompt();
    elif user_choice == '4':
        os.system('clear');
        econsystems.list();
        user_prompt();
    elif user_choice == '5':
        os.system('clear');
        US_Debt_Clock.main();
        user_prompt();
    elif user_choice == '6':
        os.system('clear');
        print(green("Thank you for visiting the Econchamber! Goodbye!"));
        time.sleep(5);
        os.system('clear');
        os.close(fd=0);
    else:
        os.system('clear');
        print(green("Invalid choice. Please try again in: "));
        time.sleep(1);
        print(green("...3"))
        time.sleep(1);
        print(green("...2"))
        time.sleep(1);
        print(green("...1"))
        time.sleep(1);
        os.system('clear');
        options(); # Message displayed to user if they enter an invalid choice and returns them to the main screen
options();
