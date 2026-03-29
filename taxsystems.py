# Tax Systems List

# Import OS module
import os

# Import time module
import time

def green(text: str) -> str: 
    # Wrap text in ANSI codes for green color
    return f"\033[92m{text}\033[0m"

# User question
def Uques():
    user_ques = input(green("Would you like to learn more? (yes/no): "))
    if user_ques.lower() in ("yes", "y"):
        list()
    elif user_ques.lower() in ("no", "n"):
        print(green("Okay then, thanks for taking the time to learn!"))

# Progressive Tax Definition
def progressive_tax():
    os.system('clear');
    prog_def = "A progressive tax is a tax system in which the tax rate increases as the taxable amount increases. \nIn this system, individuals or entities with higher incomes are taxed at higher rates compared to those with lower incomes. \nThe goal of a progressive tax is to reduce income inequality by placing a larger tax burden on those who have a greater ability to pay."
    print(green(prog_def));

# Regressive Tax Definition
def regressive_tax():
    os.system('clear');
    reg_def = "A regressive tax is a tax system in which the tax rate decreases as the taxable amount increases. \nIn this system, individuals or entities with lower incomes pay a higher percentage of their income in taxes compared to those with higher incomes. \nRegressive taxes can disproportionately affect low-income individuals, as they take a larger share of their income."
    print(green(reg_def));

# Flat Tax Definition
def flat_tax():
    os.system('clear');
    flat_def = "A flat tax is a tax system in which a single constant tax rate is applied to all levels of income or taxable amount. \nIn this system, everyone pays the same percentage of their income in taxes, regardless of their income level. \nFlat taxes are often praised for their simplicity and ease of administration, but they can also be criticized for potentially placing a heavier burden on lower-income individuals."
    print(green(flat_def));

# Sales Tax Definition
def sales_tax():
    os.system('clear');
    sales_def = "A sales tax is a consumption tax imposed by the government on the sale of goods and services. \nIt is typically calculated as a percentage of the purchase price and is collected by the retailer at the point of sale. \nSales taxes are commonly used to generate revenue for governments and can vary in rate depending on the jurisdiction and type of goods or services being sold."
    print(green(sales_def));

# Property Tax Definition
def property_tax():
    os.system('clear');
    prop_def = "A property tax is a tax levied on real estate or personal property by the government. \nIt is typically based on the assessed value of the property and is paid by the property owner. \nProperty taxes are commonly used to fund local government services such as schools, infrastructure, and public safety."
    print(green(prop_def));

def list():
    tax_systems = [
     "   List of Tax Systems   ",
     "-------------------------",
     "1. Progressive Tax",
     "2. Regressive Tax",
     "3. Flat Tax",
     "4. Sales Tax",
     "5. Property Tax",
     "6. Exit",
    ]
    for system in tax_systems:
        print(green(system));
    dec = input(green("Which tax system would you like to learn about?: "));
    if dec == '1':
        os.system('clear');
        progressive_tax();
        time.sleep(1);
        Uques();
    elif dec == '2':
        os.system('clear');
        regressive_tax();
        time.sleep(1);
        Uques();
    elif dec == '3':
        os.system('clear');
        flat_tax();
        time.sleep(1);
        Uques();
    elif dec == '4':
        os.system('clear');
        sales_tax();
        time.sleep(1);
        Uques();
    elif dec == '5':
        os.system('clear');
        property_tax();
        time.sleep(1);
        Uques();
    elif dec == '6':
        os.system('clear');
    else:
        os.system('clear');
        print(green("Invalid option selected. Please choose a valid tax system number in: "));
        time.sleep(1);
        print(green("...3"))
        time.sleep(1);
        print(green("...2"))
        time.sleep(1);
        print(green("...1"))
        time.sleep(1);
        os.system('clear');
        list();
