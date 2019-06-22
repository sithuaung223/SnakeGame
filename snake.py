from pygame.locals import*
import pygame
import time
import random
import sys
import collections

class Player:
    x = 5
    y = 5
    length = 1
    speed = 1
    body = collections.deque([(x, y)])

    def moveRight(self):
        self.x = self.x + self.speed
        self.body.appendleft((self.x, self.y))
        self.printPos()
    def moveLeft(self):
        self.x = self.x - self.speed
        self.body.appendleft((self.x, self.y))
        self.printPos()
    def moveUp(self):
        self.y = self.y - self.speed
        self.body.appendleft((self.x, self.y))
        self.printPos()
    def moveDown(self):
        self.y = self.y + self.speed
        self.body.appendleft((self.x, self.y))
        self.printPos()
    def printPos(self):
        print(self.body)


class Pill:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("pill= x: ", self.x, "y: ", self.y);
    def render_pos(self):
        return (self.x * 10, self.y * 10)

class Window:
    # Open a window on the screen
    screen_width=400
    screen_height=400
    grid_width = 40
    grid_height = 40
    player = Player()
    pill = Pill(0, 0)

    def Run(self):
        window = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.SummonPill(window)
        prev_move = self.player.moveUp
        while True:
            prev_move = self.MovePlayerWithCapturedKey(prev_move)
            if self.IsPlayerEatsPill(self.player, self.pill):# player eat pills
                self.player.length += 1
                print(self.player.length)
                self.SummonPill(window)
                continue
            if self.IsPlayerDead(self.player):
                print("Game Over!")
                break
            tail = self.player.body.pop()
            player_image = pygame.Surface((10, 10))
            player_image.fill((0, 0, 0))
            window.blit(player_image, (tail[0] * 10, tail[1] * 10))
            self.DisplayPlayer(self.player, window)
            time.sleep(0.1)

    def IsPlayerEatsPill(self, player, pill):
        if (player.x is pill.x and player.y is pill.y):
            return True
        return False

    def IsPlayerDead(self, player):
        return self.IsSelfCollide(player) or self.IsOutOfBoundary(player)

    def IsSelfCollide(self, player):
        if ((player.x, player.y) in list(player.body)[2:]):
            print("Self Collide")
            return True
        return False

    def IsOutOfBoundary(self, player):
        if (player.x >= self.grid_width or player.y >= self.grid_height 
                or player.x < 0 or player.y < 0):
            print("Out of Boundary!")
            return True
        return False

    def SummonPill(self, window):
        self.pill = Pill(random.randrange(self.grid_width), random.randrange(self.grid_height))
        pill_image = pygame.Surface((10, 10))
        pill_image.fill((0, 255, 0))
        window.blit(pill_image, self.pill.render_pos())
        pygame.display.update()

    def DisplayPlayer(self, player, window):
        player_image = pygame.Surface((10, 10))
        player_image.fill((255, 255, 255))
        for pos in player.body:
            window.blit(player_image, (pos[0] * 10, pos[1] * 10))
        pygame.display.update()

    def MovePlayerWithCapturedKey(self, prev_move):
        pygame.event.pump()
        keys = pygame.key.get_pressed()
        if(keys[K_RIGHT]):
            self.player.moveRight()
            return self.player.moveRight
        if(keys[K_LEFT]):
            self.player.moveLeft()
            return self.player.moveLeft
        if(keys[K_UP]):
            self.player.moveUp()
            return self.player.moveUp
        if(keys[K_DOWN]):
            self.player.moveDown()
            return self.player.moveDown
        if(keys[K_ESCAPE]):
            return sys.exit()
        prev_move()
        return prev_move

if __name__ == "__main__":
    window = Window()
    window.Run()

