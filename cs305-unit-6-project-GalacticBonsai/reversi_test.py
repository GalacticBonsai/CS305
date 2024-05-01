from reversiGame import *

def str_to_board(s):
    board = {
            'white': set(),
            'black': set()
    } 
    r = 1
    for line in s.strip().split('\n'):
        c = 1
        for p in line.strip():
            if p == 'O':
                board['white'].add((9-r, c))
            elif p == '#':
                board['black'].add((9-r, c))
            c += 1
        r += 1
    return board
            
def test_start():
    bstr = """
        ........
        ........
        ........
        ...#O...
        ...O#...
        ........
        ........
        ........"""
    node = Reversi(True, newboard=str_to_board(bstr))
    moves = set(node.legal_moves())
    assert len(moves) == 4
    assert (6, 4) in moves
    assert (5, 3) in moves
    assert (4, 6) in moves
    assert (3, 5) in moves
    
def test_multi_capture():
    bstr = """
        #......#
        ....O..O
        ..O.#.#.
        ...###..
        O###.##O
        ........
        ........
        .#....#."""
    node = Reversi(True, newboard=str_to_board(bstr))
    assert len(node.board['white']) == 5
    assert len(node.board['black']) == 14
    node = Reversi(True, (4, 5), newboard=str_to_board(bstr))
    assert len(node.board['white']) == 16
    assert len(node.board['black']) == 4
    
def test_black_win_big():
    bstr = """
        ########
        #####O##
        #O######
        ########
        ########
        ########
        ########
        #######O"""
    node = Reversi(True, newboard=str_to_board(bstr))
    assert node.isLeaf()
    assert node.evaluate() == -1
    node = Reversi(False, newboard=str_to_board(bstr))
    assert node.isLeaf()
    assert node.evaluate() == -1
    
    
def test_white_skip_turn():
    bstr = """
        #######.
        #####.#O
        #O######
        ########
        ########
        ########
        ########
        #######O"""
    node = Reversi(False, (8,8), newboard=str_to_board(bstr))
    assert not node.isMax
    assert node.isLeaf()
    assert node.evaluate() == -1
    
if __name__ == '__main__':
    import pytest
    pytest.main()