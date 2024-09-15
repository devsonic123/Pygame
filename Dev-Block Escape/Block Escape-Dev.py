#Dev Patel
import pygame, math,random

#Pygame Global Variables
WIDTH, HEIGHT = (1280, 720) #size of the screen
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) #the surface that everything is drawn on
FPS = 60

#calls all init functions
def init():
    '''This function is used to initialize variables or objects before the game begins'''
    initLevelandCookies()
    loadAssets()
    initFont()
    initSound()
    initStates()
    initGrid()
    initTimer()
    initTitleCookie()
    initCookiePos()
    initSpeed()

#initilizes level and cookies
def initLevelandCookies():
    global Level, Cookies
    Level = 1
    Cookies = 0

#loads assets like playerblock, enemyblock,etc
def loadAssets():
    global lists, font, gameState, bg, title,congrats, CHECKEREDBLOCK, JAILBLOCK, DEATHBLOCK, PLAYERBLOCK, WALLBLOCK, WARPBLOCK, ENEMYBLOCK, cookie
    lists = []
    bg = pygame.image.load("bg.png")
    congrats = pygame.image.load("congrats.png")
    title = pygame.image.load("menu.png")
    image = pygame.image.load("checkeredblock.png")
    lists.append(image)
    image = pygame.image.load("jailblock.png")
    lists.append(image)
    image = pygame.image.load("deathblock.png")
    lists.append(image)
    image = pygame.image.load("playerblock.png")
    lists.append(image)
    image = pygame.image.load("wallblock.png")
    lists.append(image)
    image = pygame.image.load("warpblock.png")
    lists.append(image)
    image = pygame.image.load("enemyblock.png")
    lists.append(image)
    cookie = pygame.image.load("cookie.png")
    CHECKEREDBLOCK, JAILBLOCK, DEATHBLOCK, PLAYERBLOCK, WALLBLOCK, WARPBLOCK, ENEMYBLOCK = (0,1,2,3,4,5,6)

#initializes font
def initFont():
    global font
    font= pygame.font.SysFont(None,75)

#initializes sound
def initSound():
    global playerMove,playerEat, enemyEat, timerSound, deathSound, goalUnlocks,levelPass
    playerMove = pygame.mixer.Sound("playerMovment.wav")
    playerEat = pygame.mixer.Sound("playerEat.wav")
    enemyEat = pygame.mixer.Sound("enemyEat.wav")
    timerSound = pygame.mixer.Sound("Timer.wav")
    deathSound = pygame.mixer.Sound("Death.wav")
    goalUnlocks = pygame.mixer.Sound("goalUnlocks.wav")
    levelPass = pygame.mixer.Sound("LevelPass.wav")

#creates gameStates
def initStates():
    global TITLE, PLAY, gameState, WIN, LOSE, CONGRATS
    TITLE = 0
    PLAY = 1
    LOSE = 2
    WIN = 3
    CONGRATS = 4
    gameState =TITLE

#reads the text file and puts it into a string. Finds player and enemy
def initGrid():
    global grid, gridPos, widthSpacing, heightSpacing, gridx, gridy, cookiex,row, cookiey,pIndexY,pIndexX, EIndexX, EIndexY
    grid = []
    if Level == 1:
        with open("level1.txt", 'r') as fh:
            for line in fh:
                row = []
                for char in line.strip():
                    row.append(char)
                grid.append(row)
        initGridPos1()
    elif Level == 2:
        with open("level2.txt", 'r') as fh:
            for line in fh:
                row = []
                for char in line.strip():
                    row.append(char)
                grid.append(row)
        initGridPos2()
    elif Level == 3:
        with open("level3.txt", 'r') as fh:
            for line in fh:
                row = []
                for char in line.strip():
                    row.append(char)
                grid.append(row)
        initGridPos3()
    FindPlayerWallGate()
    FindEnemy()

#initalizes level1 grid
def initGridPos1():
    global grid1Pos, grid1x, grid1y, widthSpacing, heightSpacing
    grid1x = HEIGHT / 2 - 180
    grid1y = WIDTH / 2 - 200
    grid1Pos = (grid1x, grid1y)
    widthSpacing = 32
    heightSpacing = 33
#initalizes level2 grid
def initGridPos2():
    global grid2Pos, grid2x, grid2y, widthSpacing, heightSpacing
    grid2x = HEIGHT / 2 - 180
    grid2y = WIDTH / 2 - 250
    grid2Pos = (grid2x, grid2y)
    widthSpacing = 32
    heightSpacing = 33
