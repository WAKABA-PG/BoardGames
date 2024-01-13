import pygame
import random
class BoardGrid:
    def __init__(self):
        # 変数を定義
        self.square_num = 20
        self.screen_width = 1000
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        # 1マスの大きさ
        self.square_size = self.screen_width // self.square_num
        # 色
        self.BLACK = (0,0,0)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,128,0)
        self.BLUE = (0,0,255)
        self.YELLOW = (255,255,0)
        self.DODGER_BLUE = (30,144,255)
        self.DEEP_SKY_BLUE = (0,191,255)
        self.font = pygame.font.SysFont(None, 40)
        self.font_game_over = pygame.font.SysFont(None, 150)
        self.game_over = self.font_game_over.render("GAME OVER", False, self.RED, self.BLACK)
        self.clear = self.font.render("CLEAR!", False, self.YELLOW, self.BLUE)
        self.restart = self.font.render("RESTART", False, self.BLUE, self.YELLOW)
        self.board = [[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                      [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]]
        # ランダム設定
        self.random = self.square_num * self.square_num // 8
        while self.random > 0:
            j = random.randint(0, self.square_num - 1)
            l = random.randint(0, self.square_num - 1)
            if self.board[j][l] == -2:
                self.board[j][l] = -1
                self.random -= 1
        print(j)
        print(self.board)
    def draw_grid(self):
        for i in range(self.square_num):
            # 横線
            pygame.draw.line(self.screen,
                             self.DODGER_BLUE,
                             (0, i * self.square_size),
                             (self.screen_width, i * self.square_size),
                             2
                             )
            # 縦線
            pygame.draw.line(self.screen,
                             self.DODGER_BLUE,
                             (i * self.square_size, 0),
                             (i * self.square_size, self.screen_width),
                             2
                             )
    def draw_board(self):
        for row_index, row in enumerate(self.board):
            for col_index, col in enumerate(row):
                if 0 <= col <= 8:
                # number
                    pygame.draw.rect(
                    self.screen,
                    self.GREEN,
                    (col_index * self.square_size,
                    row_index * self.square_size,
                    50,
                    50)
                    )
                    text = self.font.render(str(col), True, self.YELLOW)
                    self.screen.blit(text, [col_index * self.square_size + 15, row_index * self.square_size + 10])
                if col == -3:
                    # TODO：エラーあり                    
                    pygame.draw.rect(
                    self.screen,
                    self.RED,
                    (col_index * self.square_size,
                    row_index * self.square_size,
                    50,
                    50)
                    )
                    img1 = pygame.image.load("bomb.png")
                    img1_2 = pygame.transform.scale(img1,(50,50))
                    self.screen.blit(img1_2,[col_index * self.square_size,row_index * self.square_size])
class Play:
    def __init__(self):
        self.vec_table = [
            (-1,-1),
            (0,-1),
            (1,-1),
            (-1,0),
            (1,0),
            (-1,1),
            (0,1),
            (1,1)
        ]
    def flip_pieces(self, col, row, boardGrid):
        print(col)
        print(row)
        bomb_list = 0
        for vx, vy in self.vec_table:
            x = vx + col
            y = vy + row
            if (0<= x < boardGrid.square_num
                and 0 <= y < boardGrid.square_num
                and boardGrid.board[y][x] == -1):
                bomb_list += 1
        print (bomb_list)
        if boardGrid.board[row][col] == -2:
            boardGrid.board[row][col] = bomb_list
            return False
        elif boardGrid.board[row][col] == -1:
            boardGrid.board[row][col] = -3
            for row_index, row in enumerate(boardGrid.board):
                for col_index, col in enumerate(row):
                    if boardGrid.board[row_index][col_index] == -1:
                        boardGrid.board[row_index][col_index] = -3
            return True
def main():
    pygame.init()
    pygame.display.set_caption("マインスイーパー")
    # 定数
    FPS = 60
    clock = pygame.time.Clock()
    game_over = False
    clear = False
    run = True
    boardGrid = BoardGrid()
    play = Play()
    while run:
        boardGrid.screen.fill(boardGrid.DEEP_SKY_BLUE)
        boardGrid.draw_grid()
        boardGrid.draw_board()        
        if game_over:
            boardGrid.screen.blit(boardGrid.game_over, (200,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                # K_キー名
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over == False:
                    mx, my = pygame.mouse.get_pos()
                    x = mx // boardGrid.square_size
                    y = my // boardGrid.square_size
                    if boardGrid.board[y][x] == -1 or boardGrid.board[y][x] == -2:  #まだひっくり返してない                      
                        game_over = play.flip_pieces(x, y, boardGrid)
                        #TODO クリア条件の入力
                        #for 
                        #if not boardGrid
                else:
                    boardGrid.board = [[-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2],
                                       [-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2]]
                    boardGrid.random = boardGrid.square_num * boardGrid.square_num // 8
                    while boardGrid.random > 0:
                        j = random.randint(0, boardGrid.square_num - 1)
                        l = random.randint(0, boardGrid.square_num - 1)
                        if boardGrid.board[j][l] == -2:
                            boardGrid.board[j][l] = -1
                            boardGrid.random -= 1
                    game_over = False
        pygame.display.update()
        clock.tick(FPS)
main()