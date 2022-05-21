import random

rng = random.Random()
player_choices = []

def item():
    return { "str" : rng.randint(0, 9), "vit" : rng.randint(0, 9) }

while True:
    choices = [ item(), item(), item() ]
    for i, c in enumerate(choices):
        print(f'{i} : {c}')
    choice = input("choice: ")
    while not choice.isdigit() or 0 < int(choice) > 2: # better way ?
        choice = input("choice: ")
    player_choices.append(choices[int(choice)])
    print(f'added: {player_choices[-1]}')