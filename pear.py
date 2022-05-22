# apple but without AI (I think) therfore its dumb
# and we all know pears are inferior :)

import random
import numpy as np
import pandas as pd
from scipy.special import softmax

rng = random.Random()
player_choices = []
POINTS = 5 # the amount of points the "ai" can spend on items
STATS = ['str', 'vit','agi']

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def createItemRandom():
    return { stat : rng.randint(0, 2) for stat in STATS } # maybe this way, just to see, but maybe use np_rand_arr()?

def createItem(np_avg_mod, points_left):
    np_avg_mod_deep = np.copy(np_avg_mod) # freakin' deep clones man
    print(f'{bcolors.WARNING}Warning: These values are random{bcolors.ENDC}')
    ai_choice = rng.randint(0, len(np_avg_mod_deep)-1)
    np_avg_mod_deep[ai_choice] = np_avg_mod_deep[ai_choice] + points_left
    print('pn_avg_mod:', np_avg_mod_deep)
    return dict(zip(STATS, np_avg_mod_deep)) # YAT # TODO do 2 arrays, one of fields and enumerate them

def getAvgChoice(): # i could one line this
    df = pd.DataFrame(player_choices).values # convert to df with just values
    df_average = pd.DataFrame(df.mean(axis=0).round(0).astype(int), STATS) # make df of the average with labels
    return df_average.to_numpy()[:,0] #df_average.to_dict()[0] # convert to dict and get the first value

def getCol𝚫(col): # should return the number, otherwise confusing and to much work
    if len(player_choices) < 2:
        print(f'{bcolors.WARNING}Warning: These values are random{bcolors.ENDC}')
        return rng.randint(-1, 1)
    new = col[-1] # last item's col number
    old = col[-2] # second to last ''
    distance = 1
    𝚫 = (new - old) / distance # just the last, right
    return 𝚫 # what if 0.2, should it be 0 or 1, 0. needs to not round, so it can add numbers

def createItems():
    # for now base on avg, maybe change that too though
    # maybe chnage softmax to something for each based on patterns it sees
    if len(player_choices) == 0: # if no choices yet
        print(f'{bcolors.WARNING}Warning: These values are random{bcolors.ENDC}')
        return [ createItemRandom(), createItemRandom(), createItemRandom() ]

    np_avg_choice = getAvgChoice()
    df_choices = pd.DataFrame(player_choices)
    np_Δ = np.array( [ getColΔ(df_choices[stat].to_list()) for stat in STATS ] ) # np i guess
    #np_𝚫 = np.array([getCol𝚫(df_choices['str'].to_list()), getCol𝚫(df_choices['vit'].to_list())])
    np_𝚫_softmax = np.floor(softmax(np_𝚫)*POINTS).astype(int) # 𝚫_soft_str = 𝚫_str / (𝚫_str+𝚫_vit)
    print('col del:', np_Δ)
    print('delta pointmax:', np_𝚫_softmax) # TODO see what they add too, [2, 6] -> [1, 1] ?
    print('pointmax: str:', (np_𝚫_softmax[0]), 'max:', np.sum(np_Δ_softmax))#(np_𝚫_softmax[0]) + (np_𝚫_softmax[1]))
    np_avg_mod = np.add(np_avg_choice, np_Δ_softmax)
    points_left = POINTS - np.sum(np_Δ_softmax) # (p-(a+b)) -> (p-a-b)
    print(points_left, '=', POINTS, '-', np.sum(np_Δ_softmax))
    return [ createItem(np_avg_mod, points_left), createItem(np_avg_mod, points_left), createItem(np_avg_mod, points_left) ]


while True:
    to_spend = POINTS
    choices = createItems()
    # choices.append('pass')
    for i, c in enumerate(choices):
        print(f'{i} : {c}')
    choice = input("choice: ")
    # if choice == '3': # good for now
    #     continue # maybe add it to list, but its essentially the same idea
    while not choice.isdigit() or 0 < int(choice) > 2: # better way ?
        choice = input("choice: ")
    player_choices.append(choices[int(choice)])
    print(f'added: {player_choices[-1]}')
    print(f'mean: {getAvgChoice()}')