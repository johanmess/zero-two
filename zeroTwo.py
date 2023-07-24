import colorama, ctypes, os
from colorama import Fore

def coco():
    colorama.init()
    chose = int(input(f"0{Fore.RED}2{Fore.RESET} >  Elige un número (0, 1 o 2):  "))

    if chose == 0:
        os.system("cls")
        print(f"""{Fore.LIGHTRED_EX}
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣼⡄⠀⠀⠀⠀⠀⠀⢀⣠⡤⠤⠖⠒⠒⠒⠒⠈⠉⠉⠉⠙⠓⠒⠒⠦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡄⠀⣠⣴⣚⣉⣁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠓⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⡿⠟⠋⠁⠀⠀⠀⠀⠉⠉⠑⠲⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⢋⣤⠤⠤⠤⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠙⠢⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠞⠋⠀⠀⠀⠀⠀⠀⠈⠉⠓⠢⢤⡀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⠀⠀⠀⠀⠀
    ⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢦⣀⠀⠀⠀⠀⠉⠷⣄⠀⠀⣠⣴⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀
    ⠀⠀⠀⠉⠑⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠘⣦⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⣠⣿⡿⠀⠀⢀⡴⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⣴⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠀⣴⣿⡞⠀⠀⢀⡞⠁⠀⠀⣼⠁⠀⠀⠀⠀⠀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⣴⣿⡿⢛⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⠀⢀⣾⡻⡾⠁⠀⠀⡼⠁⠀⠀⣰⠁⠀⠀⢠⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣗⣛⡛⠷⢛⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣆⣼⢳⣻⠁⠀⠀⣼⠃⠀⠀⣰⡟⠀⠀⢀⡏⠀⢰⠇⠀⠀⠀⢠⠆⡤⠀⠀⠀⠀⠀⠘⠛⠒⢶⣔⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⠇⣿⡇⠀⠀⣰⠇⠀⡀⢀⣿⠇⠀⠀⡾⠀⠀⡞⠀⠀⠀⠀⡎⡼⡁⠀⠀⠀⢀⡆⠀⠀⠀⠀⢻⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢸⣾⠁⠀⢠⡿⠀⢰⠁⣸⣿⠀⠀⢸⠁⠀⢸⠁⠀⠀⠀⡾⣸⡿⠀⠀⠀⠀⡞⠀⣠⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢻⠘⣿⠀⠀⣸⡇⢀⡟⢠⣿⡏⠀⠀⡏⠀⢠⡏⠀⢠⠀⡸⣠⡿⠁⠀⠀⠀⣼⢃⢤⠏⠀⢀⠆⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀                           
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢸⠀⣿⡆⠀⣿⠀⢸⡗⣾⣧⠃⠀⣰⠇⠀⢸⠃⢠⠃⢠⢧⣿⠃⠀⠀⠀⣸⠃⡾⡜⠀⠀⣾⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⣼⣿⣷⣶
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣸⡀⣿⡇⠀⣿⣶⣾⡆⢸⣿⠀⠀⣿⠀⠀⡏⢠⡏⠀⣿⣾⠏⠀⠀⠀⢰⠇⣼⢡⠃⢀⣾⢳⠁⠀⠀⠀⢀⡞⠀⠀⠀⠀⡜⠁⠀⠀⠀⠀⢠⣿⣿⣿⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢾⡇⢹⣇⠀⣿⣟⣿⢻⣿⣿⠀⢸⢿⠀⢠⣧⡞⠀⡸⣾⣿⠀⠀⠀⢠⡟⣸⣇⡟⠀⣸⣏⡟⠀⠀⠀⠀⡼⠁⠀⠀⣠⡾⠁⠀⠀⠀⢀⠀⣸⣿⣟⣿⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⢿⣸⢿⡏⢻⣸⠙⣿⣦⡼⢸⠀⢸⡟⠙⢻⣷⣿⣇⣀⡀⢀⡞⣰⣿⡿⡇⠀⣿⢻⠁⠀⠀⠀⣸⠃⠀⣀⢀⣿⠃⠀⠀⠀⢰⠇⠀⣿⣿⣿⣿⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⡿⢸⠻⣼⠃⠘⠿⣯⣛⡿⡇⢸⣤⣿⠀⠀⣼⡿⣥⠀⠀⢉⡿⣻⢿⣿⣁⡇⢠⠏⡇⠀⠀⠀⣰⠇⠀⢠⡇⣸⠃⠀⠀⠀⢀⡏⠀⢀⣿⣿⣿⣿⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⡇⢸⠀⡿⠀⠀⠀⠀⠉⠀⠁⠀⠏⢻⠀⢠⣿⠷⣿⣶⣦⣼⣰⢃⣿⠃⢸⣷⡼⣾⠁⠀⠀⣠⠃⠀⢠⣿⣧⣿⡰⠀⠀⢀⡼⠁⠀⢢⡿⣿⣿⣿⣿                            
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢃⠇⠀⠀⡇⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣀⠉⣿⠿⣿⣿⣅⣀⢸⣿⢳⠃⠀⠀⢰⠏⠀⢠⣿⠿⣿⢷⠃⠀⠀⣸⢧⠀⢸⣼⣿⣻⣿⣿⣿
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⠀⠀⠀⣧⠀⠀⠀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⢿⣌⣻⣤⣿⠿⢟⠿⡏⠀⠀⣠⠇⠀⢀⣾⡉⢹⣿⡏⠀⠀⢰⣿⠏⠀⣼⣿⡿⣟⢿⣿⠉
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢸⠀⠀⣿⡿⣆⠀⠀⠷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⡼⠀⠀⣰⠃⠀⢀⡞⠀⠉⣿⡿⠀⠀⢀⣾⠃⠀⢠⣿⡿⣣⣿⠘⣿⠆
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢸⠀⢰⡟⡼⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣳⠁⠀⣴⠃⠀⢠⡾⢷⣣⣾⡻⠁⠀⠀⣼⠏⠀⠀⣼⢟⣵⣿⣿⡇⢸⡆
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⡏⠀⡼⠰⢳⡏⢳⡀⠀⠳⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣻⠃⠀⡴⠁⠀⢠⣿⣶⡟⢹⢻⠇⠀⠀⣰⠿⠒⠛⠛⠛⠿⣿⣿⣿⠇⢀⡇
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⡇⢠⠇⣠⢿⠃⠀⢳⡀⠀⠘⢮⣙⡶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢿⠇⢀⡾⠁⠀⢰⣿⣿⡟⠀⢎⡏⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠙⡿⠋⢀⡼⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣤⣇⡿⣰⠃⡞⠀⠀⢸⣷⡀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠏⢀⡞⠀⠀⣴⣿⣿⡿⠁⠐⣾⣶⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣴⠟⠁⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⢾⣿⢻⠇⠀⡇⠀⠀⠀⣿⡿⣦⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⡶⢾⣿⠇⢠⠏⠀⠀⣼⡟⣿⣿⠁⠀⢰⠇⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⣸⡞⡟⠀⠀⡇⠀⠀⠀⣿⠇⠀⣯⣿⣿⠉⣿⣿⣟⣽⣿⣿⣿⣿⠃⣰⠋⠀⢀⣾⡟⠀⣿⠃⠀⢀⡏⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⣿⢹⠁⠀⠀⡆⠀⠀⠀⡏⠀⢠⢻⣿⠈⠀⣿⣿⣿⣿⣿⣿⡿⠁⠀⠁⠀⣰⣿⡟⠀⣼⡏⠀⠀⣸⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⣏⡇⠀⠀⠀⡇⠀⠀⠀⣇⠀⢸⠸⣿⠀⣰⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣴⣿⡿⠀⠀⣿⠀⠀⠐⠃⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⢀⣀
    ⠀⠀⠀⠀⠀⠀⠜⠁⠀⢸⢹⠃⠀⠀⠀⡇⠀⠀⠀⢸⡀⡟⠀⢻⣶⡿⣿⣿⠋⣹⠏⠀⠀⠀⢀⠾⢿⡿⠁⠀⢠⠇⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⠙
    ⠀⠀⣀⣀⠄⠀⠀⠀⢀⡏⣼⠀⠀⠀⠀⣇⠀⠀⠀⠘⠇⣿⠀⣰⣿⣶⣾⣿⡿⠃⠀⠀⢀⣴⣋⣤⣾⡇⠀⢆⡞⠀⠀⠀⠀⠀⣴⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀  
            {Fore.RESET}""")
        coco()
    elif chose == 1:
        os.system('cls')
        print(f"""{Fore.LIGHTGREEN_EX}
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠔⠒⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠑⠒⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠊⠁⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀⠀⠀⢀⣤⠴⠒⠒⠉⠉⠉⠉⠉⠉⠒⠶⣄⡀⠀⠀⣠⣾⠟⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⡄⠀⣠⠶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢾⣿⣷⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢹⢿⡿⠿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠤⠖⠒⠒⠒⠒⠢⠤⢄⣀⡉⢿⡀⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⣾⣿⣧⣄⢠⠀⠀⠀⢀⡠⠔⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠈⠉⠛⠿⣧⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢱⣿⣿⣿⣿⢸⠀⢠⡶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢢⡀⠀⠀⠈⠑⣟⢽⡢⣄⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⡸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢸⡏⠿⢽⣿⣼⣴⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣄⠀⠀⠀⠀⠙⢆⠀⠀⠀⢈⠳⡈⠑⢽⡦⣄⠀⠀⠀
    ⣀⠀⠀⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⣿⣶⠞⠛⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⡄⢠⡀⠀⠀⠈⢣⡀⠀⠈⢣⠙⢆⠀⠈⠢⣷⣄⠀
    ⠀⠁⠂⠄⡀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⣸⠟⣠⠆⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⢹⣆⠳⡄⠀⠀⠀⢳⡀⠀⠀⢳⡌⢷⡀⠀⠈⠻⣄
    ⠀⠀⠀⠀⠁⢤⡸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⣴⠃⠀⡎⠀⠀⢁⠀⡆⠀⠀⢸⡀⢠⠀⠀⠀⠀⠀⡇⠀⠈⣿⡄⠱⡀⠀⠀⠀⢳⡀⠀⠀⢻⣄⠱⡄⠀⠀⠙
    ⠀⠀⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠐⠀⣾⠃⡞⠀⡇⠀⠀⢸⠀⣇⠀⠀⠀⡇⠘⡄⠀⠀⠘⡄⡇⠀⠀⢸⣿⡆⢻⡀⠀⠀⠀⢧⠀⠀⠈⣿⢦⠹⡄⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠹⡀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⡄⠇⡞⠀⢸⡃⢰⠀⢸⠀⢻⡀⠀⠀⢱⡀⢻⠀⠀⠀⢻⡇⠀⠀⠈⣿⡼⡄⢧⠀⠀⠠⠘⡇⠀⢀⠘⡄⢧⢹⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⠀⢠⠀⢀⡇⠀⠀⢠⠀⠀⠀⡇⡼⠁⠰⢷⡇⢸⠀⢸⡆⢸⣧⠀⠀⠸⣧⠈⡇⠀⡀⠀⡇⢰⠀⠀⢿⡇⠹⣘⣧⣀⡀⡇⢳⠀⠘⡆⢇⠀⢧⢳⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⢸⠀⢘⡇⠀⠀⠸⡆⠀⠀⢿⠀⠀⠰⠏⡇⢸⠀⢸⣿⠸⡌⣇⠀⣀⣻⣆⢹⡀⢣⠀⡇⢸⠀⠀⢸⣷⠚⢯⢹⡄⠀⢹⢸⠀⠀⣿⢸⠀⠘⡟⡀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⡈⡄⢸⣧⠀⢰⠀⢧⠀⠀⠘⢰⣠⠂⠀⢳⢸⣄⣬⣾⡖⡗⠻⡇⠀⠹⡽⡜⣿⠹⡄⣧⡟⠀⠀⢸⡹⠀⠘⡌⣧⠀⢸⣿⠀⠀⢹⢸⠧⠀⢱⠇              
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⡆⠀⡇⠆⡸⣿⠀⢸⠀⠸⡀⠀⠀⠀⡟⠀⡴⡿⡇⣧⠀⣿⣷⣿⠀⠹⡄⠀⢷⢱⣿⢧⣿⣿⢷⠀⢸⣸⣷⣶⣴⣷⣿⡆⣸⣿⠀⢀⣼⣼⠀⠂⠸⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⠃⠀⡇⡀⡇⣿⡀⠀⡇⠀⣷⡀⠀⠀⢧⡼⡿⠀⢳⢿⣀⣿⣿⣿⣿⣿⣿⣒⠘⡆⠻⡏⣿⣯⡀⡀⢸⣿⣿⣿⡟⠊⡟⠉⣿⣿⠀⣸⡟⡞⡆⠀⠆⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⠀⠃⣿⢠⡿⡇⠀⡇⠀⠘⣷⠀⠀⠸⣿⠁⣀⣤⣿⣿⣿⣿⣿⠏⠉⠋⠛⠋⠉⠀⢙⡼⠧⠹⣿⢿⢿⡿⠧⡄⠀⢠⣼⡏⢇⢠⡿⣼⠁⠹⡄⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⡿⢼⣿⣇⠀⢱⠀⠀⢻⢧⠀⠈⣷⡿⠻⡏⢿⣿⡧⢬⠠⡄⠀⠀⠀⠀⠀⠀⠚⠁⠀⠀⠁⠸⣅⣀⣼⣥⠃⠘⣹⣇⣿⣏⠈⠁⠀⠀⢣⠀⢣
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⣧⠤⢬⣹⡆⢸⡆⠀⠈⣏⢣⡀⢃⠐⠦⣕⡌⠉⠀⠀⣐⣧⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠈⠉⠉⠈⠀⠀⢿⡛⠁⢸⣧⠀⠀⠀⠈⠇⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⠀⠀⢀⠀⣟⠀⢀⣭⣇⠈⡇⠀⠀⠘⡄⢳⡸⡆⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣤⠀⠀⠀⠀⣸⡇⠀⠀⣿⢧⠀⠀⠀⠈⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀⢸⠀⣿⠀⢸⠀⢸⠀⢸⠀⠀⠀⠹⠀⠱⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠀⠀⠀⢀⣿⡇⠀⠀⡏⣧⢳⠀⠀⠀⠁
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠈⡆⣷⡀⠀⢀⢠⡇⠘⡆⠀⠀⠀⢦⠀⠘⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⢸⠿⣇⠀⢀⡇⠸⡄⢷⡀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣽⠞⠃⠀⢠⡇⠘⣷⣄⠈⠛⢿⡀⢷⠀⠀⠀⠈⢇⠀⢻⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠠⣻⠀⢸⡇⠀⢧⠀⢣⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⣼⡇⠀⣿⢻⣷⣤⣈⣇⠘⡄⠀⠀⠀⠘⣇⠈⡇⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⠴⠒⣒⡾⠁⠀⢠⡿⣿⠀⣿⠀⢸⠁⠀⢸⡄⠈⢧⠀                     
    ⠀⠀⠀⠀⠀⣠⢞⠃⠀⠀⠀⠀⣿⡟⠀⢹⠀⡟⣿⠈⢻⡀⢧⠀⠀⠀⠀⠘⡄⠸⡄⠹⣧⡀⠀⠀⠀⠀⠀⠰⡾⠭⠿⠶⠒⠊⢹⡏⠀⠀⣠⣾⠀⢸⡀⡿⠀⢸⢦⣄⣸⣷⠀⠈⡆
    ⠀⠀⣀⠴⢚⡟⠀⠀⠀⠀⠀⢠⣿⠹⡀⠸⣧⣿⣿⡀⠀⢷⠸⡄⠀⠀⠀⠀⠹⡄⢳⡀⠘⢿⣄⠀⠀⠀⠀⠀⠈⠳⠦⠤⠤⠶⣋⠀⠀⣴⠟⠹⡆⠸⡇⡇⠀⡼⣆⠈⠙⡿⡇⠀⡺
    ⠘⠉⠀⠀⡟⠀⠀⠀⠀⠀⠀⢸⠏⢀⣧⠀⢻⡏⠀⠉⠓⢾⡆⢷⠀⠀⠀⠀⠀⠹⡄⢧⣀⠈⠻⣧⡀⠀⠀⠀⠀⠀⠀⠀⠒⠚⠉⢠⡾⠃⠀⠀⣷⠀⢱⠇⠀⡇⠈⢧⡀⣷⡇⠀⠀
    ⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⡟⠀⡸⢹⠀⠈⡇⠀⠀⠀⠀⢱⠘⡆⠀⠀⠀⠀⠀⠹⣌⢿⠳⣶⣵⡽⣄⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠀⠀⠀⠀⠸⡄⠸⣼⠀⡇⠀⠀⠱⣿⡇⠀⠀
    ⠀⡠⠋⠀⠀⠀⠀⠀⠀⠀⢸⠇⣰⠃⣾⡇⠀⠹⡆⠀⠀⠀⠈⣧⢹⣄⠀⠀⠀⠀⠀⠘⣮⣆⠈⠻⣿⣞⢿⣶⣶⠤⣤⣀⣀⣴⡿⢻⠀⠀⠀⠀⠀⠃⠀⡇⢰⡇⠀⠀⠀⡟⡇⠀⠀
    ⡴⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣰⠃⣸⣵⣿⡆⠀⠹⡀⠀⠀⠀⠙⡆⢿⢆⠀⠀⠀⠀⠀⠘⢯⢦⢠⣿⣿⣧⠻⣏⢧⡀⠀⠀⠘⢷⡌⢧⠀⠀⠀⠀⠀⠀⡇⠀⣀⠀⠀⢀⡇⠁⠀⠂
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏⣴⢳⣿⡞⠙⡄⠀⢱⡄⠀⠀⠀⢳⠈⣏⠳⡀⠀⠀⠀⠀⠈⠳⣳⣿⣿⣿⣧⠙⣷⡳⣄⠀⠀⠈⢻⡌⢇⠀⠀⠀⠀⢀⡇⠀⡝⣗⢤⣸⠉⠀⠀⠀
    ⠀⠀⠀⡀⠀⠀⠀⠀⠀⢀⣏⡼⣡⣿⣻⠗⠛⠙⣆⠀⠙⡶⢤⣀⢀⣷⡸⣆⠘⢦⣀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣷⡈⢟⢿⡳⣄⡀⠀⠻⣮⢷⡀⠀⠀⢸⠀⠀⠱⡄⢳⣟⠀⠀⠀⠀
            {Fore.RESET}""")
        coco()
    elif chose == 2:
        os.system("cls")
        print(f"""{Fore.CYAN}
                    ⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢴⠟⠋⠙⢦⡆⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⣢⣎⣀⠀⡾⢳⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⡉⠉⠀⠹⢿⣼⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⠀⠀⡇⡎⡧⣀⣀⣠⢃⡏⠀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢀⠴⣱⣇⡗⢻⡻⣿⢾⣇⡀⠀⠀⠀⠀⠀⠀
            ⠀⠀⠀⠀⢀⣴⠇⣼⡿⣿⣆⣹⢣⣿⡿⣿⣧⡀⠀⠀⠀⠀⠀
            ⠀⠀⠀⣴⡿⢃⣼⣿⡇⢻⣿⣻⣿⡙⣿⣿⣿⣳⡄⠀⠀⠀⠀
            ⠀⢠⡾⡑⢠⡿⣜⡿⣿⣬⣿⣿⣿⣷⣬⣿⡿⢿⣽⣦⠀⠀⠀
            ⢀⣿⡷⢀⣿⡱⢎⣿⣿⣹⣿⣿⣿⢿⣿⢿⣧⢰⣿⡿⠁⠀⠀                      
            ⢸⣹⢡⣾⣿⡘⣽⣿⣧⣿⣿⣿⡾⣯⢷⣿⣧⣿⣿⠃⠀⠀⠀
            ⠀⢿⡍⣽⢸⠆⣿⣿⣿⣻⣼⣳⢿⡽⣛⣾⣿⡿⢿⢢⡀⠀⠀
            ⠀⠀⣧⣿⠈⣿⣿⣿⡷⢯⡿⣽⣛⣾⣻⡽⣿⣿⣄⢣⡙⠥⡂
            ⠀⠀⠘⠟⡄⣾⣿⣿⡽⣯⢟⣳⣟⢾⣵⣻⣳⢿⣿⣦⠗⠀⠀
            ⠀⠀⠀⠀⠀⢸⣽⣯⢷⣯⣟⣷⣿⣿⣾⣿⣿⣿⣿⣿⡦⠀⠀
            ⠀⠀⠀⠀⠀⢸⣿⣿⣾⣿⣿⠿⠿⠿⣿⣿⣿⣿⡛⠋⠁⠀⠀                         
            ⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⡟⠀⠀⠀⠹⣿⡿⣿⡇⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⢿⣿⣻⡇⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⠀⢸⣿⣷⡇⠀⠀⠀⠀⠀⠈⣿⣿⣷⠀⠀⠀⠀
            ⠀⠀⠀⠀⠀⢀⣾⣿⡿⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡀⠀⠀⠀
            ⠀⠀⠀⠀⠀⣼⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣧⠀⠀⠀
            ⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣧⠀⠀
            ⠀⠀⠀⠀⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡆⠀
            ⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠿⠿⠓⠀
            ⠀⠀⠀⢸⠉⢉⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠀⢈⠀
            ⠀⠀⠀⢸⡀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠈⠀
            ⠀⠀⠀⡸⢀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀
            ⠀⠀⠀⠇⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀
            ⠀⠀⠀⣧⣤⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⣀⣰
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁
            {Fore.RESET}""")
        coco()
    else:
        print(f"{Fore.LIGHTYELLOW_EX}Introduzca una opción válida (0, 1 o 2){Fore.RESET}")
        os.system('pause > nul')
        coco()