#initalizes level3 grid
def initGridPos3():
    global grid3Pos, grid3x, grid3y, widthSpacing, heightSpacing
    grid3x = HEIGHT / 2 - 180
    grid3y = WIDTH / 2 - 350
    grid3Pos = (grid3x, grid3y)
    widthSpacing = 32
    heightSpacing = 33

#finds player postion, gate position, and interior wall postions
def FindPlayerWallGate():
    global pIndexX, pIndexY, gateIndexX, gateIndexY,wallIndexX, wallIndexY
    pIndexY = -1
    pIndexX = -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "p":
                pIndexX = i
                pIndexY = j
                break
            elif grid[i][j] == "e":
                gateIndexX = i
                gateIndexY = j
            elif grid[i][j] == "x":
                wallIndexX = i
                wallIndexY = j

#Finds enemy positions
def FindEnemy():
    global e1IndexX, e1IndexY, enemyPos, e2IndexX, e2IndexY,e1X,e1Y,e2X,e2Y
    e1X = []
    e1Y = []
    e2X = []
    e2Y = []
    e1IndexY = -1
    e1IndexX = -1
    e2IndexY = -1
    e2IndexX = -1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                e1IndexX = i
                e1IndexY = j
                e1X.append(e1IndexX)
                e1Y.append(e1IndexY)
            elif grid[i][j] == "2":
                e2IndexX = i
                e2IndexY = j
                e2X.append(e2IndexX)
                e2Y.append(e2IndexY)
                break

#initaites timer
def initTimer():
    global timer, seconds
    timer = 0
    seconds = math.ceil(len(grid) * len(grid[0]) * 0.15)

#makes the title cookie selector
def initTitleCookie():
    global pos1, pos2, pos
    pos1 = (WIDTH / 2 - 125, HEIGHT / 2 - 75)
    pos2 = (WIDTH / 2 - 125, HEIGHT / 2)
    pos = pos1

#initalizes the cookie position when gamestate is PLAY
def initCookiePos():
    global cookiex, cookiey
    if Level == 1:
        cookiex = random.randint(1,len(grid) - 4)
        cookiey = random.randint(1,len(grid[0]) - 4)
    elif Level == 2:
        cookiex = random.randint(1, len(grid) - 4)
        cookiey = random.randint(1, len(grid[0]) - 4)
    elif Level == 3:
        cookiex = random.randint(1, len(grid) - 3)
        cookiey = random.randint(1, len(grid[0])- 3)

#initalizes variables for enemy speed
def initSpeed():
    global xspeed1,xspeed2,xspeed3, yspeed1,yspeed2
    xspeed1 = 1
    xspeed2 = 1
    xspeed3 = 1
    yspeed1 = 1
    yspeed2 = 1

# calls all update functions
def update():
    '''This function is used to modify the data portions of things shown on screen'''
    if gameState == PLAY:
        updateTimer()
        updateCookieCounter()
        if timer % 30 == 0:
            Enemy1Movement_1()
            Enemy1Movement_2()
            Enemy1Movement_3()
        if timer % 20 == 0:
            Enemy2Movement_1()
            Enemy2Movement_2()

#changes seconds when timer is 60 and makes the sound for the player dying
def updateTimer():
    global timer, seconds,gameState, Cookies
    if gameState == PLAY:
        if timer % 60 == 0:
            seconds = seconds - 1
            if seconds == 0:
                deathSound.play()

#Tells when the player or enemy eats a cookie(makes sound) and changes the jail block to a checkered block
def updateCookieCounter():
    global Cookies, JAILBLOCK
    if pIndexX == cookiex and pIndexY == cookiey:
        Cookies= Cookies + 1
        initCookiePos()
        playerEat.play()
        if Cookies >= 5:
            goalUnlocks.play()
            JAILBLOCK = CHECKEREDBLOCK

    elif e1IndexX == cookiex and e1IndexY == cookiey or e2IndexX == cookiex and e2IndexY == cookiey:
        initCookiePos()
        enemyEat.play()

