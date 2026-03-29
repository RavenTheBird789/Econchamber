# Economic Systems List

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

# Capitalism Definition
def capitalism():
    os.system('clear');
    cap_def = "Capitalism is an economic system characterized by private ownership of the means of production and the creation of goods or services for profit. \nIn a capitalist economy, individuals and businesses operate in a competitive market, where prices are determined by supply and demand. \nThe role of the government is typically limited to regulation and protection of property rights."
    print(green(cap_def));

# Socialism Definition
def socialism():
    os.system('clear');
    soc_def = "Socialism is an economic system where the means of production, distribution, and exchange are owned or regulated by the community as a whole, \noften through the government regulating the distribution of resources and wealth."
    print(green(soc_def));

# Communism Definition
def communism():
    os.system('clear');
    com_def = "Communism is a political and economic ideology advocating for a classless society in which all property and resources are communally owned, \nwith the aim of eliminating social inequalities and ensuring that wealth and power are distributed equally among all members of society."
    print(green(com_def));

# Mixed Economy Definition
def mixed_economy():
    os.system('clear');
    mix_def = "A mixed economy is an economic system that combines elements of both capitalism and socialism. \nIn a mixed economy, private enterprises operate alongside government intervention and regulation, \nallowing for a balance between market forces and social welfare."
    print(green(mix_def));

# Traditional Economy Definition
def traditional_economy():
    os.system('clear');
    trad_def = "A traditional economy is an economic system that relies on customs, traditions, and beliefs to shape the production and distribution of goods and services. \nIn a traditional economy, economic decisions are often based on historical practices and cultural norms, \nwith a focus on subsistence farming, hunting, and gathering."
    print(green(trad_def));

# Command Economy Definition
def command_economy():
    os.system('clear');
    cmd_def = "A command economy is an economic system where the government or central authority makes all decisions regarding the production and distribution of goods and services. \nIn a command economy, the government typically owns and controls the means of production, \nand economic activities are planned and directed by the state."
    print(green(cmd_def));

# Market Economy Definition
def market_economy():
    os.system('clear');
    mark_def = "A market economy is an economic system where economic decisions and the pricing of goods and services are guided by the interactions of citizens and businesses in a free market. \nIn a market economy, supply and demand determine production and distribution, with minimal government intervention."
    print(green(mark_def));

def list():
    econ_systems = [
       "List of Economic Systems",
     "----------------------------",        
        "1. Capitalism",
        "2. Socialism",
        "3. Communism",
        "4. Mixed Economy",
        "5. Traditional Economy",
        "6. Command Economy",
        "7. Market Economy",
        "8. Exit",
    ]
    for system in econ_systems:
        print(green(system));
    dec = input(green("Which economic system would you like to learn about?: "));
    if dec == '1':
        os.system('clear');
        capitalism();
        time.sleep(1);
        Uques();
    elif dec == '2':
        os.system('clear');
        socialism();
        time.sleep(1);
        Uques();
    elif dec == '3':
        os.system('clear');
        communism();
        time.sleep(1);
        Uques();
    elif dec == '4':
        os.system('clear');
        mixed_economy();
        time.sleep(1);
        Uques();
    elif dec == '5':
        os.system('clear');
        traditional_economy();
        time.sleep(1);
        Uques();
    elif dec == '6':
        os.system('clear');
        command_economy();
        time.sleep(1);
        Uques();
    elif dec == '7':
        os.system('clear');
        market_economy();
        time.sleep(1);
        Uques();
    elif dec == '8':
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
