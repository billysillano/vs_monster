import subprocess as sp
import random
import time

game_running = True
has_game_winner = False
current_round = 0

player = {
    'name': 'Player',
    'health': 100,
    'damage_min': 10,
    'damage_max': 50
}

monster = {
    'name': 'Monster',
    'health': 100,
    'damage_min': 10,
    'damage_max': 40
}

# print current health
def print_health (player_obj):
    print(player_obj['name'] + '\'s health: ' )
    print((u"\u25A0" * player_obj['health'])  + ' ' + str(player_obj['health']))

# attack
def attack (damage_dealer, damage_reciever):
    print(damage_dealer['name'] + ' attacked ' + damage_reciever['name'])

    dodge = False
    
    if damage_reciever['health'] < 60:
        dodge = random.randint(0,9) <= 2
    
    if not dodge:
        damage = random.randint(damage_dealer['damage_min'], damage_dealer['damage_max'])
        damage_reciever['health'] = max(0, damage_reciever['health'] - damage)
        print_health(damage_reciever)
    else:
        print(damage_reciever['name'] + ' dodged the attack!')

    if damage_reciever['health'] <= 0:
        global has_game_winner
        has_game_winner = True


# heal
def heal (player_obj):
    print(player_obj['name'] + ' heals.')
    player_obj['health'] = min(100, player_obj['health'] + random.randint(10, 50))
    print_health(player_obj)
    time.sleep(2)

def print_game_winner (name):
    print_divider()
    print(name + ' win the game.')
    print_divider()
    global game_running
    game_running = False


#print divider 
def print_divider ():
    print('=' * 100)
    print('\n')

# run the game
print_divider()
print('Welcome to my stupid game.')
player['name'] = input('Enter your name: ')
print_divider()

while game_running: 
    current_round += 1
    
    tmp = sp.call('cls',shell=True)

    print('Round: ' + str(current_round))
    print_health(monster)
    print_health(player)
    print_divider()    
    print('1 : Attack , 2 : Heal')
    action = input('What do you want to do? _')

    print_divider()

    if action == '1':
        attack(player, monster)
    elif action == '2':
        heal(player)
    else: 
        print('invalid input')
    
    
    time.sleep(2)
    if has_game_winner:
        print_game_winner(player['name'])
    else:
        monster_action = 0

        if(monster['health'] < 70):
            monster_action = random.randint(0, 9)
        
        if (monster_action <= 4):
            heal(monster)
        else: 
            attack(monster, player)

        if has_game_winner:    
            print_game_winner(monster['name'])

    time.sleep(2)
    if not has_game_winner:
        print('\n')
        print('End of round ' + str(current_round))
        print('please wait...')
        time.sleep(4)


print('Game over')
print_divider()



    
    
    