#Makes the enemy move from left to right in a loop for first 1  enemy
def Enemy1Movement_1():
        global grid, e1IndexX, e1IndexY, enemy1Pos,xspeed1
        length = len(grid)
        if Level == 1:
            enemy1Pos = e1IndexY + xspeed1
            temp = grid[e1IndexX][e1IndexY]
            grid[e1IndexX][e1IndexY] = grid[e1IndexX][enemy1Pos]
            grid[e1IndexX][enemy1Pos] = temp
            e1IndexY = e1IndexY + xspeed1
            if e1IndexY <= 1:
                xspeed1 = xspeed1 * -1
            if e1IndexY >= length:
                xspeed1 = xspeed1 * -1
        elif Level == 2:
            enemy1Pos = e1IndexY + xspeed1
            temp = grid[e1IndexX][e1IndexY]
            grid[e1IndexX][e1IndexY] = grid[e1IndexX][enemy1Pos]
            grid[e1IndexX][enemy1Pos] = temp
            e1IndexY = e1IndexY + xspeed1
            if e1IndexY <= 1:
                xspeed1 = xspeed1 * -1
            if e1IndexY >= length + 3:
                xspeed1 = xspeed1 * -1
        elif Level == 3:
            enemy1Pos = e1IndexY + xspeed1
            temp = grid[e1IndexX][e1IndexY]
            grid[e1IndexX][e1IndexY] = grid[e1IndexX][enemy1Pos]
            grid[e1IndexX][enemy1Pos] = temp
            e1IndexY = e1IndexY + xspeed1
            if e1IndexY <= 1:
                xspeed1 = xspeed1 * -1
            if e1IndexY >= length + 6:
                xspeed1 = xspeed1 * -1

#makes enemy move left to right if there are two 1 type enemies
def Enemy1Movement_2():
    global enemy1Pos, grid, xspeed2, e1Y, e1X
    length = len(grid)
    if e1Y != [] and Level ==2 or e1Y !=[] and Level == 3:
        enemy1Pos = e1Y[0] + xspeed2
        if grid[e1X[0]][enemy1Pos] == "_":
            temp = grid[e1X[0]][e1Y[0]]
            grid[e1X[0]][e1Y[0]] = grid[e1X[0]][enemy1Pos]
            grid[e1X[0]][enemy1Pos] = temp
            e1Y[0] = e1Y[0] + xspeed2
            if e1Y[0] <= 1:
                xspeed2 = xspeed2 * -1
            if e1Y[0] >= length + 3:
                xspeed2 = xspeed2 * -1

#makes enemy move left to right if there are three 1 type enemies
def Enemy1Movement_3():
    global enemy1Pos, grid, xspeed3, e1Y, e1X
    length = len(grid)
    if e1Y !=[] and Level == 3:
        enemy1Pos = e1Y[1] + xspeed3
        if grid[e1X[1]][enemy1Pos] == "_":
            temp = grid[e1X[1]][e1Y[1]]
            grid[e1X[1]][e1Y[1]] = grid[e1X[1]][enemy1Pos]
            grid[e1X[1]][enemy1Pos] = temp
            e1Y[1] = e1Y[1] + xspeed3
            if e1Y[1] <= 1:
                xspeed3 = xspeed3 * -1
            if e1Y[1] >= length + 4:
                xspeed3 = xspeed3 * -1

#makes enemy move left to right for first 2 type enemies
def Enemy2Movement_1():
        global grid, e2IndexX, e2IndexY, enemy2Pos,yspeed1
        length = len(grid[0])
        if Level == 2:
            enemy2Pos = e2IndexX + yspeed1
            temp = grid[e2IndexX][e2IndexY]
            grid[e2IndexX][e2IndexY] = grid[enemy2Pos][e2IndexY]
            grid[enemy2Pos][e2IndexY] = temp
            e2IndexX = e2IndexX + yspeed1
            if e2IndexX <= 1:
                yspeed1 = yspeed1 * -1
            if e2IndexX >= length - 7:
                yspeed1 = yspeed1 * -1
        if Level == 3:
            enemy2Pos = e2IndexX + yspeed1
            temp = grid[e2IndexX][e2IndexY]
            grid[e2IndexX][e2IndexY] = grid[enemy2Pos][e2IndexY]
            grid[enemy2Pos][e2IndexY] = temp
            e2IndexX = e2IndexX + yspeed1
            if e2IndexX <= 1:
                yspeed1 = yspeed1 * -1
            if e2IndexX >= length - 10:
                yspeed1 = yspeed1 * -1
