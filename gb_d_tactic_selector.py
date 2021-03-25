# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:55:50 2021

@author: ashha
"""
# Packages used:
import numpy as np

def def_strat(trials):
    transition_names = [["AtoA", "AtoB", "AtoC"],
                        ["BtoA", "BtoB", "BtoC"],
                        ["CtoA", "CtoB", "CtoC"]]
    
    transition_matrix = [[0.900, 0.075, 0.025],
                         [0.150, 0.800, 0.050],
                         [0.250, 0.250, 0.500]]
    
    start_state = "A"
    initial_matrix = [[1],
                      [0],
                      [0]]
    
    prob = 1
    i = 0
    action_current = "A"
    action_list = ["A"]
    
    while i < trials:
        if action_current == "A":
            state_change = np.random.choice(transition_names[0], 
                                            replace = True, 
                                            p = transition_matrix[0])
            if state_change == "AtoA":
                prob *= transition_matrix[0][0]
                action_list.append("A")
                pass
            elif state_change == "AtoB":
                prob *= transition_matrix[0][1]
                action_current == "B"
                action_list.append("B")
            else:
                prob *= transition_matrix[0][2]
                action_current = "C"
                action_list.append("C")
        elif action_current == "B":
            state_change = np.random.choice(transition_names[1], 
                                            replace = True, 
                                            p = transition_matrix[1])
            if state_change == "BtoB":
                prob *= transition_matrix[1][1]
                action_list.append("B")
                pass
            elif state_change == "BtoA":
                prob *= transition_matrix[1][0]
                action_current == "A"
                action_list.append("A")
            else:
                prob *= transition_matrix[1][2]
                action_current = "C"
                action_list.append("C")
        elif action_current == "C":
            state_change = np.random.choice(transition_names[2], 
                                            replace = True, 
                                            p = transition_matrix[2])
            if state_change == "CtoC":
                prob *= transition_matrix[2][2]
                action_list.append("C")
                pass
            elif state_change == "CtoA":
                prob *= transition_matrix[2][0]
                action_current == "A"
                action_list.append("A")
            else:
                prob *= transition_matrix[2][1]
                action_current = "B"
                action_list.append("B")
        i += 1
    print("Possible states: " + str(action_list))
    print("End state after "+ str(trials) + " days: " + str(action_current))
    print("Probability of the possible sequence of states: " + str(prob))