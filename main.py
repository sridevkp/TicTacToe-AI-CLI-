import random
from colorama import Fore,Back,Style

class My_style:
    BOLD = "\033[1m"
    NORMAL = "\033[0m"
    HEADER = "\033[95m"
    ENDC = "\033[0m"

data = []
PLAYER = "x" 
AI = "o"
DRAW = "draw"
BLANK = " "

def setup():
    print("\n\n")
    ans = input(Fore.LIGHTBLUE_EX+"Ready To Play? ( y / n ) :  "+Fore.RESET)
    if not ans in ["Y","y"] :
        return False
    data.clear()
    data.extend([[BLANK,BLANK,BLANK],[BLANK,BLANK,BLANK],[BLANK,BLANK,BLANK]]) 
    
    print("\n")
    return True

def render():
    [a,b,c] = data[0]
    [d,e,f] = data[1]
    [g,h,i] = data[2]

    print("\n")
    print('  '+a+'  |   '+b+'  |  '+c+'  ')
    print('---------------------')
    print('  '+d+'  |   '+e+'  |  '+f+'  ')
    print('---------------------')
    print('  '+g+'  |   '+h+'  |  '+i+'  ')
    print("\n")

def get_input():

    r = input(Fore.LIGHTYELLOW_EX+"Enter Row    ( 1 - 3 ):    "+Fore.RESET)
    while not is_input_valid(r):
        warn("Invalid input ")
        r = input(Fore.YELLOW+"Enter Row    ( 1 - 3 ):    "+Fore.RESET)
        
    r = int(r)

    c = input(Fore.LIGHTCYAN_EX+"Enter Column ( 1 - 3 ):    "+Fore.RESET)  
    while not is_input_valid(c):
        warn("Invalid input ")
        c = input(Fore.CYAN+"Enter Column ( 1 - 3 ):    "+Fore.RESET)
        
    c = int(c)

    return { "row": r -1, "col": c -1 }

def is_input_valid(val):
    return val.isdigit() and 1 <= int(val) <= 3

def warn(msg):
    print(Fore.RED+msg+Fore.RESET) 

def set_data( inp, turn ):
    n_data = data.copy()
    if turn == BLANK:
        n_data[inp["row"]][inp["col"]] = BLANK
        return n_data
    if n_data[inp["row"]][inp["col"]] == BLANK :
        n_data[inp["row"]][inp["col"]] = turn
        return n_data
    else :
        return None
        
def check_winner():
    for i in range(3):#check rows
        if data[i][0] == data[i][1] and data[i][0] == data[i][2]:
            return data[i][0]
        
    for i in range(3):#check cols
        if data[0][i] == data[1][i] and data[0][i] == data[2][i]:
            return data[0][i]
        
    if data[0][0] == data[1][1] and data[0][0] == data[2][2]:
        return data[1][1]
    
    if data[2][0] == data[1][1] and data[1][1] == data[0][2]:
        return data[1][1]
    
    for i in range(3):
        for j in range(3):
            if data[i][j] == BLANK : return BLANK 
    return DRAW

def check_available( data ):
    options = []
    for i in range(3):
        for j in range(3):
            if data[i][j] == BLANK : 
                options.append( { "row": i, "col": j })
    return options

def player_move():
    e = set_data( get_input(), PLAYER )
    while not e :
        warn("Already occupied")
        e = set_data( get_input(), PLAYER )
    data = e

def minmax( turn, depth ):
    global data
    result = check_winner()
    if result == AI:
        return 1
    elif result == DRAW :
        return 0
    elif result != BLANK:
        return -1
    
    options = check_available( data )
    best = -100
    if turn == AI:#max 
        for option in options:
            data = set_data( option, AI )
            score = minmax( PLAYER , depth+1 )
            best = max( score, best )
            data = set_data( option, BLANK )
    else:#min player
        best = 100
        for option in options:
            data = set_data( option, PLAYER )
            score = minmax( AI , depth+1 )
            best = min( score, best )
            data = set_data( option, BLANK )
    if abs(best) > 1:  print(best)
    return best 

    

def ai_turn():
    global data
    options = check_available( data ) 
                
    chosen = options[ random.randint(0, len(options)-1 ) ]
    if len(options) >= 9 :
        data = set_data( chosen, AI )
        return
    best = -100
    for option in options:
        data = set_data( option , AI)
        score = minmax( PLAYER, 0 )
        if score > best:
            chosen = option
            best = score
        data = set_data( option , BLANK)

    data = set_data( chosen, AI )

def handle_game_over( result ):
    render() 
    print(' ____              __    __        __  __\n|   _  /\  |\  /| |__   |  | \  / |__ |__|\n\___| /  \ | \/ | |__   |__|  \/  |__ | \ ')
    print(Back.LIGHTWHITE_EX)
    if result == PLAYER:
        print(Fore.GREEN+"         ________________\n         |  PLAYER won  |")
    if result == AI:
        print(Fore.RED+"         ________________\n         |    AI won    |")
    if result == DRAW:
        print(Fore.BLUE+"         ________________\n         | Game is DRAW |")
    print("         ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾"+Back.RESET+Fore.RESET)

def game():
    render()
    player_move()
    # print("player",data)
    winner = check_winner()
    if winner != BLANK: 
        # print(winner)
        handle_game_over( winner )
        if not setup() :
            exit()
    
    ai_turn()
    # print("ai",data)
    winner = check_winner()
    if winner != BLANK: 
        print("winner  :  ",winner)
        handle_game_over( winner )
        if not setup() :
            exit()
    
if __name__ == "__main__" :
    print(Back.WHITE+Fore.BLACK+My_style.BOLD)
    print("        __      __   __         __   _____  __\n| /\ | |__ |   |    |  ||\  /| |__     |   |  |\n|/  \| |__ |__ |__  |__|| \/ | |__     |   |__|")
    print("_____    __    _____        __   _____  __   __\n  |   | |        |    /\   |       |   |  | |__\n  |   | |__      |   /  \  |__     |   |__| |__")
    print(Back.RESET+Fore.RESET)

    if not setup() : exit()

    while True:
        game()