import time
from engine import TicTacToe, minimax

def play():
    game = TicTacToe()
    human_letter = 'X'
    ai_letter = 'O'
    
    print("\n--- Unbeatable Tic-Tac-Toe AI ---")
    print("Board Positions: \n| 0 | 1 | 2 |\n| 3 | 4 | 5 |\n| 6 | 7 | 8 |")
    
    # Game Loop
    while game.available_moves():
        if len(game.available_moves()) == 9: # Human starts
            letter = human_letter
        else:
            # Switch players
            letter = ai_letter if letter == human_letter else human_letter

        if letter == ai_letter:
            print(f"\nAI ({letter}) is thinking...")
            # If it's the first move for AI, pick a random corner to save computation time
            if len(game.available_moves()) == 9:
                square = 4 # Center is statistically strong
            else:
                square = minimax(game, ai_letter)['position']
            time.sleep(0.5) # Add a slight delay for "realism"
        else:
            # Human Input with Validation
            square = None
            while square is None:
                user_input = input(f"\n{letter}'s turn. Input move (0-8): ")
                try:
                    val = int(user_input)
                    if val not in game.available_moves():
                        raise ValueError
                    square = val
                except ValueError:
                    print("Invalid square. Try again.")

        if game.make_move(square, letter):
            print(f"{letter} makes a move to square {square}")
            game.print_board()
            print("") # Empty line for readability

            if game.current_winner:
                print(f"{letter} wins!")
                return

    print("It's a tie!")

if __name__ == '__main__':
    play()