# Py-Pac-Poe

# Global Variables
state = {}

# Welcome Message
def render_welcome_message():
    print()
    print("----------------------")
    print("Welcome to Py-Pac-Poe!")
    print("----------------------")

# Let's Play Message
def render_lets_play_message():
    print()
    print("----------------------")
    print("Let's play Py-Pac-Poe!")
    print("----------------------")

# Display Board
def render_board():
    print()
    print( "     A   B   C ")
    print()
    print( f"1)   {state['board']['a1'] if state['board']['a1'] else ' '} | {state['board']['b1'] if state['board']['b1'] else ' '} | {state['board']['c1'] if state['board']['c1'] else ' '} ")
    print( "    -----------")
    print( f"2)   {state['board']['a2'] if state['board']['a2'] else ' '} | {state['board']['b2'] if state['board']['b2'] else ' '} | {state['board']['c2'] if state['board']['c2'] else ' '} ")
    print( "    -----------")
    print( f"3)   {state['board']['a3'] if state['board']['a3'] else ' '} | {state['board']['b3'] if state['board']['b3'] else ' '} | {state['board']['c3'] if state['board']['c3'] else ' '} ")
    print()

# Check for Valid Move
def is_valid_move(move):
    # Make sure they entered a valid square on the board AND that no one has already taken that square
    return move in state['board'] and state['board'].get(move) == None

# Get Move
def get_move():
    move = ""
    while not is_valid_move(move):
        if move != "":
            print("Bogus move! Try again...")
            print()

        move = input(f"Player {state['turn']}'s Move (example B2): ").lower()

    return move

# Check Horizonal Win
def check_horizontal_win():
    if state['board']['a1'] == state['board']['b1'] and state['board']['b1'] == state['board']['c1']:
        return state['board']['a1']
    elif state['board']['a2'] == state['board']['b2'] and state['board']['b2'] == state['board']['c2']:
        return state['board']['a2']
    elif state['board']['a3'] == state['board']['b3'] and state['board']['b3'] == state['board']['c3']:
        return state['board']['a3']
    else:
        return None
    
# Check Vertical Win
def check_vertical_win():
    if state['board']['a1'] == state['board']['a2'] and state['board']['a2'] == state['board']['a3']:
        return state['board']['a1']
    elif state['board']['b1'] == state['board']['b2'] and state['board']['b2'] == state['board']['b3']:
        return state['board']['b1']
    elif state['board']['c1'] == state['board']['c2'] and state['board']['c2'] == state['board']['c3']:
        return state['board']['c1']
    else:
        return None
    
# Check Diagonal Win
def check_diagonal_win():
    if state['board']['a1'] == state['board']['b2'] and state['board']['b2'] == state['board']['c3']:
        return state['board']['a1']
    elif state['board']['c1'] == state['board']['b2'] and state['board']['b2'] == state['board']['a3']:
        return state['board']['c1']
    else:
        return None
    
# Check Tie
def check_tie():
    for square, turn in state['board'].items():
        if not turn:
            return None
    
    return 'T'
    
# Get Winner
def get_winner():
    return check_horizontal_win() or check_vertical_win() or check_diagonal_win() or check_tie()

# Initialize Game
def init_game():
    
    # Initialize current state of the game
    state['board'] = {
        'a1': None, 'b1': None, 'c1': None,
        'a2': None, 'b2': None, 'c2': None,
        'a3': None, 'b3': None, 'c3': None
    }
    state['turn'] = 'X'

    # Display let's play message
    render_lets_play_message()

    # Display board
    render_board()
    winner = None

    while not winner:

        # Get Move
        move = get_move()
        state['board'][move] = state['turn']

        # Display board
        render_board()

        # Next Move
        state['turn'] = 'O' if state['turn'] == 'X' else 'X'

        winner = get_winner()

    if winner == "T":
        print("Another tie!")
    else:
        print(f"Player {winner} wins the game!")

    print()

    return winner

# Check for win_goal
def met_win_goal(win_goal):
    return state['score']['X'] == win_goal or state['score']['O'] == win_goal

# Get winner of series
def get_series_winner(win_goal):
    return 'X' if state['score']['X'] == win_goal else 'O'

# Display score
def display_score():
    print()
    print("SCORE: ")
    print(f"Player X: {state['score']['X']}    Player O: {state['score']['O']}    Ties: {state['score']['T']}")
    print()

# Initialize Game Series
def init_game_series():

    # Initialize game series variables
    state['score'] = {
        'X': 0,
        'O': 0,
        'T': 0
    }

    # Prompt user for number of wins to play to
    render_welcome_message()
    win_goal = int(input("Enter the number of wins to play to: "))
    print(f"Great! We will play until someone gets {win_goal} wins.")

    while (not met_win_goal(win_goal)):
        winner = init_game()
        state['score'][winner] += 1
        display_score()

    print(f"Congrats to player {get_series_winner(win_goal)} for winning {win_goal} games!")
    print()


# Run Game Series  
init_game_series()