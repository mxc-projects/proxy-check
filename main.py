import os, sys, time, json, random, threading, requests
from colorama import Fore, Style, init
from prettytable import PrettyTable
import platform
# Initialize colorama for cross-platform compatibility

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def re(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.001)  
        
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'
print(f"{lrd}")
t = PrettyTable([f'{cn}Number{lrd}', f'{cn}Method{lrd}'])
t.add_row([f'{lgn}1{lrd}', f'{gn}Report Spam{lrd}'])
t.add_row([f'{lgn}2{lrd}', f'{gn}Report Pornography{lrd}'])
t.add_row([f'{lgn}3{lrd}', f'{gn}Report Violence{lrd}'])
t.add_row([f'{lgn}4{lrd}', f'{gn}Report Child Abuse{lrd}'])
t.add_row([f'{lgn}5{lrd}', f'{gn}Report Other{lrd}'])
t.add_row([f'{lgn}6{lrd}', f'{gn}Report Copyright{lrd}'])
t.add_row([f'{lgn}7{lrd}', f'{gn}Report Fake{lrd}'])
t.add_row([f'{lgn}8{lrd}', f'{gn}Report Geo Irrelevant{lrd}'])
t.add_row([f'{lgn}9{lrd}', f'{gn}Report Illegal Drugs{lrd}'])
t.add_row([f'{lgn}10{lrd}', f'{gn}Report Personal Details{lrd}'])

account = f"""{k}
                                                                 
                    .---:                :---.                   
               .=++*+=+#+                +#*=+*++=.              
             =#*+++=++-=#                #==++=+++*#=            
           =%++**==**-*+#=              =#+*-**==**++%=          
         .#*+***=+**-*+##+.            .+*%+*-**+=***+*%:        
        -%=****-***=+*=%@+=            =+@%=*+=***-****=%-       
       -%=****-****-***++@#.          .#@++***-****-****=%-      
      .%=****=+***+=****-=%@=*:=#%=.*=@%=-****=+***+=****=%.     
      *+*****-****=*****-+=#%*%#@@#%*%#=+-*****=****-*****=#     
     .%=****=+****-*-..::%@@@+@@@@@@*@@@%-:..-*-****+=****=#.    
     ++*****-*+-:::.    @@@@@*%@@@@%*@@@@@    .:::-+*-*****++    
     *=***++-=         :@@@@@@##@@##@@@@@@:         =-++***=#    
     *=+:               %@@%#@@@##@@@##@@%               :+=#    
     +-            .... =@@@+@@@@@@@@+@@@= ....            -*    
     =          *@@@@@@@+@@@=@@@@@@@@=@@@+@@@@@@@*          =    
               :@@@@@@@@+@@%##%@@@@@###@@+@@@@@@@@:              
               .@@@@##%@+@@%*@@@@@@@@*%@@+@%##@@@@.              
                .*@@@@%#*+@@#%@@@@@@%#@@+*#%@@@@#:               
                  .=#@@@@*%@@-*+--+*-@@%*@@@@#=.                 
                      :=*@+@@:.    .-@@+@#=:                     
                          #*@=      =@*#                         
                         :%=@+      +@=%:                        
                       +****%*+=  =+*%****+                      
                        .-.=-        -=.-.                       

    {lrd}{lrd}[{lgn}+{lgn}] Auto proxy checker for combo-list{k} {lrd}[{lgn}+{lgn}]
    {lrd}------------------------------------------------------------- \n 
    {lrd}[{lgn}+{lrd}] {gn}Contact:{lgn}@mxc-projects{lrd} \n
    {lrd}[{lgn}+{lrd}] {gn}GitHub: 
    {lgn}https://github.com/mxc-projects{lrd} \n
    {lrd}[{lgn}+{lrd}] {gn}Telegram: {lgn}@mxc_projects{lrd} \n
    {lrd}[{lgn}+{lrd}] {gn}YouTube: 
    {lgn}https://www.youtube.com/@mxc-projects{lrd} \n
    {lrd}[{lgn}+{lrd}] {gn}Discord: 
    {lgn}https://discord.gg/8f2b3a5c{lrd} \n \n
    \n ------------------------------------------------------------- \n  """	 

if 'Windows' in platform.system():
    try:
        from colorama import init
    except ImportError:
        os.system("pip install colorama")
        
