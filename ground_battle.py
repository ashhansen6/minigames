# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 13:38:35 2021

GROUND INVASION! The Game
@author: Ashton Hansen (ashhansen6@outlook.com)
"""

# Packages used:
import numpy as np
import pandas as pd
import random as rng
from termcolor import colored

# Defining starting forces
## Defenders:
def_force = 1250
def_reserves = 400
defenders = def_force + def_reserves
def_strength = def_force
def_guard = def_force

## Attackers:
att_force = 900
att_reserves = 1000
attackers = att_force + att_reserves
att_strength = att_force
att_guard = att_force

# Defining strategies:
    
## Defenders:
def_strat = ["draft", "turtle"]

### Draft
def draft(def_force, def_reserves):
    global def_pair
    global def_strength
    global def_guard
    # Defender Strategy Information
    print(colored("########## INTELLIGENCE REPORT ##########", on_color = "on_cyan"))
    print("You hear news that a draft decree was issued...")
    print("Intelligence suggests that there will be more enemy combatants.")
    print("You expect the drafted soldiers to have decreased combat effectiveness.")
    # Defender Strategy Effects
    if def_reserves >= 100:
        def_danger = def_force + 100
        def_safe = def_reserves - 100
        print("Defender's fielded forces:", def_danger)
        print("Defender's forces still in reserve:", def_safe)
    else:
        def_danger = def_force + def_reserves
        def_safe = 0
        print("Defender's fielded forces:", def_danger)
        print("Defender's forces still in reserve:", def_safe)
    def_power = def_danger * 0.980
    def_protection = def_danger * 0.95
    def_deployment = [def_danger, def_safe, def_power, def_protection]
    return(def_deployment)

### Turtle
def turtle(def_force, def_reserves):
    global def_pair
    global def_strength
    global def_guard
    # Defender Strategy Information
    print(colored("########## INTELLIGENCE REPORT ##########", on_color = "on_cyan"))
    print("The defenders appear to bolster their defenses in preparation.")
    print("Intelligence suggests that their defenses will be difficult to penetrate.")
    print("It is likely that the defenders will try to keep soldiers out of harm's way.")
    # Defender Strategy Effects
    if def_force > 1100:
        def_danger = def_force
        def_safe = def_reserves + (def_danger - 1100)
        def_danger = 1100
        print("Defender's fielded forces:", def_danger)
        print("Defender's forces still in reserve:", def_safe)
    else:
        def_danger = def_force
        def_safe = def_reserves
        print("Defender's fielded forces:", def_danger)
        print("Defender's forces still in reserve:", def_safe)
    def_power = def_danger * 0.975
    def_protection = def_danger * 1.15
    def_deployment = [def_danger, def_safe, def_power, def_protection]
    return(def_deployment) 

## Attackers:
    
att_strat = ["blitz", "guerilla"]

### Blitz
def blitz(att_force, att_reserves):
    global att_pair
    global att_strength
    global att_guard
    # Attacker Strategy Information
    print(colored("########## OFFICERS' REPORTS  #########", on_color = "on_cyan"))
    print("Your officers grimly accept your orders...")
    print("There is an air of apprehension as the troops prepare to deploy.")
    print("While offensive effectiveness will improve, heavier losses are expected.")
    # Attacker Strategy Effects
    if att_reserves >= 200:
        att_danger = att_force + 200
        att_safe = att_reserves - 200
        print("Attacker's fielded forces:", att_danger)
        print("Attacker's forces still in reserve:", att_safe)
    else:
        att_danger = att_force + att_reserves
        att_safe = 0
        print("Attacker's fielded forces:", att_danger)
        print("Attacker's forces still in reserve:", att_reserves)
    att_power = att_danger * 1.10
    att_protection = att_danger * 0.90
    att_deployment = [att_danger, att_safe, att_power, att_protection]
    return(att_deployment)

### Guerilla
def guerilla(att_force, att_reserves):
    global att_pair
    global att_strength
    global att_guard
    # Attacker Strategy Information
    print(colored("########## OFFICERS' REPORTS  #########", on_color = "on_cyan"))
    print("Your officers immediately begin plans to target strategic weak points.")
    print("Soldiers move out in small forces and keep the enemy guessing.")
    print("While not as effective offensively, troop survival rates should be higher.")
    # Attacker Strategy Effects
    if att_force > 750:
        att_danger = att_force
        att_safe = att_reserves + (att_force - 750)
        att_danger = 750
    else:
        att_danger = att_force
        att_safe = att_reserves
    print("Attacker's fielded forces:", att_danger)
    print("Attacker's forces still in reserve:", att_safe)
    att_power = att_danger * 0.95
    att_protection = att_danger * 1.25
    att_deployment = [att_danger, att_safe, att_power, att_protection]
    return(att_deployment)

# Ground Battle Event (Player == Attacker)
wave = 0
player = input("Attacker or Defender? [A/D]:")
while (attackers > 0) and (defenders > 0):
    # Wave Information
    wave = wave + 1
    if wave == 1:
        print("############################################################")
        print("PREPARE FOR BATTLE! THE FIRST WAVE OF THE BATTLE BEGINS NOW.")
        print("############################################################")
    else:
        print("########## WAVE:", wave, "##########")
        print("#############################")
    print("Defending force strength:", def_force)
    print("Defending forces in reserve:", def_reserves)
    print("Attacking force strength:", att_force)
    print("Attacking forces in reserve:", att_reserves)
    if player =="A":
        # Active Player (Attacker)
        att_strat_chosen = input(colored("How should we proceed, commander? [blitz/guerilla]:", "yellow"))
    elif player == "D":
        # CPU Attacker
        att_strat_chosen = rng.choice(att_strat)
    # Defender Setup
    if player == "A":
        # CPU Defender
        if def_reserves > 0:
            def_strat = ["none", 
                         "draft", "draft", "draft", "draft", "draft", "draft", 
                         "turtle", "turtle", "turtle"]
            def_strat_chosen = rng.choice(def_strat)
        else:
            def_strat = ["none", "none",
                         "turtle", "turtle", "turtle" ,"turtle", "turtle", "turtle", "turtle", "turtle"]
            def_strat_chosen = rng.choice(def_strat)
    elif player == "D":
        # Active Player (defender)
        def_strat_chosen = input(colored("How should we proceed, commander? [draft/turtle]:", "yellow"))
    if def_strat_chosen == "draft":
        draft_results = draft(def_force, def_reserves)
        def_force = draft_results[0]
        def_reserves = draft_results[1]
        def_strength = draft_results[2]
        def_guard = draft_results[3]
    elif def_strat_chosen == "turtle":
        turtle_results = turtle(def_force, def_reserves)
        def_force = turtle_results[0]
        def_reserves = turtle_results[1]
        def_strength = turtle_results[2]
        def_guard = turtle_results[3]
    elif def_strat_chosen == "none":
        print(colored("########## INTELLIGENCE REPORT ##########", on_color = "on_cyan"))
        print("It appears that the enemy will employ standard tactics...")
        def_force = def_force
        def_reserves = def_reserves
        def_strength = def_force
        def_guard = def_force
        print("Defending force strength:", def_force)
        print("Forces kept in reserve:", def_reserves)
    # Attacker Setup
    if att_strat_chosen == "blitz":
        blitz_results = blitz(att_force, att_reserves)
        att_force = blitz_results[0]
        att_reserves = blitz_results[1]
        att_strength = blitz_results[2]
        att_guard = blitz_results[3]
    elif att_strat_chosen == "guerilla":
        guerilla_results = guerilla(att_force, att_reserves)
        att_force = guerilla_results[0]
        att_reserves = guerilla_results[1]
        att_strength = guerilla_results[2]
        att_guard = guerilla_results[3]
    # Combat
    # Attacker damage
    def_guard = np.random.normal(def_guard, def_guard/10) * 0.50
    att_strength = att_strength - def_guard
    if att_strength < 0:
        att_strength = 0
    def_force = def_force - np.random.normal(att_strength, att_strength/10)//2 - (0.1*att_strength)//1
    if def_force < 0:
        def_force = 0
    # Defender damage
    att_guard  = np.random.normal(att_guard, att_guard/10) * 0.50 - 0.1
    def_strength = def_strength - att_guard
    if def_strength < 0:
        def_strength = 0
    att_force = att_force - np.random.normal(def_strength, def_strength/10)//2 - (0.1*def_strength)//1
    if att_force < 0:
        att_force = 0
    # Post-wave results:
    print(colored("########## POST-WAVE RESULTS ##########", on_color = "on_cyan"))
    print(colored("Defenders:", on_color = "on_blue"))
    print("Surviving defensive forces:", def_force)
    print("Defenseive forces kept in reserve:", def_reserves)
    print("Defender strength estimate:", def_strength)
    print("Defender guard estimate:", def_guard)
    print(colored("Attackers:", on_color = "on_red"))
    print("Surviving attacker forces:", att_force)
    print("Attacker forces kept in reserve:", att_reserves)
    print("Attacker strength estimate:", att_strength)
    print("Attacker guard estimate:", att_guard)
    # Reset allocations
    # Defender reallocations:
    def_reserves = def_reserves + def_force
    def_force = 0
    if def_reserves >= 1250:
        def_reserves = def_reserves - 1250
        def_force = 1250
        def_guard = def_force
    else:
        def_force = def_reserves
        def_reserves = 0
        def_guard = def_force
    # Attacker reallocations:
    att_reserves = att_reserves + att_force
    att_force = 0
    if att_reserves >= 900:
        att_reserves = att_reserves - 900
        att_force = 900
        att_guard = att_force
    else:
        att_force = att_reserves
        att_reserves = 0
        att_guard = att_force
    defenders = def_force + def_reserves
    attackers = att_force + att_reserves
    # End of wave conditionals
    if (attackers > 0) and (defenders > 0) and (player == "A"):
        fightflight = input(colored("Continue or retreat?: [continue/retreat]:", "yellow"))
        if fightflight == "retreat":
            print(colored("########## WITHDRAWAL ##########", on_color = "on_blue"))
            print("You choose to withdraw your troops...")
            print(colored("######### INVASION STATISTICS ##########", on_color = "on_cyan"))
            print("Troops remaining:", attackers)
            print("Total losses:", (1900 - attackers))
            print("Survival rate:", (attackers)/1900)
            print("Total assault waves:", wave)
            break
        else:
            print("The battle will continue next turn...")
    elif attackers <= 0 and player == "A":
        print(colored("########## FAILURE! ##########", on_color = "on_red"))
        print("Your assault has been repelled!")
        print("You return home, wondering what punishment for your failure awaits...")
        print(colored("######### INVASION STATISTICS ##########", on_color = "on_cyan"))
        print("Troops remaining:", attackers)
        print("Total losses:", (1900 - attackers))
        print("Survival rate:", (attackers)/1900)
        print("Total assault waves:", wave)
    elif defenders <= 0 and player == "A":
        print(colored("########## SUCCESS! ##########", on_color = "on_green"))
        print("The defenders have been routed!")
        print("You may now decide the fate of the defending population...")
        print(colored("######### INVASION STATISTICS ##########", on_color = "on_cyan"))
        print("Troops remaining:", attackers)
        print("Total losses:", (1900 - attackers))
        print("Survival rate:", (attackers)/1900)
        print("Total assault waves:", wave)
    elif (attackers > 0) and (defenders > 0) and (player == "D"):
        fightflight = input(colored("Defend or retreat?: [defend/retreat]:", "yellow"))
        if fightflight == "retreat":
            print(colored("########## WITHDRAWAL ##########", on_color = "on_blue"))
            print("You choose to withdraw your troops from the region...")
            print(colored("######### INVASION STATISTICS ##########", on_color = "on_cyan"))
            print("Troops remaining:", defenders)
            print("Total losses:", (1900 - defenders))
            print("Survival rate:", (defenders)/1900)
            print("Total assault waves:", wave)
            break
        else:
            print("The battle will continue next turn...")
    elif defenders <= 0 and player == "D":
        print(colored("########## FAILURE! ##########", on_color = "on_red"))
        print("Your defense has been broken!")
        print("Enemy troops now occupy your lands and have claimed dominion...")
        print(colored("######### INVASION STATISTICS ##########", on_color = "on_cyan"))
        print("Troops remaining:", defenders)
        print("Total losses:", (1650 - defenders))
        print("Survival rate:", (defenders)/1650)
        print("Total assault waves:", wave)
    elif attackers <= 0 and player == "D":
        print(colored("########## SUCCESS! ##########", on_color = "on_green"))
        print("The attackers have been repelled!")
        print("The storm has passed, and your people live another day...")
        print(colored("######### INVASION STATISTICS ##########", on_color = "on_cyan"))
        print("Troops remaining:", defenders)
        print("Total losses:", (1650 - defenders))
        print("Survival rate:", (defenders)/1650)
        print("Total assault waves:", wave)
    print("#############################")
    
    
    
    
    
    

