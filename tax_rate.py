# Tax Rate Percentage Evaluation Program

# Import time module
import time

def green(text: str) -> str: 
    # Wrap text in ANSI codes for green color
    return f"\033[92m{text}\033[0m"

def bold(text: str) -> str: 
    # Wrap text in ANSI codes for bold formatting
    return f"\033[1m{text}\033[0m"

def tax_rate():
    initial_price = float(input(green("Initial Price: "))) or int(input("Initial Price: ")); # ask user for listed price of something
    final_price = float(input(green("Final Price: "))) or int(input("Final Price: ")); # ask user the final price paid for something after tax

    diff = final_price - initial_price # evaluate the difference between the final price after tax and the price listed

    formula = diff / initial_price * 100 # evaluate the tax percentage using this formula
    
    mes = f"The current tax rate based on your purchase is {formula}"; # create message to show user the tax rate based on their purchase
    print(green(mes + "%")); # show the user the current tax rate based on their purchase
    time.sleep(2);
    print(green(bold("(Note: This is only an estimate of the tax rate based on your purchase and \nis an oversimplification that doesn't factor in all the information necessary \nto accurately calculate the tax rate.)")));
    time.sleep(2);