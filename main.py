import random

data = []
PLAYER = "x" 
AI = "o"
DRAW = "draw"
BLANK = " "

def setup():
    print("\n\n")
    ans = input("Ready To Play? ( y / n )     :")
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
    r = input("Enter row ( 1 - 3 ):    ")
    try : 
        r = int(r)
    except:
        r=None
    while not r or not 1 <= int(r) <= 3:
        print("Invalid input ")
        r = input("Enter row ( 1 - 3 ):    ")
        try : 
            r = int(r)
        except:
            r=None

    c = input("Enter Column ( 1 - 3 ):    ")
    try : 
        c = int(r)
    except:
        c=None
    while not c or not 1 <= int(c) <= 3:
        print("Invalid input ")
        c = input("Enter Column ( 1 - 3 ):    ")
        try : 
            c = int(c)
        except:
            c=None

    return { "row": int(c) -1, "col": int(r) -1 }

def set_data( inp, turn ):
    if data[inp["row"]][inp["col"]] != BLANK :
        return False
    else :
        data[inp["row"]][inp["col"]] = turn
        return True

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

def player_move():
    e = set_data( get_input(), PLAYER )
    while not e :
        print("\nAlready occupied\n")
        e = set_data( get_input(), PLAYER )


def ai_turn():
    options = []
    for i in range(3):
        for j in range(3):
            if data[i][j] == BLANK : 
                options.append( { "row": i, "col": j }) 
                
    chosen = options[ random.randint(0, len(options)-1 ) ]
    set_data( chosen, AI )


def handle_game_over( result ):
    render() 
    print(' ____              __    __        __  __\n|   _  /\  |\  /| |__   |  | \  / |__ |__|\n\___| /  \ | \/ | |__   |__|  \/  |__ | \ ')
    print("\n________________")
    if result == PLAYER:
        print("|  PLAYER won  |")
    if result == AI:
        print("|    AI won    |")
    if result == DRAW:
        print("| Game is DRAW |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def game_loop():
    render()
    player_move()

    winner = check_winner()
    if winner != BLANK: 
        print(winner)
        handle_game_over( winner )
        if not setup() :
            exit()
    
    ai_turn()

    winner = check_winner()
    if winner != BLANK: 
        print("winner  :  ",winner)
        handle_game_over( winner )
        if not setup() :
            exit()
    

if __name__ == "__main__" :
    print("        __      __   __         __   _____  __\n| /\ | |__ |   |    |  ||\  /| |__     |   |  |\n|/  \| |__ |__ |__  |__|| \/ | |__     |   |__|")
    print("_____    __    _____        __   _____  __   __\n  |   | |        |    /\   |       |   |  | |__\n  |   | |__      |   /  \  |__     |   |__| |__")
    
    if not setup() : exit()

    while True:
        game_loop()