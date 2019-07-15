import time
import random
import sys
import collections
import enum

import pygame
from pygame.locals import*


class Direction(enum.Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4


class Player:
    def __init__(self, x=5, y=5):
        self.x = x
        self.y = y 
        self.length = 1
        self.speed = 1
        self.direction = Direction.UP
        self.body = collections.deque([(self.x, self.y)])

    def moveRight(self):
        self.x = self.x + self.speed
        self.body.appendleft((self.x, self.y))
        self.direction = Direction.RIGHT

    def moveLeft(self):
        self.x = self.x - self.speed
        self.body.appendleft((self.x, self.y))
        self.direction = Direction.LEFT

    def moveUp(self):
        self.y = self.y - self.speed
        self.body.appendleft((self.x, self.y))
        self.direction = Direction.UP

    def moveDown(self):
        self.y = self.y + self.speed
        self.body.appendleft((self.x, self.y))
        self.direction = Direction.DOWN


class Pill:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.PIXEL_SIZE = 10

    def render_pos(self):
        return (self.x * self.PIXEL_SIZE, self.y * self.PIXEL_SIZE) 


class Game:
    SCREEN_WIDTH=400
    SCREEN_HEIGHT=400
    GRID_WIDTH = 40
    GRID_HEIGHT = 40

    def __init__(self):
        self.RestartGame()

    def RestartGame(self):
        self.player = Player(20, 20)
        self.pill = Pill(0, 0)

    def ContinueOnKeyPress(self):
        print("waiting for key")
        pygame.event.clear()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    return

    def Run(self):
        self.CreateWindow()
        self.SummonRandomPill()
        self.DisplayPill()
        prev_move = self.player.moveUp

        self.ContinueOnKeyPress()
        while True:
            prev_move = self.MovePlayerWithCapturedKey(prev_move, self.player.direction)
            if self.IsPlayerEatsPill(self.player, self.pill):
                self.player.length += 1
                self.SummonRandomPill()
                self.DisplayPill()
                continue
            if self.IsPlayerDead(self.player):
                print("Game Over!")
                self.ShowScore()
                self.ContinueOnKeyPress()
                break
            tail = self.player.body.pop()

            # render next state
            self.DisplayPlayer(self.player, tail)

            # clock 
            time.sleep(0.1)

    def ShowScore(self):
        pygame.init()
        score_font = pygame.font.Font('freesansbold.ttf', 32)
        score_text = score_font.render("Score: {}".format(self.player.length), True, (255, 0, 0))
        self.window.blit(score_text, score_text.get_rect() )
        pygame.display.update()
        print("Score: ", self.player.length)

    def IsPlayerEatsPill(self, player, pill):
        return player.x is pill.x and player.y is pill.y

    def IsPlayerDead(self, player):
        return self.IsSelfCollide(player) or self.IsOutOfBoundary(player)

    def IsSelfCollide(self, player):
        #print("Self Collide")
        return (player.x, player.y) in list(player.body)[2:]

    def IsOutOfBoundary(self, player):
        #print("Out of Boundary!")
        return (player.x >= self.GRID_WIDTH or player.y >= self.GRID_HEIGHT 
                or player.x < 0 or player.y < 0)

    def SummonRandomPill(self):
        self.pill = Pill(random.randrange(self.GRID_WIDTH), random.randrange(self.GRID_HEIGHT))

    def CreateWindow(self):
        self.window = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        self.window.fill((255, 255, 255))

    def DisplayPill(self):
        pill_image = pygame.Surface((10, 10))
        pill_image.fill((0, 255, 0))
        self.window.blit(pill_image, self.pill.render_pos())
        pygame.display.update()

    def DisplayPlayer(self, player, tail):
        self.ErasePlayerOldTail(tail)
        self.DisplayPlayerNewHead(player)
        pygame.display.update()

    def ErasePlayerOldTail(self, tail):
        player_image = pygame.Surface((10, 10))
        player_image.fill((255, 255, 255)) 
        self.window.blit(player_image, (tail[0] * 10, tail[1] * 10)) 

    def DisplayPlayerNewHead(self, player):
        player_image = pygame.Surface((10, 10))
        player_image.fill((0, 0, 0))
        for pos in player.body:
            self.window.blit(player_image, (pos[0] * 10, pos[1] * 10))

    def MovePlayerWithCapturedKey(self, prev_move, direction):
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        if(keys[K_RIGHT] and direction is not Direction.LEFT):
            prev_move = self.player.moveRight
        elif(keys[K_LEFT] and direction is not Direction.RIGHT):
            prev_move = self.player.moveLeft
        elif(keys[K_UP] and direction is not Direction.DOWN):
            prev_move = self.player.moveUp
        elif(keys[K_DOWN] and direction is not Direction.UP):
            prev_move = self.player.moveDown
        elif(keys[K_ESCAPE]):
            return sys.exit()
        prev_move()
        return prev_move

if __name__ == "__main__":
    while(True):
        game = Game()
        game.Run()
