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

# Proxy Checker

This repository provides a tool for checking HTTP and HTTPS proxies without passwords.

## Installation

To set up the Proxy Checker, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mxc-projects/proxy-ckeck.git
   cd proxy-ckeck
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How It Works

Proxy Checker validates HTTP and HTTPS proxies, ensuring they meet the following criteria:
- Only HTTP and HTTPS proxies are supported.
- Password-protected proxies are **not** supported.
  
The tool sends requests using the provided proxy list and checks their response status.

## Usage

1. Add your list of proxies to a file (e.g., `input.txt`), with one proxy per line:
   ```
   http://proxy1.com:8080
   https://proxy2.com:443
   ```

2. Run the Proxy Checker script:
   ```bash
   python3 proxy_chceck.py
   ```

   Do not replace name of input file!
   it will be inpuT.txt.

   Result would be generatwd automaticly.
    
        ## About This Version
    
    This first version of Proxy Checker is designed to validate **open HTTP and HTTPS proxies** that do **not require authentication** (no username or password). Simply provide a list of proxies in the `input.txt` file, and the script will automatically check which ones are working.
    
    **Note:**  
    - Only proxies without login/password are supported in this version.
    - The input file must be named `input.txt`.
    
    ## Coming in the Next Version
    
    The next release will add support for **authenticated proxies**. You will be able to check proxy lists that include usernames and passwords (combo lists), allowing you to validate proxies that require login credentials.

---

