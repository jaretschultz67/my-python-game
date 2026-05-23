import tkinter as tk

ROWS = 6
COLS = 7
CELL_SIZE = 80

# Colors
EMPTY = "white"
PLAYER1 = "green"
PLAYER2 = "blue"

current_player = PLAYER1

# Create board
board = [[EMPTY for _ in range(COLS)] for _ in range(ROWS)]

# Window
root = tk.Tk()
root.title("Connect 4")

canvas = tk.Canvas(root, width=COLS * CELL_SIZE,
                   height=ROWS * CELL_SIZE,
                   bg="black")
canvas.pack()


def draw_board():
    canvas.delete("all")

    for row in range(ROWS):
        for col in range(COLS):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            canvas.create_oval(
                x1 + 5, y1 + 5,
                x2 - 5, y2 - 5,
                fill=board[row][col]
            )


def drop_piece(col):
    global current_player

    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == EMPTY:
            board[row][col] = current_player

            if check_winner(row, col):
                draw_board()
                canvas.create_text(
                    COLS * CELL_SIZE // 2,
                    20,
                    text=f"{current_player.upper()} WINS!",
                    fill="black",
                    font=("Arial", 24, "bold")
                )
                return

            current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1
            break


def check_winner(row, col):
    color = board[row][col]

    directions = [
        (1, 0),   # vertical
        (0, 1),   # horizontal
        (1, 1),   # diagonal down-right
        (1, -1)   # diagonal down-left
    ]

    for dr, dc in directions:
        count = 1

        # Check one direction
        r, c = row + dr, col + dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == color:
            count += 1
            r += dr
            c += dc

        # Check opposite direction
        r, c = row - dr, col - dc
        while 0 <= r < ROWS and 0 <= c < COLS and board[r][c] == color:
            count += 1
            r -= dr
            c -= dc

        if count >= 4:
            return True

    return False


def handle_click(event):
    col = event.x // CELL_SIZE

    if 0 <= col < COLS:
        drop_piece(col)
        draw_board()


canvas.bind("<Button-1>", handle_click)

draw_board()

root.mainloop()
import pygame

pygame.init()
pygame.mixer.init()

# Create window
screen = pygame.display.set_mode((800, 600))

# Load sound
jump_sound = pygame.mixer.Sound("jump.wav")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Play sound when SPACE is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jump_sound.play()

pygame.quit()
