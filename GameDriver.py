from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from Grid import Grid
from PlayerAI import PlayerAI
from Helper import canMove, ChangeToOneDimension
import pandas as pd

class GameDriver:
    def __init__(self):
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.url = 'https://www.2048.org/'
        self.driver = webdriver.Chrome(self.PATH)
        self.driver.get(self.url)
        self.body = self.driver.find_element(by=By.TAG_NAME, value="body")
        self.moves = {
            0: Keys.ARROW_UP,
            1: Keys.ARROW_DOWN,
            2: Keys.ARROW_LEFT,
            3: Keys.ARROW_RIGHT
        }

    def getGrid(self):
        matrix = [[0 for i in range(4)] for j in range(4)]
        tiles = self.driver.find_elements(by=By.CLASS_NAME, value="tile")
        try:
            for tile in tiles:
                cls = tile.get_attribute('class')
                col, row = cls.split('tile-position-')[1].split(' ')[0].split('-')
                col, row = int(col) - 1, int(row) - 1
                num = int(cls.split('tile tile-')[1].split(' ')[0])
                if num > matrix[row][col]:
                    matrix[row][col] = num

            grid = Grid()
            return grid.makeGrid(matrix)
        except StaleElementReferenceException:
            tiles = self.driver.find_elements(by=By.CLASS_NAME, value="tile")
            for tile in tiles:
                cls = tile.get_attribute('class')
                col, row = cls.split('tile-position-')[1].split(' ')[0].split('-')
                col, row = int(col) - 1, int(row) - 1
                num = int(cls.split('tile tile-')[1].split(' ')[0])
                if num > matrix[row][col]:
                    matrix[row][col] = num

            grid = Grid()
            return grid.makeGrid(matrix)

    def move(self, moveCode):
        try:
            self.body.send_keys(self.moves[moveCode])
        except StaleElementReferenceException:
            self.body = self.driver.find_element(by=By.TAG_NAME, value="body")
            self.body.send_keys(self.moves[moveCode])

    def quit(self):
        self.driver.close()

    def keepGoing(self):
        try:
            self.driver.find_element(By.CLASS_NAME,'keep-playing-button').click()
        except NoSuchElementException:
            pass
        except ElementNotInteractableException:
            pass
        

func = str(input('Expectimax or Minimax?\n'))
d = int(input('Depth: \n'))
solanChoi = int(input('How many times do you want to play?\n'))

dct_plays = dict()
count_plays = 1

def playExpectimax():
    global dct_plays, count_plays, solanChoi, d

    while count_plays <= solanChoi:
        
        gameDriver = GameDriver()
        moves_count = 1

        score = 0
        maxTile = 0
        t1 = time.time()
        while True:
            gameDriver.keepGoing()
            grid = gameDriver.getGrid()

            grid_1D = ChangeToOneDimension(grid)
            if not canMove(grid_1D):
                
                maxTile = grid.getMaxTile()
                print("Lose the game")
                time.sleep(4)
                score = int(gameDriver.driver.find_element(By.CLASS_NAME,'score-container').text)
                gameDriver.quit()
                break
                
            playerAI = PlayerAI(d)
            moveCode = playerAI.getMoveExpectimax(grid)
            gameDriver.move(moveCode)
            moves_count += 1
            
        t2 = time.time()
        t = round(t2 - t1,2)
        dct_plays[count_plays] = [score,maxTile,moves_count,t]

        print('Play '+str(count_plays))
        print('Score:',score)
        print('Max Tile:',maxTile)
        print('Moves:',moves_count)
        print('Time:',t)
        print('\n\n\n')
        count_plays += 1
    

def playMinimax():
    global dct_plays, count_plays, solanChoi, d

    while count_plays <= solanChoi:
        
        gameDriver = GameDriver()
        moves_count = 1

        score = 0
        maxTile = 0
        t1 = time.time()
        while True:
            gameDriver.keepGoing()
            grid = gameDriver.getGrid()

            grid_1D = ChangeToOneDimension(grid)
            if not canMove(grid_1D):
                
                maxTile = grid.getMaxTile()
                print("Lose the game")
                time.sleep(4)
                score = int(gameDriver.driver.find_element(By.CLASS_NAME,'score-container').text)
                gameDriver.quit()
                break
                
            playerAI = PlayerAI(d)
            moveCode = playerAI.getMoveMinimax(grid)
            gameDriver.move(moveCode)
            moves_count += 1
            
        t2 = time.time()
        t = round(t2 - t1,2)
        dct_plays[count_plays] = [score,maxTile,moves_count,t]

        print('Play '+str(count_plays))
        print('Score:',score)
        print('Max Tile:',maxTile)
        print('Moves:',moves_count)
        print('Time:',t)
        print('\n\n\n')
        count_plays += 1


if func == 'Expectimax':
    playExpectimax()
elif func == 'Minimax':
    playMinimax()

data = pd.DataFrame(dct_plays)
data.columns = ['Play '+str(i) for i in data.columns]
data.index = ['Score','Max Tile','Moves','Time']
print(data)