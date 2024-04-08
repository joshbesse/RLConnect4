import numpy as np 
import pygame 
import sys 


pygame.init()
width = 700
height = 700
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Conenct 4")

BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("monospace", 50)

class Connect4:
    def __init__(self):
        # board creation
        self.rows = 6
        self.columns = 7
        self.board = np.zeros((self.rows, self.columns), dtype=int)
        # game over state
        self.game_over = False
        # player 1 starts 
        self.current_player = 1
    
    # Action Handling
    def is_valid_location(self, col):
        return self.board[0, col] == 0
    
    def drop_piece(self, row, col, piece):
        self.board[row, col] = piece

    def next_open_row(self, col):
        for r in range(self.rows-1, -1, -1):
            if self.board[r, col] == 0:
                return r
        return None 
    
    # Game Rules 
    def play_move(self, col):
        if self.is_valid_location(col):
            row = self.next_open_row(col)
            if row is not None:
                self.drop_piece(row, col, self.current_player)
                if self.check_win():
                    self.game_over = True
                # switch players turn 
                self.current_player = 3 - self.current_player
                return True 
        return False 
    
    # Check Win Condition 
    def check_win(self):
        # check horizontal win
        for c in range(self.columns-3): 
            for r in range(self.rows):
                if self.board[r][c] == self.current_player and self.board[r][c+1] == self.current_player and self.board[r][c+2] == self.current_player and self.board[r][c+3] == self.current_player:
                   return True 
                
        # check vertical win
        for c in range(self.columns):
            for r in range(self.rows-3):
                if self.board[r][c] == self.current_player and self.board[r+1][c] == self.current_player and self.board[r+2][c] == self.current_player and self.board[r+3][c] == self.current_player:
                    return True 
                
        # check right diagonal win
        for c in range(self.columns-3):
            for r in range(self.rows-3):
                if self.board[r][c] == self.current_player and self.board[r+1][c+1] == self.current_player and self.board[r+2][c+2] == self.current_player and self.board[r+3][c+3] == self.current_player:
                    return True
        
        # check left diagonal win
        for c in range(self.columns-3):
            for r in range(3, self.rows):
                if self.board[r][c] == self.current_player and self.board[r-1][c+1] == self.current_player and self.board[r-2][c+2] == self.current_player and self.board[r-3][c+3] == self.current_player:
                    return True
        
        return False 
    
    # Display Game 
    def draw_board(self, screen):
        for c in range(self.columns):
            for r in range(self.rows):
                pygame.draw.rect(screen, BLUE, (c * 100, r * 100 + 100, 100, 100))
                color = WHITE
                if self.board[r, c] == 1:
                    color = RED 
                elif self.board[r, c] == 2:
                    color = YELLOW
                pygame.draw.circle(screen, color, (int(c*100+50), int(r*100+150)), 44)

        if self.game_over:
            label = font.render(f"Player {3 - self.current_player} wins!", 1, (255, 0, 0) if 3 - self.current_player == 1 else (255, 255, 0))
            screen.blit(label, (135, 20))


board = Connect4()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not board.game_over:
            xpos = event.pos[0]
            col = xpos // 100
            if board.play_move(col):
                if board.check_win():
                    board.game_over = True

    screen.fill(WHITE)
    board.draw_board(screen)
    pygame.display.update()