def print_welcome():
    clear_screen()
    time.sleep(3)
    print(account)
    print(f"{Style.BRIGHT}{Fore.GREEN}WELCOME TO PROXY CHECKER!{Style.RESET_ALL}")
    print('\n') 
    print(f"{Fore.GREEN}This tool checks the status of proxies from 'input.txt'.")
    print(f"{Fore.GREEN}Please ensure 'input.txt' is in the same directory as this script. name it as 'input.txt'. \n ")
    input(f"{Style.BRIGHT}{Fore.GREEN}Press Enter to continue...{Style.RESET_ALL}")    
    print(f"{Style.DIM}{Fore.GREEN}{'-'*74}{Style.RESET_ALL}")
    time.sleep(2)
    print(f"{Style.BRIGHT}{Fore.GREEN}Thank you for using Proxy Checker!{Style.RESET_ALL} {Style.BRIGHT}{Fore.RED}by mxc-projects ;){Style.RESET_ALL}")
    time.sleep(2)
    clear_screen()
    

print_welcome()

def files_check():
    if not os.path.exists("input.txt"):
        print(f"{Style.BRIGHT}{Fore.RED}ERROR: 'input.txt' file not found!{Style.RESET_ALL}")
        sys.exit(1)
    with open("input.txt", "r") as file:
        lines = file.readlines()
    if not lines:
        print(f"{Style.BRIGHT}{Fore.RED}ERROR: 'input.txt' is empty!{Style.RESET_ALL}")
        sys.exit(1)
    return [line.strip() for line in lines if line.strip()]

def load_proxies():
    print(f"{Style.BRIGHT}{Fore.GREEN}Loading proxies from 'input.txt'...{Style.RESET_ALL}")
    proxies = files_check()
    if not proxies:
        print(f"{Style.BRIGHT}{Fore.RED}ERROR: No valid proxies found in 'input.txt'!{Style.RESET_ALL}")
        sys.exit(1)
    return proxies

