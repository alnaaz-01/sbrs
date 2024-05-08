class NQueens:
    def solve(self, board, col, n):
        if col >= n:
            return True
        for i in range(n):
            if self.is_safe(board, i, col, n):
                board[i][col] = 'Q'
                if self.solve(board, col + 1, n):
                    return True
                board[i][col] = '.'
        return False
    def is_safe(self, board, row, col, n):
        # Check this row on the left side
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True
    def print_solution(self, board):
        for row in board:
            print(" ".join(row))
def main():
    n = int(input("Enter the number of queens: "))
    if n <= 0:
        print("Number of queens must be greater than 0.")
        return
    board = [['.'] * n for _ in range(n)]
    print("Solution using Backtracking:")
    n_queens = NQueens()  # Create an instance of the NQueens class
    if n_queens.solve(board, 0, n):  # Assuming 0 is the starting column
        n_queens.print_solution(board)
    else:
        print("No solution exists.")
#if __name__ == "__main__":
main()
