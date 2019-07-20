from snake import *

game = Game()

def test_IsPlayerEatsPill_playerheadposispillpos_returntrue():
    player = Player(1,1)
    pill = Pill(1, 1)
    assert game.IsPlayerEatsPill(player, pill)

def test_IsPlayerEatsPill_playerheadposisnotpillpos_returnfalse():
    player = Player(1,1)
    pill = Pill(0, 0)
    assert not game.IsPlayerEatsPill(player, pill)

def test_IsPlayerDead_playerheadposisoneofitsbodyposes_returntrue():
    player = Player(2,1)
    player.body = [(2,1), (2,2), (3,2), (3,1), (2,1), (1,1)]
    assert game.IsPlayerDead(player)

def test_IsPlayerDead_playerheadposisnoneofitsbodyposes_returnfalse():
    player = Player(4,1)
    player.body = [(4,1), (3,1), (2,1), (1,1)]
    assert not game.IsPlayerDead(player)

def test_IsPlayerDead_playeroutofboundary_returntrue():
    player = Player(-1, game.GRID_HEIGHT)
    assert game.IsPlayerDead(player)
    player = Player(game.GRID_WIDTH, -1)
    assert game.IsPlayerDead(player)
    player = Player(game.GRID_WIDTH, game.GRID_HEIGHT+1)
    assert game.IsPlayerDead(player)
    player = Player(game.GRID_WIDTH+1, game.GRID_HEIGHT)
    assert game.IsPlayerDead(player)

def test_IsPlayerDead_playerwithinboundary_returnfalse():
    player = Player(game.GRID_WIDTH, game.GRID_HEIGHT)
    assert game.IsPlayerDead(player)
    player = Player(game.GRID_WIDTH, game.GRID_HEIGHT-1)
    assert game.IsPlayerDead(player)
    player = Player(game.GRID_WIDTH-1, game.GRID_HEIGHT)
    assert game.IsPlayerDead(player)
