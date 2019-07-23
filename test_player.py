from snake import Player

def test_moveRight_playerheadxposincrease_playerheadxpositionincrementbyone():
    player = Player(5, 5)
    player.moveRight()
    assert player.head_pos[0] == 6 and player.head_pos[1] == 5

def test_moveLeft_playerheadxposdecrease_playerheadxpositiondecrementbyone():
    player = Player(5, 5)
    player.moveLeft()
    assert player.head_pos[0] == 4 and player.head_pos[1] == 5

def test_moveUp_playerheadyposdecrease_playerheadypositiondecrementbyone():
    player = Player(5, 5)
    player.moveUp()
    assert player.head_pos[0] == 5 and player.head_pos[1] == 4

def test_moveDown_playerheadyposincrease_playerheadypositionincrementbyone():
    player = Player(5, 5)
    player.moveDown()
    assert player.head_pos[0] == 5 and player.head_pos[1] == 6
