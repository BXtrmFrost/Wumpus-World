import random
import sys
import pygame

class Tile:

    def __init__(self, enable, breeze, stench, glitter, pit, monster, gold, reveal, player):

        # Enable the boxes available around the player
        self.enable = enable

        # To check Breeze Signal
        self.breeze = breeze

        # To check Stench Signal
        self.stench = stench

        # To Check Glitter Signal
        self.glitter = glitter

        # Pit Present
        self.pit = pit

        # Moster Present
        self.monster = monster

        # Gold Present
        self.gold = gold

        # To Display the current signals
        self.reveal = reveal

        # To check if Plyaer is present in Tile
        self.player = player

class Player:

    def __init__(self):

        # Playing Game until Player is alive
        self.alive = True

        # Player has one arrow to shoot
        self.arrow = 1

        # Initilaizing Player Position
        self.pos = [[0 for i in range(0, 6)] for i in range(0, 6)]
        self.pos[5][0] = 1

        self.xpos = 5
        self.ypos = 0

    def player_position(self):

        return [self.xpos, self.ypos]

def create_gamemap(num):
    # To read and store the game map
    gamemap = []

    # To create Tile Objects and storing in an list
    gamemap_objects = []

    # Read from the file
    file_data = open(f"Maps\map{num}.txt", "r")

    # Fetching Data from the File
    for i in range(0, 6):
        data = file_data.readline().split(' ')
        data.pop()
        gamemap.append(data)

    # Creating Tile Objects
    for row in gamemap:
        temp = []
        for col in row:
            if col == '0':
                temp.append(Tile(False, False, False, False,
                            False, False, False, False, False))
            elif col == '1':
                temp.append(Tile(False, False, False, False,
                            False, False, True, False, False))
            elif col == '2':
                temp.append(Tile(False, False, False, False,
                            False, True, False, False, False))
            elif col == '3':
                temp.append(Tile(False, False, False, False,
                            True, False, False, False, False))
        gamemap_objects.append(temp)

    # Fixing Game Map
    for i in range(0, 6):
        for j in range(0, 6):
            if(gamemap_objects[i][j].monster == True):
                if(i-1 != -1):
                    gamemap_objects[i-1][j].stench = True
                if(i+1 != 6):
                    gamemap_objects[i+1][j].stench = True
                if(j-1 != -1):
                    gamemap_objects[i][j-1].stench = True
                if(j+1 != 6):
                    gamemap_objects[i][j+1].stench = True
            if(gamemap_objects[i][j].gold == True):
                if(i-1 != -1):
                    gamemap_objects[i-1][j].glitter = True
                if(i+1 != 6):
                    gamemap_objects[i+1][j].glitter = True
                if(j-1 != -1):
                    gamemap_objects[i][j-1].glitter = True
                if(j+1 != 6):
                    gamemap_objects[i][j+1].glitter = True
            if(gamemap_objects[i][j].pit == True):
                if(i-1 != -1):
                    gamemap_objects[i-1][j].breeze = True
                if(i+1 != 6):
                    gamemap_objects[i+1][j].breeze = True
                if(j-1 != -1):
                    gamemap_objects[i][j-1].breeze = True
                if(j+1 != 6):
                    gamemap_objects[i][j+1].breeze = True

    gamemap_objects[5][0].player = True
    gamemap_objects[5][1].enable = True
    gamemap_objects[4][0].enable = True
    return gamemap_objects

def game_call():
    global __gamemap__, player, key, selected_keys,  player_xpos, player_ypos

    player = Player()
    key = 0
    selected_keys = 0
    player_xpos = 135
    player_ypos = 640
    maap = random.randint(0, 4)
    __gamemap__ = create_gamemap(maap)


def enable(data_cap):
    if(data_cap[0] != 5):
        __gamemap__[data_cap[0]+1][data_cap[1]].enable = True
    if(data_cap[0] != 0):
        __gamemap__[data_cap[0]-1][data_cap[1]].enable = True
    if(data_cap[1] != 5):
        __gamemap__[data_cap[0]][data_cap[1]+1].enable = True
    if(data_cap[1] != 0):
        __gamemap__[data_cap[0]][data_cap[1]-1].enable = True

def disable(data_cap):
    if(data_cap[0] != 5):
        __gamemap__[data_cap[0]+1][data_cap[1]].enable = False
    if(data_cap[0] != 0):
        __gamemap__[data_cap[0]-1][data_cap[1]].enable = False
    if(data_cap[1] != 5):
        __gamemap__[data_cap[0]][data_cap[1]+1].enable = False
    if(data_cap[1] != 0):
        __gamemap__[data_cap[0]][data_cap[1]-1].enable = False