def test_proxy(proxy):
    requests.packages.urllib3.disable_warnings()
    try:
        response = requests.get("https://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
        if response.status_code == 200:
            return {"proxy": proxy, "status": "alive", "latency": round(response.elapsed.total_seconds() * 1000, 2)}
        else:
            return {"proxy": proxy, "status": "dead", "latency": None}
    except requests.RequestException:
        return {"proxy": proxy, "status": "dead", "latency": None}



def check_proxies(proxies):

    clear_screen()
    print(f"{Style.BRIGHT}{Fore.GREEN}Checking proxies...{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.GREEN}Total proxies to check: {len(proxies)}{Style.RESET_ALL}")

    time.sleep(1)
    results = []
    threads = []
    tick_count = 0

    def worker(proxy):
        result = test_proxy(proxy)
        results.append(result)

    for proxy in proxies:
        thread = threading.Thread(target=worker, args=(proxy,))
        threads.append(thread)
        thread.start()
        tick_count += 1
        if tick_count % 10 == 0:
            print(f"{Style.BRIGHT}{Fore.GREEN}Checked {tick_count} proxies so far...{Style.RESET_ALL}")
            print(f"{Fore.GREEN}{'-'*47}{Style.RESET_ALL}")
            time.sleep(0.01)
            clear_screen()
            if tick_count % 100 == 0:
                clear_screen()
    print(f"{Style.BRIGHT}{Fore.GREEN}Waiting for all threads to finish...{Style.RESET_ALL}")

    for thread in threads:
        thread.join()

    print(f"{Style.BRIGHT}{Fore.GREEN}Proxy check completed.{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'-'*47}{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.GREEN}Total proxies checked: {len(results)}{Style.RESET_ALL}")
    clear_screen()
    print(f"{Fore.GREEN}{'-'*59}{Style.RESET_ALL}")
    alive_count = sum(1 for r in results if r["status"] == "alive")
    dead_count = sum(1 for r in results if r["status"] == "dead")
    print(f"{Style.BRIGHT}{Fore.GREEN}Alive proxies: {alive_count}{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.RED}Dead proxies: {dead_count}{Style.RESET_ALL}")
    if alive_count == 0:
        print(f"{Style.BRIGHT}{Fore.RED}NO ALIVE PROXIES FOUND!{Style.RESET_ALL}")
        sys.exit(1)
    if dead_count == 0:
        print(f"{Style.BRIGHT}{Fore.GREEN}ALL PROXIES ARE ALIVE!{Style.RESET_ALL}")
    else:
        print(f"{Style.BRIGHT}{Fore.GREEN}Saving results...{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}{Fore.GREEN}Results will be saved to 'results.json'.{Style.RESET_ALL}")
    return results

def save_results(results, filename):
    with open(filename, "w") as file:
        json.dump(results, file, indent=4)
    print(f"{Style.BRIGHT}{Fore.GREEN}Results saved to '{filename}'.{Style.RESET_ALL}")
    print(f"{Fore.GREEN}You can view the results in '{filename}'.{Style.RESET_ALL}")
    time.sleep(0.5)
    clear_screen()

def print_menu():
    print(f"{Style.BRIGHT}{Fore.GREEN}")
    print("╔" + "═"*38 + "╗")
    print("║" + " " * 38 + "║")
    print("║" + f"{'PROXY CHECKER MENU':^38}" + "║")
    print("║" + " " * 38 + "║")
    print("╠" + "═"*38 + "╣")
    print("║" + f"{Fore.GREEN}{Style.BRIGHT}1.{Style.NORMAL} List Active Proxies{' '*17}{Style.RESET_ALL}{Fore.GREEN}║")
    print("║" + f"{Fore.GREEN}{Style.BRIGHT}2.{Style.NORMAL} List Dead Proxies{' '*19}{Style.RESET_ALL}{Fore.GREEN}║")
    print("║" + f"{Fore.GREEN}{Style.BRIGHT}3.{Style.NORMAL} Reload Proxies and Check Again{Style.RESET_ALL}{Fore.GREEN}║")
    print("║" + f"{Fore.GREEN}{Style.BRIGHT}4.{Style.NORMAL} Exit{' '*29}{Style.RESET_ALL}{Fore.GREEN}║")
    print("╚" + "═"*38 + "╝" + Style.RESET_ALL)
    choice = input(f"{Style.BRIGHT}{Fore.GREEN}Enter your choice: {Style.RESET_ALL}")
    return choice

def main():
    proxies = load_proxies()
    
    results = check_proxies(proxies)
    save_results(results, 'outputs/results.json')
    active_proxies = [r for r in results if r["status"] == "alive"]
    dead_proxies = [r for r in results if r["status"] == "dead"]
    save_results(active_proxies, "outputs/active.json")
    save_results(dead_proxies, "outputs/dead.json")

    while True:
        print(f"{Fore.GREEN}{'-'*47}{Style.RESET_ALL}")
        choice = print_menu()
        if choice == "1":
            active_proxies = [r for r in results if r["status"] == "alive"]
            print(f"{Style.BRIGHT}{Fore.GREEN}ACTIVE PROXIES:{Style.RESET_ALL}")
            for proxy in active_proxies:
                print(f"{Fore.GREEN}{proxy['proxy']} - {proxy['latency']} ms{Style.RESET_ALL}")
        elif choice == "2":
            dead_proxies = [r for r in results if r["status"] == "dead"]
            print(f"{Style.BRIGHT}{Fore.RED}DEAD PROXIES:{Style.RESET_ALL}")
            for proxy in dead_proxies:
                print(f"{Fore.RED}{proxy['proxy']}{Style.RESET_ALL}")
        elif choice == "3":
            print(f"{Style.BRIGHT}{Fore.GREEN}Reloading proxies...{Style.RESET_ALL}")
            proxies = load_proxies()
            results = check_proxies(proxies)
            active_proxies = [r for r in results if r["status"] == "alive"]
            save_results(active_proxies, "outputs/active.json")
            print(f"{Style.BRIGHT}{Fore.GREEN}Proxies reloaded and checked.{Style.RESET_ALL}")
        elif choice == "4":
            print(f"{Style.BRIGHT}{Fore.GREEN}Thank you for using Proxy Checker!{Style.RESET_ALL}")
            print(f"{Style.BRIGHT}{Fore.GREEN}Exiting...{Style.RESET_ALL}")
            time.sleep(1)
            clear_screen()
            break
        else:
            print(f"{Style.BRIGHT}{Fore.RED}Invalid choice! Please try again.{Style.RESET_ALL}")
            time.sleep(1)

if __name__ == "__main__":
    main()
    print(f"{Style.BRIGHT}{Fore.GREEN}Proxy Checker finished.{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}{Fore.GREEN}Thank you for using Proxy Checker!{Style.RESET_ALL}")
