# Py-Pac-Poe

# Global Variables
state = {}

# Welcome Message
def welcome():
    print("----------------------")
    print("Let's play Py-Pac-Poe!")
    print("----------------------")
    print()

# Display Board
def print_board():
    print( "     A   B   C ")
    print()
    print( f"1)   {state['board']['a1'] if state['board']['a1'] else ' '} | {state['board']['b1'] if state['board']['b1'] else ' '} | {state['board']['c1'] if state['board']['c1'] else ' '} ")
    print( "    -----------")
    print( f"1)   {state['board']['a2'] if state['board']['a2'] else ' '} | {state['board']['b2'] if state['board']['b2'] else ' '} | {state['board']['c2'] if state['board']['c2'] else ' '} ")
    print( "    -----------")
    print( f"1)   {state['board']['a3'] if state['board']['a3'] else ' '} | {state['board']['b3'] if state['board']['b3'] else ' '} | {state['board']['c3'] if state['board']['c3'] else ' '} ")
    print()

# Check for Valid Move
def is_valid_move(move):
    return move in state['board']

# Get Move
def get_move():
    move = ""
    while not is_valid_move(move):
        if move != "":
            print("Bogus move! Try again...")
            print()

        move = input(f"Player {state['turn']}'s Move (example B2): ").lower()
        
    return move

# Get Winner
def get_winner():
    return None

# Initialize Game
def init_game():
    # Initialize current state of the game
    state['board'] = {
        'a1': 'X', 'b1': None, 'c1': None,
        'a2': None, 'b2': 'O', 'c2': None,
        'a3': None, 'b3': None, 'c3': None
    }
    state['turn'] = 'X'

    # Display welcome message
    welcome()

    #while not get_winner():
    # Display board
    print_board()

    # Get Move
    move = get_move()
    print(f"Next move is {move}")

# Run Game    
init_game()