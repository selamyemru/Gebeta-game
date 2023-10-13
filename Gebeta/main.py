import pygame
from gameOver import gameOver
def main():
    # pygame initialization
    pygame.init()
    WIDTH, HEIGHT = 1536, 793
    CENTER = (WIDTH/2, HEIGHT/2)

    HOLE_SIZE = (160, 148)
    SEED_SIZE = (50, 50)
    ROW1 = 290
    COLUMN1 = 330

    COLUMN_SPACE = 180
    ROW_SPACE = 185
    ROW2 = ROW1 + ROW_SPACE

    HOLE1_POS = (COLUMN1, ROW1)
    HOLE2_POS = (COLUMN1 + COLUMN_SPACE, ROW1)
    HOLE3_POS = (COLUMN1 + 2*COLUMN_SPACE, ROW1)
    HOLE4_POS = (COLUMN1 + 3*COLUMN_SPACE, ROW1)
    HOLE5_POS = (COLUMN1 + 4*COLUMN_SPACE, ROW1)
    HOLE6_POS = (COLUMN1 + 5*COLUMN_SPACE, ROW1)

    HOLE7_POS = (COLUMN1, ROW2)
    HOLE8_POS = (COLUMN1 + COLUMN_SPACE, ROW2)
    HOLE9_POS = (COLUMN1 + 2*COLUMN_SPACE, ROW2)
    HOLE10_POS = (COLUMN1 + 3*COLUMN_SPACE, ROW2)
    HOLE11_POS = (COLUMN1 + 4*COLUMN_SPACE, ROW2)
    HOLE12_POS = (COLUMN1 + 5*COLUMN_SPACE, ROW2)

    screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.RESIZABLE)
    board = pygame.image.load('./img/board01.jpg')

    hole1 = pygame.image.load('./img/trou-bonduc06.png')
    hole1 = pygame.transform.scale(hole1, HOLE_SIZE)

    hole2 = pygame.image.load('./img/trou-bonduc04.png')
    hole2 = pygame.transform.scale(hole2, HOLE_SIZE)

    hole3 = pygame.image.load('./img/trou-bonduc04.png')
    hole3 = pygame.transform.scale(hole3, HOLE_SIZE)

    hole4 = pygame.image.load('./img/trou-bonduc04.png')
    hole4 = pygame.transform.scale(hole4, HOLE_SIZE)

    hole5 = pygame.image.load('./img/trou-bonduc04.png')
    hole5 = pygame.transform.scale(hole5, HOLE_SIZE)

    hole6 = pygame.image.load('./img/trou-bonduc04.png')
    hole6 = pygame.transform.scale(hole6, HOLE_SIZE)

    hole7 = pygame.image.load('./img/trou-bonduc04.png')
    hole7 = pygame.transform.scale(hole7, HOLE_SIZE)

    hole8 = pygame.image.load('./img/trou-bonduc04.png')
    hole8 = pygame.transform.scale(hole8, HOLE_SIZE)

    hole9 = pygame.image.load('./img/trou-bonduc04.png')
    hole9 = pygame.transform.scale(hole9, HOLE_SIZE)

    hole10 = pygame.image.load('./img/trou-bonduc04.png')
    hole10 = pygame.transform.scale(hole10, HOLE_SIZE)

    hole11 = pygame.image.load('./img/trou-bonduc04.png')
    hole11 = pygame.transform.scale(hole11, HOLE_SIZE)

    hole12 = pygame.image.load('./img/trou-bonduc04.png')
    hole12 = pygame.transform.scale(hole12, HOLE_SIZE)

    # Game logic initialization
    player_1 = [4,4,4,4,4,4]
    player_2 = [4,4,4,4,4,4]


    pot_1=0
    pot_2=0

    total = player_1 + [pot_1] + player_2 +[pot_2]


    def game_status():
        print(player_1)
        print(player_2)
        print("")
        print("Current position")
        print("")
        print("")
        
        print("                ######## Player 2 ########")
        print("")      
        print("            Position | 6 | 5 | 4 | 3 | 2 | 1 |")
        print("            ----------------------------------")
        print("            Count    | " + ' | '.join('{}'.format(k) for k in player_2[::-1]) + " |")
        
        print("")
        print("Player 2 Pot                                  Player 1 Pot")
        print("     {0}                                             {1}".format(pot_2,pot_1))
        print("")
        
        print("               ######## Player 1 ########")
        print("")
        print("            Position | 1 | 2 | 3 | 4 | 5 | 6 |")
        print("            ----------------------------------")
        print("            Count    | " + ' | '.join('{}'.format(k) for k in player_1) + " |")
        print("")
        print("")
            
    def print_winner(pot_1,pot_2):
        if pot_1>pot_2:
            print("")
            print("##########################################################")
            print("                Player 1 won!!                            ")
            print("##########################################################")
            print("")
        elif pot_2>pot_1:
            print("")
            print("##########################################################")
            print("                Player 2 won!!                            ")
            print("##########################################################")
            print("")
        else:
            print("")
            print("##########################################################")
            print("                It's a draw!!                            ")
            print("##########################################################")
            print("")

    
    def getBet(p):
        print("Turn: " + str(p))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if p == 2:
                        if pygame.Rect(HOLE1_POS[0]-HOLE_SIZE[0]/2, HOLE1_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 6
                        if pygame.Rect(HOLE2_POS[0]-HOLE_SIZE[0]/2, HOLE2_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 5
                        if pygame.Rect(HOLE3_POS[0]-HOLE_SIZE[0]/2, HOLE3_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 4
                        if pygame.Rect(HOLE4_POS[0]-HOLE_SIZE[0]/2, HOLE4_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 3
                        if pygame.Rect(HOLE5_POS[0]-HOLE_SIZE[0]/2, HOLE5_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 2
                        if pygame.Rect(HOLE6_POS[0]-HOLE_SIZE[0]/2, HOLE6_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 1
                    else:
                        if pygame.Rect(HOLE7_POS[0]-HOLE_SIZE[0]/2, HOLE7_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 1
                        if pygame.Rect(HOLE8_POS[0]-HOLE_SIZE[0]/2, HOLE8_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 2
                        if pygame.Rect(HOLE9_POS[0]-HOLE_SIZE[0]/2, HOLE9_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 3
                        if pygame.Rect(HOLE10_POS[0]-HOLE_SIZE[0]/2, HOLE10_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 4
                        if pygame.Rect(HOLE11_POS[0]-HOLE_SIZE[0]/2, HOLE11_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 5
                        if pygame.Rect(HOLE12_POS[0]-HOLE_SIZE[0]/2, HOLE12_POS[1]-HOLE_SIZE[1]/2, HOLE_SIZE[0], HOLE_SIZE[1]).collidepoint(event.pos):
                            return 6

    def draw_screen(player_1, player_2, turn):
        screen.fill((255, 255, 255))
        boardRect = board.get_rect()
        boardRect.center = CENTER
        screen.blit(board, boardRect)
        
        hole1 = pygame.image.load('./img/trou-bonduc0'+str(player_2[5])+'.png').convert_alpha()
        hole1 = pygame.transform.scale(hole1, HOLE_SIZE)
        hole1Rect = hole1.get_rect()
        hole1Rect.center = HOLE1_POS
        screen.blit(hole1, hole1Rect)
        
        hole2 = pygame.image.load('./img/trou-bonduc0'+str(player_2[4])+'.png').convert_alpha()
        hole2 = pygame.transform.scale(hole2, HOLE_SIZE)
        hole2Rect = hole2.get_rect()
        hole2Rect.center = HOLE2_POS
        screen.blit(hole2, hole2Rect)
        
        hole3 = pygame.image.load('./img/trou-bonduc0'+str(player_2[3])+'.png').convert_alpha()
        hole3 = pygame.transform.scale(hole3, HOLE_SIZE)
        hole3Rect = hole3.get_rect()
        hole3Rect.center = HOLE3_POS
        screen.blit(hole3, hole3Rect)
        
        hole4 = pygame.image.load('./img/trou-bonduc0'+str(player_2[2])+'.png').convert_alpha()
        hole4 = pygame.transform.scale(hole4, HOLE_SIZE)
        hole4Rect = hole4.get_rect()
        hole4Rect.center = HOLE4_POS
        screen.blit(hole4, hole4Rect)
        
        hole5 = pygame.image.load('./img/trou-bonduc0'+str(player_2[1])+'.png').convert_alpha()
        hole5 = pygame.transform.scale(hole5, HOLE_SIZE)
        hole5Rect = hole5.get_rect()
        hole5Rect.center = HOLE5_POS
        screen.blit(hole5, hole5Rect)
        
        hole6 = pygame.image.load('./img/trou-bonduc0'+str(player_2[0])+'.png').convert_alpha()
        hole6 = pygame.transform.scale(hole6, HOLE_SIZE)
        hole6Rect = hole6.get_rect()
        hole6Rect.center = HOLE6_POS
        screen.blit(hole6, hole6Rect)
        
        hole7 = pygame.image.load('./img/trou-bonduc0'+str(player_1[0])+'.png').convert_alpha()
        hole7 = pygame.transform.scale(hole7, HOLE_SIZE)
        hole7Rect = hole7.get_rect()
        hole7Rect.center = HOLE7_POS
        screen.blit(hole7, hole7Rect)
        
        hole8 = pygame.image.load('./img/trou-bonduc0'+str(player_1[1])+'.png').convert_alpha()
        hole8 = pygame.transform.scale(hole8, HOLE_SIZE)
        hole8Rect = hole8.get_rect()
        hole8Rect.center = HOLE8_POS
        screen.blit(hole8, hole8Rect)
        
        hole9 = pygame.image.load('./img/trou-bonduc0'+str(player_1[2])+'.png').convert_alpha()
        hole9 = pygame.transform.scale(hole9, HOLE_SIZE)
        hole9Rect = hole9.get_rect()
        hole9Rect.center = HOLE9_POS
        screen.blit(hole9, hole9Rect)
        
        hole10 = pygame.image.load('./img/trou-bonduc0'+str(player_1[3])+'.png').convert_alpha()
        hole10 = pygame.transform.scale(hole10, HOLE_SIZE)
        hole10Rect = hole10.get_rect()
        hole10Rect.center = HOLE10_POS
        screen.blit(hole10, hole10Rect)
        
        hole11 = pygame.image.load('./img/trou-bonduc0'+str(player_1[4])+'.png').convert_alpha()
        hole11 = pygame.transform.scale(hole11, HOLE_SIZE)
        hole11Rect = hole11.get_rect()
        hole11Rect.center = HOLE11_POS
        screen.blit(hole11, hole11Rect)
        
        hole12 = pygame.image.load('./img/trou-bonduc0'+str(player_1[5])+'.png').convert_alpha()
        hole12 = pygame.transform.scale(hole12, HOLE_SIZE)
        hole12Rect = hole12.get_rect()
        hole12Rect.center = HOLE12_POS
        screen.blit(hole12, hole12Rect)
        
        font = pygame.font.SysFont('Arial', 44)
        score_color = (255, 190, 0)


        label1 = font.render("Player 1", True, score_color)
        label1Rect = label1.get_rect()
        label1Rect.center = (100, 340)
        screen.blit(label1, label1Rect)
        
        score1 = font.render(str(total[13]), True, score_color)
        score1Rect = score1.get_rect()
        score1Rect.center = (100, 400)
        screen.blit(score1, score1Rect)
        
        seed = pygame.image.load('./img/seed.jpg')
        seed = pygame.transform.scale(seed, SEED_SIZE)
        seedRect = seed.get_rect()
        seedRect.center = (100, 460)
        screen.blit(seed, seedRect)
        
        label2 = font.render("Player 2", True, score_color)
        label2Rect = label2.get_rect()
        label2Rect.center = (WIDTH-100, 340)
        screen.blit(label2, label2Rect)

        score2 = font.render(str(total[6]), True, score_color)
        score2Rect = score2.get_rect()
        score2Rect.center = (WIDTH-100, 400)
        screen.blit(score2, score2Rect)
        
        player = font.render('Turn: '+str(turn), True, (0, 0, 0))
        playerRect = player.get_rect()
        playerRect.center = (WIDTH/2, 30)
        screen.blit(player, playerRect)

        seed = pygame.image.load('./img/seed.jpg')
        seed = pygame.transform.scale(seed, SEED_SIZE)
        seedRect = seed.get_rect()
        seedRect.center = (WIDTH - 100, 460)
        screen.blit(seed, seedRect)
        
        pygame.display.update()
                        
    game_status()

    game_cont = True
    exit_loop_a = False
    exit_loop_b = False


    font = pygame.font.SysFont('Arial', 36)

    while game_cont == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                
        draw_screen(player_1, player_2, 1)
        
        while exit_loop_b == False:
            z_b = [(a+1) for a,b in enumerate(player_2) if b==0]
            choice_b=0
            cond_b=0
            while cond_b==0:
                choice_b= getBet(2)
                if choice_b not in z_b:
                    cond_b=1
            
            pos_game = total[7+choice_b-1]
            bb = choice_b
            total[7+bb-1] =0
            total_copy = total[:]
            
            for i in range(0,pos_game):
                if (7+bb+i)>13:
                    bb = -i-7
                total[7+bb+i] += 1
                check_pot=7+bb+i
            
            if (7<=check_pot<=12) and (total_copy[check_pot]==0) and (total[check_pot]!=0) and (total[12-check_pot]!=0):
                total[13] += total[check_pot] + total[12-check_pot]
                total[check_pot]=0
                total[12-check_pot]=0
            
            player_1 = total[0:6]
            player_2 = total[7:13]
            
            pot_1=total[6]
            pot_2=total[13]
            
            game_status()
            
            if sum(player_1)==0 or sum(player_2)==0:
                print_winner(pot_1,pot_2)
                game_cont = False
                exit_loop_a = True
                exit_loop_b = True
                gameOver(1)

                
            if (check_pot)!=13:
                    break
            
        draw_screen(player_1, player_2, 2)
        
        while exit_loop_a == False:
            z_a = [(a+1) for a,b in enumerate(player_1) if b==0]
            choice_a=0
            cond_a=0
            while cond_a==0:
                choice_a= getBet(1)
                if choice_a not in z_a:
                    cond_a=1
            
            pos_game = total[choice_a-1]
            aa = choice_a
            total[aa-1] =0
            total_copy = total[:]
                
            for i in range(0,pos_game):
                if (aa+i)>12:
                    aa = -i
                total[aa+i] += 1
                check_pot=aa+i
                
            if (0<=check_pot<=5) and (total_copy[check_pot]==0) and (total[check_pot]!=0) and (total[12-check_pot]!=0):
                total[6] += total[check_pot] + total[12-check_pot]
                total[check_pot]=0
                total[12-check_pot]=0
            
            player_1 = total[0:6]
            player_2 = total[7:13]
            
            pot_1=total[6]
            pot_2=total[13]
            
            game_status()
            
            if sum(player_1)==0 or sum(player_2)==0:
                print_winner(pot_1,pot_2)
                game_cont = False
                exit_loop_a = True
                exit_loop_b = True
                gameOver(2)
            
            if (check_pot)!=6:
                break
        