#makes enemy move left to right if there are two 2 type enemies
def Enemy2Movement_2():
    global grid, e2IndexX, e2IndexY, enemy2Pos, yspeed2, e2X,e2Y
    length = len(grid[0])
    if e2Y != [] and Level == 3:
        enemy2Pos = e2X[0] + yspeed2
        if grid[e2X[0]][enemy2Pos] == "_":
            temp = grid[e2X[0]][e2Y[0]]
            grid[e2X[0]][e2Y[0]] = grid[e2X[0]][enemy2Pos]
            grid[e2X[0]][enemy2Pos] = temp
            e2X[0] = e2X[0] + yspeed2
            if e2X[0] <= 1:
                yspeed2 = yspeed2 * -1
            if e2X[1] >= length - 10:
                yspeed2 = yspeed2 * -1

#calls all draw functions
def draw():
    '''This function is used to draw things onto the screen'''
    drawBackground()
    drawGrid()
    drawTimer()
    drawLevelandCookies()
    drawTitleCookie()
    drawLose()
    drawWin()
    pygame.display.flip() #should always be the last line in this function

#draws background
def drawBackground():
    if gameState == TITLE:
        SCREEN.blit(title,(0,0))

    if gameState != TITLE:
        SCREEN.blit(bg,(0,0))
#draws all the grid for each level
def drawGrid():
    drawGrid1()
    drawGrid2()
    drawGrid3()

#draws grid for first level and makes sure its in the center of the screen
def drawGrid1():
    global seconds,row,col,row1, gameState,Cookies,seconds,grid1Pos
    if gameState != TITLE and Level == 1:
        totalrows = len(grid)
        totalCols = len(grid[0])
        for i in range(totalrows):
            for j in range(totalCols):
                block = grid[i][j]
                row1 = grid1Pos[0] + heightSpacing * i
                col = grid1Pos[1] + widthSpacing * j
                if block == "x":
                    SCREEN.blit(lists[WALLBLOCK], (col, row1))
                elif block == "e":
                    if gameState != WIN:
                        SCREEN.blit(lists[JAILBLOCK], (col, row1))
                        if Cookies >= 5:
                            SCREEN.blit(lists[CHECKEREDBLOCK], (col, row1))
                elif block == "_":
                    SCREEN.blit(cookie, (cookiey * heightSpacing + grid1Pos[1], cookiex * widthSpacing + grid1Pos[0]))
                elif block == "p":
                    SCREEN.blit(lists[PLAYERBLOCK], (col, row1))
                    if seconds == 0:
                        drawDeathBlock()
                        gameState = LOSE
                    playerDie()
                if gameState != LOSE:
                    if block == "1":
                        SCREEN.blit(lists[ENEMYBLOCK], (col, row1))
                    elif block == "2":
                        SCREEN.blit(lists[ENEMYBLOCK], (col, row1))

#draws grid for second level and makes sure its in the center of the screen
def drawGrid2():
    global seconds, row, col, row1, gameState,Cookies, seconds,grid2Pos
    if gameState != TITLE and Level == 2:
        totalrows = len(grid)
        totalCols = len(grid[0])
        for i in range(totalrows):
            for j in range(totalCols):
                block = grid[i][j]
                row1 = grid2Pos[0] + heightSpacing * i
                col = grid2Pos[1] + widthSpacing * j
                if block == "x":
                    SCREEN.blit(lists[WALLBLOCK], (col, row1))
                elif block == "e":
                    if gameState != WIN:
                        SCREEN.blit(lists[JAILBLOCK], (col, row1))
                        if Cookies >= 5:
                            SCREEN.blit(lists[CHECKEREDBLOCK], (col, row1))
                elif block == "_":
                    SCREEN.blit(cookie, (cookiey * heightSpacing + grid2Pos[1], cookiex * widthSpacing + grid2Pos[0]))
                elif block == "p":
                    SCREEN.blit(lists[PLAYERBLOCK], (col, row1))
                    if seconds == 0:
                        drawDeathBlock()
                        gameState = LOSE
                    playerDie()
                if gameState != LOSE:
                    if block == "1":
                        SCREEN.blit(lists[ENEMYBLOCK], (col, row1))
                    elif block == "2":
                        SCREEN.blit(lists[ENEMYBLOCK], (col, row1))

