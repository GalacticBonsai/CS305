from ast import literal_eval
import time

##
## BEGIN modified code from masMiniMax.py in AIPython 0.9.4
## Function is modified to return the node datastructure, enfore depth limits, and avoid printing
##
# Artificial Intelligence: Foundations of Computational Agents http://artint.info
# Copyright David L Poole and Alan K Mackworth 2017-2022.
# This work is licensed under a Creative Commons
# Attribution-NonCommercial-ShareAlike 4.0 International License.
# See: http://creativecommons.org/licenses/by-nc-sa/4.0/deed.en

def minimax_alpha_beta(node,alpha=-float('inf'),beta=float('inf'),depth=0,max_depth=5):
    """node is a Node, alpha and beta are cutoffs, depth is the depth
    returns value, node
    where node is the resulting best choice for the player of the given node
    """
    best=None      # only used if it will be pruned
    if node.isLeaf() or depth > max_depth:
        return node.evaluate(),None
    elif node.isMax:
        for C in node.children():
            score,path = minimax_alpha_beta(C,alpha,beta,depth+1,max_depth)
            if score >= beta:    # beta pruning
                return score, None 
            if score > alpha:
                alpha = score
                best = C
        return alpha,best
    else:
        for C in node.children():
            score,path = minimax_alpha_beta(C,alpha,beta,depth+1,max_depth)
            if score <= alpha:     # alpha pruning
                return score, None
            if score < beta:
                beta=score
                best = C
        return beta,best

##
## END modified code from masMiniMax.py in AIPython 0.9.4
##


class IllegalMove(Exception):
    def __init__(self, msg):
        pass

class GameClient:
    def __init__(self, game, p1ai = False, p2ai = False, aidepth=5):
        self.game = game
        self.p1ai = p1ai
        self.p2ai = p2ai
        self.aidepth = aidepth
    
    def player_turn(self, node):
        while True:
            move_str = input('Enter move for Player ' + ('1' if node.isMax else '2') + ': ')
            try:
                move = literal_eval(move_str)
                return self.game(node.isMax, move, node.prior_moves, node.board)
            except IllegalMove as e:
                print('Illegal move, try again.', e)     

    def ai_turn(self, node, ai):
        start_time = time.perf_counter()
        node = ai(node.isMax, None, node.prior_moves, node.board)
        v, n = minimax_alpha_beta(node, max_depth=self.aidepth)
        end_time = time.perf_counter()
        print("Time:", end_time - start_time, "seconds")
        return n
            
    def run_game(self):
        main_node = self.game()
        
        while not main_node.isLeaf():
            print('Current Board: ')
            main_node.print_board()
            next_node = None
            
            if main_node.isMax:
                print("Player 1's Turn")
                if self.p1ai:
                    next_node = self.ai_turn(main_node, self.p1ai)
                else:
                    next_node = self.player_turn(main_node)
            else:
                print("Player 2's Turn")
                if self.p2ai:
                    next_node = self.ai_turn(main_node, self.p2ai)
                else:
                    next_node = self.player_turn(main_node)
            
            print('Move is: ' + str(next_node.move))
            main_node = next_node
        
        if main_node.evaluate() > 0:
            print('Player 1 wins')
        else:
            print('Player 2 wins')
        
        
    