LF_FACESIZE = 32
STD_OUTPUT_HANDLE = -11

class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

class CONSOLE_FONT_INFOEX(ctypes.Structure):
    _fields_ = [("cbSize", ctypes.c_ulong),
                ("nFont", ctypes.c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", ctypes.c_uint),
                ("FontWeight", ctypes.c_uint),
                ("FaceName", ctypes.c_wchar * LF_FACESIZE)]

font = CONSOLE_FONT_INFOEX()
font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
font.nFont = 12
font.dwFontSize.X = 11
font.dwFontSize.Y = 18
font.FontFamily = 54
font.FontWeight = 400
font.FaceName = "MS Gothic"

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
ctypes.windll.kernel32.SetCurrentConsoleFontEx(handle, ctypes.c_long(False), ctypes.pointer(font))

ctypes.windll.kernel32.SetConsoleTitleW('zeroTwo [johanmess]')

print (f"""{Fore.LIGHTBLUE_EX}
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡷⡀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠺⣟⡽⠀⠀⠀⠀⠀⠀⠀⠈⠑⠂⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠊⠁⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠈⠳⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⠀⠆⠀⢰⡃⠀⠐⡄⠀⢲⠀⠃⢻⠀⠀⠀⡄⠀⠀⠈⠱⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠸⣶⣄⣺⢇⡄⠀⡇⠀⢰⢺⠱⣄⠀⠘⢆⠈⡆⠀⠸⠀⠀⠀⡇⠀⠀⠀⠰⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠙⢿⡏⢸⠀⠀⡇⠀⢸⣾⢀⣨⣷⡄⠈⢣⣇⠀⠀⡆⠀⠀⡇⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⠃⢸⡄⢸⡇⡀⢸⢿⡏⠀⣀⣹⣦⡀⢿⠀⠀⡇⠀⠀⡇⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣼⡄⠈⡇⠈⣿⣿⣼⣞⣷⠾⣿⣿⡿⠉⢻⠀⠀⡇⠀⠀⡿⠟⢷⡄⠀⠀⠀⡘⡄⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⡇⣇⢸⢿⡀⠇⠻⠉⠸⠏⣠⠟⠉⠀⠀⠀⡄⠀⠿⠀⠀⣿⡀⠀⡇⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣿⣿⣾⣷⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⢀⡿⢃⣼⠁⠀⠀⠃⠀⢸⠀⠀⠀⠀⠀⠀⠀               
    ⠀⠀⠀⠀⠀⢻⡻⢯⣻⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⠀⠀⠀⢸⡧⡎⢸⠃⠀⠀⢠⢀⣸⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⡇⢸⠉⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢸⡇⡇⢸⠀⠀⠀⢸⡈⣿⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢸⠃⢸⡀⠀⠀⠀⢀⡠⠴⠚⠀⠀⠀⠀⠀⢸⠀⠀⠀⢸⡇⢸⢸⡀⠀⠀⠈⡇⢻⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠘⡆⠀⢇⠀⠀⠰⠋⠀⠀⠀⠀⠀⠀⠀⠀⢨⠀⠀⠀⢸⠃⠈⡇⡇⠀⠀⠀⢱⢸⠀⠀⠀⠀⠀⠀⠀                      
    ⠀⠀⠀⠀⠀⠀⣿⠀⠈⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠍⠀⠀⠀⣿⠀⠀⢡⠱⠀⠀⠀⠸⡜⡇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣽⢆⠀⠀⠀⠀⠀⣠⠒⠁⠉⢀⡆⠀⠀⣿⡄⠀⠸⡄⠀⠀⠀⠀⢇⠇⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⣿⠀⠓⠤⠔⠒⠻⡇⢀⡴⠚⠉⡇⠀⠀⡧⢇⠀⠀⢱⡀⠀⠀⠀⠘⣾⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢸⡆⠀⢰⣿⡄⡆⠀⠀⠀⠀⢷⠋⠀⠀⠀⡇⠀⢀⠁⢈⠷⢶⣤⡷⣤⣤⢤⡤⠞⠓⠒⠦⢄⡀⠀
    ⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⡇⡇⢁⠀⠀⠀⢀⢻⠀⠀⠀⠀⡇⠀⢸⠀⠣⢤⣀⣞⡏⠉⡱⠋⠀⠀⠀⠀⠀⠀⠙⡆
    ⠀⠀⠀⠀⠀⠀⢸⠀⠀⡞⠀⢡⢸⡀⠀⣀⡼⠀⢳⠀⠀⠀⡇⠀⡏⠀⢀⣾⣿⣾⣟⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻
    ⠀⠀⠀⠀⠀⠀⢸⠀⢠⠇⠀⠈⢇⡷⣺⢿⠏⡞⠑⠚⠉⢀⠀⢠⠁⣠⣿⣿⣻⣟⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿
    ⠀⠀⠀⠀⠀⠀⣿⠀⡘⢀⣠⠞⣉⠵⣡⠏⠀⢧⠀⠀⠀⣸⠀⣾⣼⣉⣉⣍⡿⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
    ⠀⠀⠀⠀⢀⣴⡿⢠⠏⣉⣵⠞⠁⡰⡃⠀⠀⢘⡤⠴⢒⠇⢠⣿⡀⣉⣴⣿⣿⡁⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹
    ⠀⠀⠀⢀⠎⢸⡇⣸⣾⣿⣿⣀⣴⢱⣇⡤⠚⠁⢀⠀⣼⠄⡿⠋⠉⠁⢸⡛⢿⠑⢤⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
    ⠀⠀⠀⡞⢀⣎⢧⣟⣿⡿⠋⠀⠀⠉⠁⠀⣠⣾⠟⣸⡟⢸⠁⠀⠀⠀⠸⡇⢸⡄⢸⠃⠀⢀⣠⠤⠤⠤⠔⠢⡀⣸
    ⠀⠀⣸⠀⡸⢸⡟⣶⡿⠁⠀⠀⠀⠀⠀⠀⠉⠀⢠⣿⠀⡞⠀⠀⠀⠀⡇⣿⠸⣿⣾⠀⠀⠀⠙⠒⠒⠲⣌⣠⢌⣻
    ⠀⠀⡏⠀⣇⠞⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢿⢻⠀⡇⠀⠀⠀⠀⣷⡇⠀⢻⢹⡄⠀⠀⠀⠀⠀⠀⠈⠁⠀⣼
    ⠀⢰⢀⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢸⣞⡄⡇⠀⠀⠀⠀⡿⡇⠀⠸⡆⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟
    ⠀⡞⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣄⠀⢸⢸⠛⠙⠻⠀⠀⠀⠀⢣⡇⠀⠀⡇⢡⠀⠀⠀⠀⠀⡀⠀⠀⠀⡇
    ⠀⢳⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡿⠀⠀⡞⡀⠀⠀⠀⠀⠀⠀⠘⡾⡄⠀⡇⢸⠀⠀⠀⠀⡼⠁⠀⠀⢠⠃
    ⢸⢸⠀⣾⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠘⣿⣆⡇⡆⠀⠀⣀⡜⠁⠀⠀⠀⢸⡆          
{Fore.RESET}""")

coco()