def disable_monster(data_cap):
    if(data_cap[0] != 5):
        __gamemap__[data_cap[0]+1][data_cap[1]].stench = False
    if(data_cap[0] != 0):
        __gamemap__[data_cap[0]-1][data_cap[1]].stench = False
    if(data_cap[1] != 5):
        __gamemap__[data_cap[0]][data_cap[1]+1].stench = False
    if(data_cap[1] != 0):
        __gamemap__[data_cap[0]][data_cap[1]-1].stench = False

    
# FPS Clock
pygame.init()
FPS = 60
fpsclock = pygame.time.Clock()

# Screen Size
width = 1080
height = 720

pygame.display.set_caption("Wumpus World")


screen = pygame.display.set_mode((width, height))

# Loading Game Fonts
font = pygame.font.Font("Assets\\CascadiaCode.ttf", 20, italics=True)
font1 = pygame.font.Font("Assets\\CascadiaCode.ttf", 16, italics=True)
font2 = pygame.font.Font("Assets\\Game Of Squids.ttf", 50)


game_call()

while(True):


    # Filling Game Screens
    screen.fill((204, 229, 255))

    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 1080, 80))
    pygame.draw.rect(screen, (0, 0, 51), pygame.Rect(780, 80, 300, 640))
    pygame.draw.rect(screen, (76, 153, 0), pygame.Rect(790, 90, 280, 620))

    # Displaying Tiles
    x = 100
    y = 105
    for i in range(0, 6):
        for j in range(0, 6):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, 90, 90))
            x = x+100
        y = y + 100
        x = 100
    screen.blit(font.render("Hey there,", True, (0, 0, 0)), (795, 100))
    screen.blit(font1.render("I'm Macho, I want to find gold", True, (0, 0, 0)), (795, 130))
    screen.blit(font1.render("in this dark cave but I am", True, (0, 0, 0)), (808, 150))
    screen.blit(font1.render("afraid of being eaten by", True, (0, 0, 0)), (817, 170))
    screen.blit(font1.render("Wumpus monster and also being", True, (0, 0, 0)), (799, 190))
    screen.blit(font1.render("fallen into the pit.", True, (0, 0, 0)), (835, 210))
    screen.blit(font1.render("Can you help me out find the", True, (0, 0, 0)), (802, 230))
    screen.blit(font1.render("and avoid obstacles for me?", True, (0, 0, 0)), (805, 250))
    screen.blit(font1.render("psst.........!", True, (0, 0, 0)), (795, 280))
    screen.blit(font1.render("I have an arrow to kill wumpus", True, (0, 0, 0)), (795, 300))
    screen.blit(font1.render("and pits cannot be bigger", True, (0, 0, 0)), (815, 320))
    screen.blit(font1.render("than one square place. I can", True, (0, 0, 0)), (800, 340))
    screen.blit(font1.render("sense adjacent tiles, breeze ", True, (0, 0, 0)), (800, 360))
    screen.blit(font1.render("if pit is present and stench", True, (0, 0, 0)), (800, 380))
    screen.blit(font1.render("if wumpus and glitter if gold", True, (0, 0, 0)), (798, 400))
    screen.blit(font1.render("THANK YOU FOR HELPING ME! :)", True, (0, 0, 0)), (800, 430))
    screen.blit(font2.render("Wumpus World", True, (255, 255, 0)), (280, 10))
    for event in pygame.event.get():

        if (event.type == pygame.QUIT):
            pygame.quit()
            sys.exit()

        if (event.type == pygame.KEYDOWN):

            if(event.key == pygame.K_SPACE): 
                selected_keys = 1   
                key = (key + 1)%2

            if(event.key == pygame.K_r):
                game_call()

            if(key == 1 and player.arrow == 1):

                if(event.key == pygame.K_UP):
                    selected_keys = 3
                    player.arrow = 0
                    if(player.xpos != 0 and __gamemap__[player.xpos - 1][player.ypos].monster == True):
                        __gamemap__[player.xpos - 1][player.ypos].monster = False
                        disable_monster([player.xpos -1, player.ypos])

                if(event.key == pygame.K_DOWN):
                    selected_keys = 4
                    player.arrow = 0
                    if(player.xpos != 5 and __gamemap__[player.xpos + 1][player.ypos].monster == True):
                        __gamemap__[player.xpos + 1][player.ypos].monster = False
                        disable_monster([player.xpos +1, player.ypos])

                if(event.key == pygame.K_LEFT):
                    player.arrow = 0
                    selected_keys = 5
                    if(player.ypos != 0 and __gamemap__[player.xpos][player.ypos - 1].monster == True):
                        __gamemap__[player.xpos][player.ypos - 1].monster = False
                        disable_monster([player.xpos, player.ypos - 1])

                if(event.key == pygame.K_RIGHT):
                    player.arrow = 0
                    selected_keys = 6
                    if(player.ypos != 5 and __gamemap__[player.xpos][player.ypos + 1].monster == True):
                        __gamemap__[player.xpos][player.ypos + 1].monster = False
                        disable_monster([player.xpos, player.ypos + 1])

            if(key == 0):

                if(event.key == pygame.K_UP and player_ypos != 140):
                    selected_keys = 7
                    player.pos[player.xpos][player.ypos] = 0
                    disable(player.player_position())
                    player.xpos = player.xpos - 1
                    player.pos[player.xpos][player.ypos] = 1
                    enable(player.player_position())
                    player_ypos = player_ypos - 100

                if(event.key == pygame.K_DOWN and player_ypos != 640):
                    selected_keys = 8
                    player.pos[player.xpos][player.ypos] = 0
                    disable(player.player_position())
                    player.xpos = player.xpos + 1
                    player.pos[player.xpos][player.ypos] = 1
                    enable(player.player_position())
                    player_ypos = player_ypos + 100

                if(event.key == pygame.K_LEFT and player_xpos != 135):
                    selected_keys = 9
                    player.pos[player.xpos][player.ypos] = 0
                    disable(player.player_position())
                    player.ypos = player.ypos - 1
                    player.pos[player.xpos][player.ypos] = 1
                    enable(player.player_position())
                    player_xpos = player_xpos - 100

                if(event.key == pygame.K_RIGHT and player_xpos != 635):
                    selected_keys = 10
                    player.pos[player.xpos][player.ypos] = 0
                    disable(player.player_position())
                    player.ypos = player.ypos + 1
                    player.pos[player.xpos][player.ypos] = 1
                    enable(player.player_position())
                    player_xpos = player_xpos + 100

    screen.blit(font.render(f"Sensory Mind", True, (0, 0, 0)), (850, 500))

    if(__gamemap__[player.xpos][player.ypos].monster == True):
        screen.blit(font1.render(f"Death by stinky teeths!!", True, (255, 0, 0)), (820, 640))
        key = 3

    if(__gamemap__[player.xpos][player.ypos].pit == True):
        screen.blit(font1.render(f"You died jumping into hell!", True, (255, 0, 0)), (810, 640))
        key = 3

    if(__gamemap__[player.xpos][player.ypos].gold == True):
        screen.blit(font1.render(f"Lottery! glittery guilty gold!", True, (255, 255, 0)), (795, 640))
        key = 3

    if(__gamemap__[player.xpos][player.ypos].breeze == True):
        screen.blit(font.render(f"Breeze : True", True, (255, 0, 0)), (840, 530))
    else:
        screen.blit(font.render(f"Breeze : False", True, (0, 0, 0)), (840, 530))

    if(__gamemap__[player.xpos][player.ypos].stench == True):
        screen.blit(font.render(f"Stench : True", True, (255, 0, 0)), (840, 550))
    else:
        screen.blit(font.render(f"Stench : False", True, (0, 0, 0)), (840, 550))

    if(__gamemap__[player.xpos][player.ypos].glitter == True):
        screen.blit(font.render(f"Glitter : True", True, (255, 255, 0)), (828, 570))
    else:
        screen.blit(font.render(f"Glitter : False", True, (0, 0, 0)), (828, 570))

    if(key != 0):
        screen.blit(font.render(f"Arrow : {player.arrow}", True, (0, 0, 153)), (852, 590))
    else:
        screen.blit(font.render(f"Arrow : {player.arrow}", True, (0, 0, 0)), (852, 590))


    if(selected_keys == 3):
        screen.blit(font1.render(f"Shot Up", True, (0, 0, 0)), (890, 675))
    elif(key == 3):
        screen.blit(font1.render(f"Press R to Restart", True, (0, 0, 0)), (850, 675))
    elif(selected_keys == 4):
        screen.blit(font1.render(f"Shot Down", True, (0, 0, 0)), (886, 675))
    elif(selected_keys == 5):
        screen.blit(font1.render(f"Shot Left", True, (0, 0, 0)), (886, 675))
    elif(selected_keys == 6):
        screen.blit(font1.render(f"Shot Right", True, (0, 0, 0)), (889, 675))
    elif(selected_keys == 1 and key == 0):
        screen.blit(font1.render(f"Arrow Unselected", True, (0, 0, 0)), (860, 675))
    elif(selected_keys == 1 and key == 1):
        screen.blit(font1.render(f"Arrow Selected", True, (0, 0, 0)), (868, 675))
    elif(selected_keys == 7):
        screen.blit(font1.render(f"Moved Up", True, (0, 0, 0)), (887, 675))
    elif(selected_keys == 8):
        screen.blit(font1.render(f"Moved Down", True, (0, 0, 0)), (882, 675))
    elif(selected_keys == 9):
        screen.blit(font1.render(f"Moved Left", True, (0, 0, 0)), (882, 675))
    elif(selected_keys == 10):
        screen.blit(font1.render(f"Moved Right", True, (0, 0, 0)), (880, 675))


    pygame.draw.rect(screen, (255, 0, 0),pygame.Rect(player_xpos, player_ypos, 20, 20))

    pygame.display.update()
    fpsclock.tick(FPS)
