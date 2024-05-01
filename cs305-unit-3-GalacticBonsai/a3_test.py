from a3 import path_to_actions, gen_tiles, gen_puzzle_feature_dict, str_to_8puzzle_state, gen_spaces, gen_puzzle_actions, gen_puzzle_domain, puzzle_heuristic 
import time
import math
import types
from stripsProblem import Strips, STRIPS_domain, Planning_problem
from stripsForwardPlanner import Forward_STRIPS, SearcherMPP
from operator import lt,ne,eq,gt

# Unit tests for CS305 Unit 3 homework assignment 
    
def test_1():
    """test gen_spaces in 8-puzzle"""
    spaces = set(gen_spaces(3))
    assert len(spaces) == 9, "wrong number of spaces generated for 8-puzzle"
    assert 'space1-1' in spaces
    assert 'space1-2' in spaces
    assert 'space1-3' in spaces
    assert 'space2-1' in spaces
    assert 'space2-2' in spaces
    assert 'space2-3' in spaces
    assert 'space3-1' in spaces
    assert 'space3-2' in spaces
    assert 'space3-3' in spaces
    
def test_2():
    """test gen-spaces in additional dimensions"""
    spaces = set(gen_spaces(2))
    assert len(spaces) == 4
    assert 'space2-1' in spaces
    
    spaces = set(gen_spaces(4))
    assert len(spaces) == 16
    assert 'space2-1' in spaces
    assert 'space3-4' in spaces
    

def test_3():
    """test 8puzzle results of generating actions"""
    actions = set(gen_puzzle_actions(3))
    assert len(actions) == 4*3*2*(3*3-1)
    
    for action in actions:
        if str(action) == 'move-5-down':
            if action.preconds == {'tile5': 'space1-1', 'blank': 'space2-1'} and \
               action.effects == {'tile5': 'space2-1', 'blank': 'space1-1'}:
                found = True
                
    assert found, "did not find move-5-down for space1-1"
    
    for action in actions:
        if str(action) == 'move-8-left':
            if action.preconds == {'tile8': 'space2-3', 'blank': 'space2-3'} and \
               action.effects == {'tile8': 'space2-2', 'blank': 'space2-3'}:
                found = True
                
    assert found, "did not find move-8-left for space2-3"
    
 
def test_4():
    """test 16puzzle results of generating actions"""
    actions = set(gen_puzzle_actions(4))
    assert len(actions) == 4*4*3*(4*4-1)
    
    for action in actions:
        if str(action) == 'move-5-down':
            if action.preconds == {'tile5': 'space1-1', 'blank': 'space2-1'} and \
               action.effects == {'tile5': 'space2-1', 'blank': 'space1-1'}:
                found = True
                
    assert found, "did not find move-5-down for space1-1"
    
    for action in actions:
        if str(action) == 'move-12-left':
            if action.preconds == {'tile12': 'space4-3', 'blank': 'space4-3'} and \
               action.effects == {'tile12': 'space4-2', 'blank': 'space4-3'}:
                found = True
                
    assert found, "did not find move-12-left for space4-3"
    
    
def test_5():
    """test gen_puzzle_domain along with rest of system for 8puzzle"""
    
    p1start = """123
                 456
                 7X8"""
    p2start = """X23
                 156
                 478"""
    pend = """123
              456
              78X"""
    
    prob = Planning_problem(gen_puzzle_domain(3),
                        str_to_8puzzle_state(p1start),
                        str_to_8puzzle_state(pend))
    fsprob = Forward_STRIPS(prob)
    searcher = SearcherMPP(fsprob)
    res = searcher.search()
    res = list(path_to_actions(res))
    assert len(res) == 1, "only one move should be in the solution here"
    assert str(res[0]) == 'move-8-left', "moving 8 left solves the puzzle"
    
    prob = Planning_problem(gen_puzzle_domain(3),
                        str_to_8puzzle_state(p2start),
                        str_to_8puzzle_state(pend))
    fsprob = Forward_STRIPS(prob)
    searcher = SearcherMPP(fsprob)
    res = searcher.search()
    res = list(path_to_actions(res))
    assert len(res) == 4, "only one move should be in the solution here"
    assert str(res[3]) == 'move-1-up'
    assert str(res[2]) == 'move-4-up'
    assert str(res[1]) == 'move-7-left'
    assert str(res[0]) == 'move-8-left'

def test_6():
    """test heuristic"""
    p1state = str_to_8puzzle_state("""123
                                      456
                                      7X8""")
    p2state = str_to_8puzzle_state("""X23
                                      156
                                      478""")
    goal = str_to_8puzzle_state("""123
                                   456
                                   78X""")
    # test to ensure the heuristic is admissable (at least)
    assert puzzle_heuristic(goal, goal) == 0
    assert puzzle_heuristic(p1state, goal) >= puzzle_heuristic(goal, goal)
    assert puzzle_heuristic(p2state, goal) >= puzzle_heuristic(goal, goal)
    assert puzzle_heuristic(p2state, goal) >= puzzle_heuristic(p1state, goal)

if __name__ == '__main__':
    import pytest
    pytest.main()