#draws grid third first level and makes sure its in the center of the screen
def drawGrid3():
    global seconds, row, col, row1, gameState,Cookies,seconds,grid3Pos,JAILBLOCK
    if gameState != TITLE  and Level == 3:
        totalrows = len(grid)
        totalCols = len(grid[0])
        for i in range(totalrows):
            for j in range(totalCols):
                block = grid[i][j]
                row1 = grid3Pos[0] + heightSpacing * i
                col = grid3Pos[1] + widthSpacing * j
                if block == "x":
                    SCREEN.blit(lists[WALLBLOCK], (col, row1))
                elif block == "e":
                    if gameState != WIN:
                        SCREEN.blit(lists[JAILBLOCK], (col, row1))
                        if Cookies >= 5:
                            SCREEN.blit(lists[CHECKEREDBLOCK], (col, row1))
                elif block == "_":
                    SCREEN.blit(cookie, (cookiey * heightSpacing + grid3Pos[1], cookiex * widthSpacing + grid3Pos[0]))
                elif block == "p":
                    SCREEN.blit(lists[PLAYERBLOCK], (col, row1))
                    if seconds == 0:
                        drawDeathBlock()
                        gameState = LOSE
                    playerDie()
                if gameState != LOSE:
                    if block == "1":
                        SCREEN.blit(lists[ENEMYBLOCK], (col, row1))
                    elif block == "2":
                        SCREEN.blit(lists[ENEMYBLOCK], (col, row1))

#draws death block
def drawDeathBlock():
    global col , row1
    SCREEN.blit(lists[DEATHBLOCK], (col, row1))

#sees if the player collides with enemy
def playerDie():
    global gameState
    if pIndexX == e1IndexX and pIndexY == e1IndexY or e2IndexX == pIndexX and e2IndexY == pIndexY:
        drawDeathBlock()
        gameState = LOSE

#draws timer on screen and makes it red when hiting 3(sound plays)
def drawTimer():
    if gameState != TITLE:
        if seconds > 3:
            timerImg = font.render(str(seconds), True, (255,255,255))
            SCREEN.blit(timerImg, (400,25))
        else:
            timerImg = font.render(str(seconds), True, (255, 0,0))
            SCREEN.blit(timerImg, (400, 25))
        if seconds == 3 or seconds == 2:
            timerSound.play()

#draws the number of cookies and what level you are on
def drawLevelandCookies():
    if gameState != TITLE:
        levelImg = font.render(str(Level), True, (255,255,255))
        SCREEN.blit(levelImg, (725,25))
        cookieImg = font.render(str(Cookies), True, (255,255,255))
        SCREEN.blit(cookieImg, (1100,25))

#Draws the title cookie
def drawTitleCookie():
    global pos,pos1,pos2
    if gameState == TITLE:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            pos = pos2
        elif keys [pygame.K_UP]:
            pos = pos1
        SCREEN.blit(cookie,pos)

#draws the lose state
def drawLose():
    if gameState == LOSE:
        loseImg = font.render("Press p to play again or press q to quit",True, (255,255,255))
        SCREEN.blit(loseImg,(190,100))

#draws the win state
def drawWin():
    if gameState == WIN:
        winImg = font.render("Press Enter for new level", True, (255, 255, 255))
        SCREEN.blit(winImg, (350, 100))

    if gameState == CONGRATS:
        SCREEN.blit(congrats, (0, 0))

#makes player move according to keyboard inputs
def handlePlayerMovement():
    global grid, pIndexX, pIndexY,keys,playerPos
    keys = pygame.key.get_pressed()
    if gameState == PLAY:
        if keys[pygame.K_DOWN]:
            playerPos = pIndexX + 1
            length = len(grid)
            if playerPos < length - 1 or pIndexX!= wallIndexX and pIndexY != wallIndexY:
                if grid[playerPos][pIndexY] == "_" or "1":
                    temp = grid[pIndexX][pIndexY]
                    grid[pIndexX][pIndexY] = grid[playerPos][pIndexY]
                    grid[playerPos][pIndexY] = temp
                    pIndexX = pIndexX + 1
                    playerMove.play()

        elif keys[pygame.K_UP]:
            playerPos = pIndexX - 1
            if playerPos > 0:
                if grid[playerPos][pIndexY] == "_" or "1":
                    temp = grid[pIndexX][pIndexY]
                    grid[pIndexX][pIndexY] = grid[playerPos][pIndexY]
                    grid[playerPos][pIndexY] = temp
                    pIndexX = pIndexX - 1
                    playerMove.play()

        elif keys[pygame.K_LEFT]:
            playerPos = pIndexY - 1
            if playerPos > 0:
                if grid[pIndexX][playerPos] == "_" or "1":
                    temp = grid[pIndexX][pIndexY]
                    grid[pIndexX][pIndexY] = grid[pIndexX][playerPos]
                    grid[pIndexX][playerPos] = temp
                    pIndexY = pIndexY - 1
                    playerMove.play()

        elif keys[pygame.K_RIGHT]:
            playerPos = pIndexY + 1
            playerrightBoundaries()
            playerMove.play()

