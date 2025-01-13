import os



class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'






banner = '''
,--.                ,--.          ,--.,--.               
|  |,--,--,  ,---.,-'  '-. ,--,--.|  ||  | ,---. ,--.--. 
|  ||      \(  .-''-.  .-'' ,-.  ||  ||  || .-. :|  .--' 
|  ||  ||  |.-'  `) |  |  \ '-'  ||  ||  |\   --.|  |    
`--'`--''--'`----'  `--'   `--`--'`--'`--' `----'`--'   '''

print(bcolors.YELLOW + banner)
user_input = input('Do you want install all packages? y/n: ')

if user_input == 'y':
    os.system('pkg install apt')
    os.system('apt install nmap')
    os.system('apt install aircrack-ng')
    os.system('apt install python3-pip')

if user_input == 'n':
    print(bcolors.GREEN + 'exiting...' + bcolors.RESET)
    os.system('python3 run.py')
