# apple but without AI (I think) therfore its dumb
# and we all know pears are inferior :)

import random
import numpy as np
import pandas as pd
from scipy.special import softmax

rng = random.Random()
player_choices = []
POINTS = 3 # the amount of points the "ai" can spend on items

def createItem():
    if len(player_choices) == 0: # if no choices yet
        return { "str" : rng.randint(0, 9), "vit" : rng.randint(0, 9) }
    
    np_avg_choice = getAvgChoice()
    df_choices = pd.DataFrame(player_choices)
    np_𝚫 = np.array([getCol𝚫(df_choices['str'].to_list()), getCol𝚫(df_choices['vit'].to_list())]) # np i guess
    np_𝚫_softmax = np.floor(softmax(np_𝚫)*POINTS).astype(int) # 𝚫_soft_str = 𝚫_str / (𝚫_str+𝚫_vit)
    print(np_Δ)
    print(np_𝚫_softmax) # TODO see what they add too, [2, 6] -> [1, 1] ?
    print('str:', (np_𝚫_softmax[0]))
    print('max:', (np_𝚫_softmax[0]) + (np_𝚫_softmax[1]))
    np_avg_mod = np.add(np_avg_choice, np_Δ_softmax)
    points_left = POINTS - (np_𝚫_softmax[0]) + (np_𝚫_softmax[1])
    ai_choice = rng.randint(0, len(np_avg_mod)-1)
    np_avg_mod[ai_choice] = np_avg_mod[ai_choice] + points_left
    print('pn_avg_mod:', np_avg_mod)
    return { "str" : np_avg_mod[0], "vit" : np_avg_mod[1] } # TODO do 2 arrays, one of fields and enumerate them

def getAvgChoice(): # i could one line this
    df = pd.DataFrame(player_choices).values # convert to df with just values
    df_average = pd.DataFrame(df.mean(axis=0).round(0).astype(int), ["str", "vit"]) # make df of the average with labels
    return df_average.to_numpy()[:,0] #df_average.to_dict()[0] # convert to dict and get the first value

def getCol𝚫(col): # should return the number, otherwise confusing and to much work
    if len(player_choices) < 2:
        return rng.randint(-1, 1)
    new = col[-1] # last item's col number
    old = col[-2] # second to last ''
    distance = 1
    𝚫 = (new - old) / distance # just the last, right
    return 𝚫 # what if 0.2, should it be 0 or 1, 0. needs to not round, so it can add numbers

def createItems():
    to_spend = POINTS


while True:
    to_spend = POINTS
    choices = [ createItem(), createItem(), createItem() ]
    for i, c in enumerate(choices):
        print(f'{i} : {c}')
    choice = input("choice: ")
    while not choice.isdigit() or 0 < int(choice) > 2: # better way ?
        choice = input("choice: ")
    player_choices.append(choices[int(choice)])
    print(f'added: {player_choices[-1]}')
    print(f'mean: {getAvgChoice()}')