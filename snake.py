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
    def __init__(self, x, y):
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

    def printPos(self):
        print(self.body)
        return


class Pill:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def render_pos(self):
        return (self.x * 10, self.y * 10)

    def __repr__(self):
        pass #TODO


class Game:
    screen_width=400
    screen_height=400
    grid_width = 40
    grid_height = 40

    def __init__(self):
        self.player = Player(20, 20)
        self.pill = Pill(0, 0)

    def RestartGame(self):
        self.player = Player(20, 20)
        self.pill = Pill(0, 0)

    def StartOnKeyPress(self):
        print("waiting for key")
        pygame.event.clear()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    return

    def Run(self):
        window = self.CreateWindow()
        self.SummonPill()
        self.DisplayPill(window)
        prev_move = self.player.moveUp

        self.StartOnKeyPress()
        while True:
            prev_move = self.MovePlayerWithCapturedKey(prev_move, self.player.direction)
            if self.IsPlayerEatsPill(self.player, self.pill):
                self.player.length += 1
                self.SummonPill()
                self.DisplayPill(window)
                continue
            if self.IsPlayerDead(self.player):
                print("Game Over!")
                self.RestartGame()
                break
            tail = self.player.body.pop()

            # render next state
            self.DisplayPlayer(self.player, tail, window)

            # clock 
            time.sleep(0.1)

    def IsPlayerEatsPill(self, player, pill):
        return (player.x is pill.x and player.y is pill.y)

    def IsPlayerDead(self, player):
        return self.IsSelfCollide(player) or self.IsOutOfBoundary(player)

    def IsSelfCollide(self, player):
        #print("Self Collide")
        return ((player.x, player.y) in list(player.body)[2:])

    def IsOutOfBoundary(self, player):
        #print("Out of Boundary!")
        return (player.x >= self.grid_width or player.y >= self.grid_height 
                or player.x < 0 or player.y < 0)

    def SummonPill(self):
        self.pill = Pill(random.randrange(self.grid_width), random.randrange(self.grid_height))

    def CreateWindow(self):
        window = pygame.display.set_mode([self.screen_width, self.screen_height])
        window.fill((255, 255, 255))
        return window

    def DisplayPill(self, window):
        pill_image = pygame.Surface((10, 10))
        pill_image.fill((0, 255, 0))
        window.blit(pill_image, self.pill.render_pos())
        pygame.display.update()

    def DisplayPlayer(self, player, tail,  window):
        self.ErasePlayerOldTail(tail, window)
        self.DisplayPlayerNewHead(player, window)
        pygame.display.update()

    def ErasePlayerOldTail(self, tail, window):
        player_image = pygame.Surface((10, 10))
        player_image.fill((255, 255, 255)) 
        window.blit(player_image, (tail[0] * 10, tail[1] * 10)) 

    def DisplayPlayerNewHead(self, player, window):
        player_image = pygame.Surface((10, 10))
        player_image.fill((0, 0, 0))
        for pos in player.body:
            window.blit(player_image, (pos[0] * 10, pos[1] * 10))

    def MovePlayerWithCapturedKey(self, prev_move, direction):
        pygame.event.pump()
        keys = pygame.key.get_pressed()

        if(keys[K_RIGHT] and direction is not Direction.LEFT):
            prev_move = self.player.moveRight
        if(keys[K_LEFT] and direction is not Direction.RIGHT):
            prev_move = self.player.moveLeft
        if(keys[K_UP] and direction is not Direction.DOWN):
            prev_move = self.player.moveUp
        if(keys[K_DOWN] and direction is not Direction.UP):
            prev_move = self.player.moveDown
        if(keys[K_ESCAPE]):
            return sys.exit()
        prev_move()
        return prev_move

if __name__ == "__main__":
    game = Game()
    while(True):
        game.Run()

