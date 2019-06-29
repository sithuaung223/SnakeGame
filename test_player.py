from snake import Player

def test_playermoveright_xpositionincrementbyone():
    player = Player(5, 5)
    player.moveRight()
    assert player.x == 6 and player.y == 5

def test_playermoveleft_xpositiondecrementbyone():
    player = Player(5, 5)
    player.moveLeft()
    assert player.x == 4 and player.y == 5

def test_playermoveup_ypositiondecrementbyone():
    player = Player(5, 5)
    player.moveUp()
    assert player.x == 5 and player.y == 4

def test_playermovedown_ypositionincrementbyone():
    player = Player(5, 5)
    player.moveDown()
    assert player.x == 5 and player.y == 6
