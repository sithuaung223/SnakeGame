from snake import *

game = Game()

def test_playereatspill_returntrue():
    player = Player(1,1)
    pill = Pill(1, 1)
    assert game.IsPlayerEatsPill(player, pill) == True

def test_playerdoesnoteatspill_returnfalse():
    player = Player(1,1)
    pill = Pill(0, 0)
    assert game.IsPlayerEatsPill(player, pill) == False

def test_playercollideitself_returntrue():
    player = Player(2,1)
    player.body = [(2,1), (2,2), (3,2), (3,1), (2,1), (1,1)]
    assert game.IsSelfCollide(player) == True

def test_playerdoesnotcollideitself_returnfalse():
    player = Player(4,1)
    player.body = [(4,1), (3,1), (2,1), (1,1)]
    assert game.IsSelfCollide(player) == False

def test_playeroutofboundary_returntrue():
    player = Player(game.grid_width, game.grid_height+1)
    assert game.IsOutOfBoundary(player) == True
    player = Player(game.grid_width+1, game.grid_height)
    assert game.IsOutOfBoundary(player) == True

def test_playerwithinboundary_returnfalse():
    player = Player(game.grid_width, game.grid_height)
    assert game.IsOutOfBoundary(player) == True
    player = Player(game.grid_width, game.grid_height-1)
    assert game.IsOutOfBoundary(player) == True
    player = Player(game.grid_width-1, game.grid_height)
    assert game.IsOutOfBoundary(player) == True
