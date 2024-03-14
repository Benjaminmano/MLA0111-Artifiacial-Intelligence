import math

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Represents the Tic Tac Toe board
        self.current_winner = None  # Keeps track of the winner

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # Tells us which number corresponds to which position on the board
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # Returns a list of indices of available spots on the board
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        # Checks if there is any empty spot on the board
        return ' ' in self.board

    def num_empty_squares(self):
        # Counts the number of empty spots on the board
        return self.board.count(' ')

    def make_move(self, square, letter):
        # If the move is valid, it assigns the letter to the square
        # Returns True if the move was valid, False otherwise
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False


def minimax(board, maximizer, depth=0):
    if board.current_winner == 'X':
        return -1
    elif board.current_winner == 'O':
        return 1
    elif not board.empty_squares():
        return 0

    if maximizer:
        max_eval = -math.inf
        for move in board.available_moves():
            board.make_move(move, 'O')
            eval = minimax(board, False, depth+1)
            board.board[move] = ' '  # Undo the move
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in board.available_moves():
            board.make_move(move, 'X')
            eval = minimax(board, True, depth+1)
            board.board[move] = ' '  # Undo the move
            min_eval = min(min_eval, eval)
        return min_eval


if __name__ == '__main__':
    t = TicTacToe()
    t.print_board_nums()
    print("\nInitial board:")
    t.print_board()

    while t.empty_squares():
        move_scores = []
        for move in t.available_moves():
            t.make_move(move, 'O')
            move_scores.append((move, minimax(t, False)))
            t.board[move] = ' '  # Undo the move
        best_move = max(move_scores, key=lambda x: x[1])[0]
        t.make_move(best_move, 'O')
        print(f"\nMove by AI (O) at position {best_move}:")
        t.print_board()
        if t.current_winner:
            break

        human_move = int(input("\nYour move (X), input position (0-8): "))
        t.make_move(human_move, 'X')
        print("\nYour move (X):")
        t.print_board()
        if t.current_winner:
            break

    if t.current_winner == 'X':
        print("\nYou win!")
    elif t.current_winner == 'O':
        print("\nAI wins!")
    else:
        print("\nIt's a tie!")