#used to make different boundaries to make player move all the way right(my grid changes if level changes)
def playerrightBoundaries():
    global pIndexY
    length = len(grid)
    if Level == 1:
        if playerPos < length + 1:
            if grid[pIndexX][playerPos] == "_":
                temp = grid[pIndexX][pIndexY]
                grid[pIndexX][pIndexY] = grid[pIndexX][playerPos]
                grid[pIndexX][playerPos] = temp
                pIndexY = pIndexY + 1
    elif Level == 2:
        if playerPos < length + 4:
            if grid[pIndexX][playerPos] == "_":
                temp = grid[pIndexX][pIndexY]
                grid[pIndexX][pIndexY] = grid[pIndexX][playerPos]
                grid[pIndexX][playerPos] = temp
                pIndexY = pIndexY + 1
    elif Level == 3:
        if playerPos < length + 7:
            if grid[pIndexX][playerPos] == "_":
                temp = grid[pIndexX][pIndexY]
                grid[pIndexX][pIndexY] = grid[pIndexX][playerPos]
                grid[pIndexX][playerPos] = temp
                pIndexY = pIndexY + 1

#checks to see if player has reacher the goal
def playerFinish():
    global playerPos, pIndexX, CHECKEREDBBLOCK, JAILBLOCK, pIndexY,gameState
    if Cookies >=5:
        keys = pygame.key.get_pressed()
        playerPos = pIndexX - 1
        if playerPos == gateIndexX and pIndexY == gateIndexY:
            if keys[pygame.K_UP]:
                temp = grid[pIndexX][pIndexY]
                grid[pIndexX][pIndexY] = grid[playerPos][pIndexY]
                grid[playerPos][pIndexY] = temp
                pIndexX = pIndexX - 1
                levelPass.play()
                gameState = WIN

#calls all the fucntions
def main():
    global gameState,timer,Level,pos,seconds,Cookies,JAILBLOCK
    pygame.init()
    init()
    isRunning = True
    clock = pygame.time.Clock()

    while isRunning:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == pygame.KEYDOWN:
                handlePlayerMovement()
                playerFinish()
                #resets all game stats when start over
                if event.key == pygame.K_p and gameState == LOSE:
                    Level = 1
                    initGrid()
                    seconds = math.ceil(len(grid) * len(grid[0]) * 0.15)
                    Cookies = 0
                    JAILBLOCK = 1
                    gameState = PLAY
                #quits game
                elif event.key == pygame.K_q and gameState == LOSE:
                    isRunning = False
                #starts game
                if event.key == pygame.K_RETURN and gameState == TITLE and pos == pos1:
                    gameState = PLAY
                #quits game
                elif event.key == pygame.K_RETURN and gameState == TITLE and pos == pos2:
                    isRunning = False
                #changes level
                if event.key == pygame.K_RETURN and gameState == WIN:
                    Level = Level + 1
                    seconds = math.ceil(len(grid) * len(grid[0]) * 0.15)
                    Cookies = 0
                    initGrid()
                    gameState = PLAY
                    JAILBLOCK = 1
                #starts game over if they win
                if event.key == pygame.K_r and gameState == CONGRATS:
                    gameState = TITLE
                    Cookies = 0
                    Level = 1
                    initGrid()
                    seconds = math.ceil(len(grid) * len(grid[0]) * 0.15)
                #quits game
                elif event.key == pygame.K_q and gameState == CONGRATS:
                    isRunning = False
            #gives user the congrats screen
            if Level == 3 and gameState == WIN:
                gameState = CONGRATS
        update()
        draw()
        timer = timer + 1
    pygame.quit()
if __name__ == "__main__":
    main()


