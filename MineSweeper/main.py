import pygame
import random

class BoardGrid:
    def __init__(self):
        # 変数を定義
        self.square_num = 20
        self.screen_width = 1000
        self.screen_height = 1000

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        #１マスの大きさ(50)
        self.suqare_size = self.screen_width // self.square_num
        #色
        self.BLACK = (0,0,0)
        self.GREY = (192,192,192)
        self.SNOW=(255,250,250)
        self.MOCA=(255,228,181)
        self.WHITE = (255,255,255)
        self.RED = (255,0,0)
        self.GREEN = (0,128,0)
        self.BLUE = (0,0,255)
        self.YELLOW = (255,255,0)

        # TODO
        self.font = pygame.font.SysFont(None, 100)
        self.font2 = pygame.font.SysFont(None, 40)

        self.win_black = self.font.render("黒が勝ったよ！", False, self.BLACK, self.RED)
        self.win_white = self.font.render("白が勝ったよ！", False, self.WHITE, self.RED)
        self.drow = self.font.render("引き分け！", False, self.BLUE, self.RED)
        self.restart = self.font.render("リスタート", False, self.BLUE, self.RED)

        # 盤面作成
        self.board =self.init_board(7)
    
    def draw_grid(self):
        for i in range(self.square_num):
            # 横線
            pygame.draw.line(self.screen,
                              self.BLACK,
                              (0, i * self.suqare_size),
                              (self.screen_width, i * self.suqare_size),
                              3
                                )
            # 縦線
            pygame.draw.line(self.screen,
                              self.BLACK,
                              ( i * self.suqare_size, 0),
                              (i * self.suqare_size, self.screen_height),
                              3
                                )
    def draw_board(self):
        for row_index, row in enumerate(self.board):
            for col_index,col in enumerate(row):
                # 周りの地雷数が１より大きいとき
                if col >=  0:
                    pygame.draw.rect(self.screen, self.SNOW, (col_index * self.suqare_size, row_index* self.suqare_size, 50, 50))
                    text =  self.font2.render(str(col), True, self.BLACK) 
                    self.screen.blit(text, [col_index * self.suqare_size + 15,  row_index* self.suqare_size+10])
    
    def init_board(self, bombCount):
        board = []

        # 二次元配列を作成
        for row in range(self.square_num):
            boardChild = []
            for col in range(self.square_num):
                boardChild.append(-2)
            board.append(boardChild)
        
        # 地雷を埋め込む
        while bombCount > 0: 
            # 地雷の位置をランダムに決定
            j = random.randint(0, self.square_num - 1)
            i = random.randint(0, self.square_num - 1)

            if board[i][j] != -1:
                # まだ地雷が設定されていなければ、地雷(-1)を設置
                board[i][j] = -1
                bombCount -=1
        return board


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

    # クリックした箇所が地雷かどうか判別
    def check_bomb(self, boardGrid, mx, my):
        if boardGrid.board[my][mx] == -1:
            return True
        else:
            return False
        

    
    # クリックしたところの周りの地雷数をカウント
    def search_inspector(self, boardGrid, mx, my):
        bomb_count = 0
        for vx, vy in self.vec_table:
            x = vx + mx
            y = vy + my
            if(0<= x < boardGrid.square_num
                and 0 <= y < boardGrid.square_num
                and boardGrid.board[y][x] == -1):
                # 盤面の枠内かつ、地雷の場所ならカウントアップ
                bomb_count += 1

        return bomb_count            


def main():
    pygame.init()
    pygame.display.set_caption("マインスイーパー")

    # 定数
    FPS = 60
    clock = pygame.time.Clock()

    game_over = False

    boardGrid = BoardGrid()
    play = Play()

    run = True
    while run:
        boardGrid.screen.fill(boardGrid.GREY)
        boardGrid.draw_grid()
        boardGrid.draw_board()

        for evet in pygame.event.get():
            if evet.type == pygame.QUIT:
                run = False
            
            # マウスがクリックされたとき
            if evet.type == pygame.MOUSEBUTTONDOWN:
                mx, my =pygame.mouse.get_pos()
                x = mx // boardGrid.suqare_size
                y = my // boardGrid.suqare_size
                print(f'{x}、{y}')

                # 地雷かどうか判別
                if play.check_bomb(boardGrid, x, y):
                    # 地雷なら終了
                    game_over = True
                    print("OUT!!!!!")
                else:
                    # 地雷でなければ周りの地雷数取得して、設定
                    count = play.search_inspector(boardGrid, x, y)
                    print(count)
                    boardGrid.board[y][x] = count




        pygame.display.update()
        clock.tick(FPS)


main()

