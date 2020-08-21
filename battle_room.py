import time
import sys
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def slow_print(string):
    for n in range(len(string)):
        sys.stdout.write(string[n])
        sys.stdout.flush()
        time.sleep((len(string) - n) / 100)
    print("")
    time.sleep(1)


def valid_input(prompt, answers):
    negations = ["That didn't seem to work",
                 "That didn't quite do the trick",
                 "That attempt failed",
                 "How about you try something else",
                 "That may not be the wisest move",
                 "Give it a thought and try again",
                 "Let's consider an alternative",
                 "Sorry, try to be more clear",
                 "Apologies, but I can't accept that answer"]
    friends = ["friend", "pal", "mate", "buddy", "comrade", "ally", "champion",
               "trainee", "amigo", "amiga", "mon ami", "mon amie"]
    while True:
        response = input(prompt + "\n").lower()
        if response == '':
            print_pause(random.choice(negations) + ', ' +
                        random.choice(friends) + '.')
        else:
            for n in range(len(answers)):
                if answers[n] in response or response in answers[n]:
                    return answers[n]
            print_pause(random.choice(negations) + ', ' +
                        random.choice(friends) + '.')


def randomized_weapons():
    possible_weapons = ['sword', 'dagger', 'potion', 'staff', 'bow', 'harp']
    weapon_choices = ['', '', '']
    for n in range(3):
        weapon_choices[n] = random.choice(possible_weapons)
        possible_weapons.remove(weapon_choices[n])
    return weapon_choices


def randomized_enemy():
    enemies = ['unicorn', 'troll', 'centaur', 'dragon', 'fairy', 'phoenix']
    your_enemy = []
    your_enemy.append(random.choice(enemies))
    return your_enemy


def full_descriptions(simple_names):
    detailed_descriptions = []

    def add_description(item, description):
        if simple_names[n] == item:
            detailed_descriptions.append(description)
    for n in range(len(simple_names)):
        add_description('sword', 'broad, shining sword with a royal blue hilt')
        add_description('dagger', 'short dagger made of black obsidian')
        add_description('potion', 'softly glowing green potion')
        add_description('staff', 'long staff topped with an orb '
                        'of changing colors')
        add_description('bow', 'wooden bow engraved with runes')
        add_description('harp', 'golden harp embellished with swans')
        add_description('unicorn', 'glaringly white and majestic unicorn')
        add_description('troll', 'monstrously tall and powerful troll')
        add_description('centaur', 'gloriously proud and noble centaur')
        add_description('dragon', 'long, lithe dragon with black scales')
        add_description('fairy', 'malevolent fairy wreathed in a glowing aura')
        add_description('phoenix', 'dazzling red phoenix in flight')
    return detailed_descriptions


def weapon_prompt(weapon):
    if weapon == 'sword':
        prompt = "Which way do you slash your sword?"
    if weapon == 'bow':
        prompt = "Which way do you aim your bow?"
    if weapon == 'staff':
        prompt = 'Which spell do you cast?'
    if weapon == 'harp':
        prompt = "Which note do you play?"
    if weapon == 'dagger':
        prompt = "Where do you strike?"
    return prompt


def weapon_moves(weapon):
    if weapon == 'sword' or weapon == 'bow' or weapon == 'dagger':
        moves = ['upwards', 'downwards', 'to the left', 'to the right']
    if weapon == 'staff':
        moves = ['fire', 'wind', 'water', 'lightning']
    if weapon == 'harp':
        moves = ['A', 'C', 'E', 'G']
    return moves


def print_move_list(weapon):
    possible_moves = weapon_moves(weapon)
    print_pause("1. " + possible_moves[0] + "\n" +
                "2. " + possible_moves[1] + "\n" +
                "3. " + possible_moves[2] + "\n" +
                "4. " + possible_moves[3] + "\n" +
                "(Type 'help' to see these moves listed again.)")


def first_room():
    slow_print("...you begin to wake up...")
    print_pause("You feel cold marble beneath you.")
    print_pause("You sit up and look around the room.")
    print_pause("You are on a stone bed in a room built of black marble.")
    print_pause("It is mostly dark, except for three items standing "
                "on pedestals.")
    weapon_choices = randomized_weapons()
    weapon_descriptions = full_descriptions(weapon_choices)
    print_pause("There is a " + weapon_descriptions[0] + ".")
    print_pause("There is a " + weapon_descriptions[1] + ".")
    print_pause("And finally, a " + weapon_descriptions[2] + ".")
    chosen_weapon = valid_input("Which item do you reach for?", weapon_choices)
    satchel = []
    for n in range(len(weapon_choices)):
        if weapon_choices[n] in chosen_weapon:
            chosen_weapon = weapon_choices[n]
            satchel.append(weapon_choices[n])
    print_pause("You reach towards the " + chosen_weapon + ".")
    print_pause("As your hand closes around it, the other two items vanish "
                "into thin air.")
    print_pause("You hear grating stone as a door begins to slide open, ")
    print_pause("and a faint light pours into the room.")
    print_pause("You step through into the next room.")
    return satchel


def second_room():
    print_pause("You feel grass and dirt beneath your feet.")
    print_pause("The walls and ceiling in this room are also made of marble, ")
    print_pause("but it is a swirling, disorienting mix of colors.")
    print_pause("In the center of the room, you see it:")
    your_enemy = randomized_enemy()
    enemy_description = full_descriptions(your_enemy)
    your_enemy = your_enemy[0]
    print_pause("A " + enemy_description[0] + '.')
    return your_enemy


def rules_of_battle(weapon):
    if weapon == 'staff':
        print_pause("You have the following spells:")
    elif weapon == 'harp':
        print_pause("You can play the following notes:")
    else:
        print_pause("You have the following attacks:")
    print_move_list(weapon)


def select_attack(attack_options, prompt, weapon):
    # this allows the player to see the move list at the beginning of the turn
    attack_options.append('help')
    attack_response = valid_input(prompt, attack_options)
    if attack_response == 'help':
        print_move_list(weapon)
        attack_response.remove('help')
        attack_response = valid_input(prompt, attack_options)
    else:
        attack_options.remove('help')
    return attack_response


def does_attack_hit(attack_result, last_attack):
    moves = [0, 1, 2, 3]
    if last_attack in moves:
        moves.remove(last_attack)
    success1 = random.choice(moves)
    moves.remove(success1)
    success2 = random.choice(moves)
    return attack_result == success1 or attack_result == success2


def successful_hit(weapon, your_enemy, attack_response):
    if weapon == 'harp':
        print_pause("Voila! Your note blended into a melody.")
    else:
        print_pause("Success! Your attack lands on the " + your_enemy
                    + ".")
    damage = 20
    super_effective = ['bowdragon', 'bowunicorn', 'swordtroll', 'daggerfairy',
                       'daggerunicorn']
    strong_spells = ['lightningphoenix', 'waterdragon', 'firetroll',
                     'windfairy', 'firecentaur', 'lightningunicorn']
    if weapon == 'harp':
        if your_enemy == 'phoenix' or your_enemy == 'troll':
            print_pause("What soothing music! The " + your_enemy +
                        " grows tired!")
            damage *= 2
    if weapon == 'staff' and attack_response + your_enemy in strong_spells:
        print_pause("That spell seems strong against the " + your_enemy + "!")
        damage *= 2
    if weapon + your_enemy in super_effective:
        print_pause("That was a serious hit!")
        damage *= 2
    return damage


def missed_hit(weapon, your_enemy):
    if weapon == 'harp':
        print_pause("Oh no, that note was discordant. The " + your_enemy
                    + " strikes you!")
    else:
        print_pause("You missed! The " + your_enemy + " strikes you.")


def who_won(PlayerHP, EnemyHP, weapon, your_enemy):
    if PlayerHP <= 0:
        return 'lose'
    if EnemyHP <= 0:
        if weapon == 'harp':
            print_pause("Bravo! Your melodic talent with the harp " +
                        "enchants the " + your_enemy + ".")
            print_pause("It grows weary and falls to the ground, asleep.")
        else:
            print_pause("The " + your_enemy + " stumbles and hits "
                        "the ground, severely wounded.")
        print_pause("You have defeated it.")
        return 'win'


def battle_system(weapon, your_enemy):
    PlayerHP = 100
    EnemyHP = 100
    last_attack = 4
    prompt = weapon_prompt(weapon)
    attack_options = weapon_moves(weapon)
    rules_of_battle(weapon)
    # I'm using last_attack as a variable to prevent the loop from picking
    # the same successful attack number twice in a row.
    while PlayerHP > 0 and EnemyHP > 0:
        attack_response = select_attack(attack_options, prompt, weapon)
        # this converts text attack_options answer to an integer
        for n in range(len(attack_options)):
            if attack_response == attack_options[n]:
                attack_result = n
        if does_attack_hit(attack_result, last_attack):
            damage = successful_hit(weapon, your_enemy, attack_response)
            EnemyHP -= damage
            last_attack = attack_result
        else:
            missed_hit(weapon, your_enemy)
            PlayerHP -= 20
    battle_result = who_won(PlayerHP, EnemyHP, weapon, your_enemy)
    return battle_result


def unicorn_dialogue():
    print_pause("The unicorn approaches, looks you up and down slowly, ")
    print_pause("And then asks:")
    answer = valid_input('"Do you think I\'m pretty?"', ['yes', 'no'])
    if answer == 'yes':
        print_pause('"Really? No you don\'t."')
        follow_up = input('"Prove it, describe how pretty I am in as ' +
                          'specific terms as possible." \n')
        if len(follow_up) >= 30:
            print_pause('"You see, it\'s like pulling teeth trying to get ' +
                        'a REAL compliment around here."')
            print_pause('"You may pass."')
            return 'win'
        else:
            print_pause('"That was not believable at all."')
    else:
        print_pause("The unicorn looks at you with disgust and anger.")
        print_pause('"Who even let you in here?!"')
    print_pause("The unicorn charges at you.")
    return 'lose'


def troll_dialogue():
    print_pause("The troll looks at you suspiciously. It asks you, ")
    answer = valid_input('"Do you think you unfairly judge people ' +
                         'based on how they look?', ['yes', 'no'])
    if answer == 'no':
        print_pause('"Well then, I suppose you are not as bad as the ')
        print_pause('others who pass through here. You may pass."')
        return 'win'
    if answer == 'yes':
        print_pause('"Well then, I suppose I\'m just as violent ' +
                    'as everyone thinks I look."')
        print_pause("The troll attacks, and you have no weapon to " +
                    "defend yourself.")
        return 'lose'


def centaur_dialogue():
    print_pause("The centaur trots over to you and paws the ground " +
                "impatiently.")
    print_pause('He says, "I am curious why you did not pick a weapon."')
    print_pause('"Did you not pick one because you are weak '
                'and cannot fight, ')
    answer = valid_input('or because you think violence is not the answer?"',
                         ['weak', 'fight', 'violence', 'answer'])
    if answer == 'weak' or answer == 'fight':
        print_pause('"Not being strong enough to fight...')
        print_pause('is a terrible reason not to try."')
        print_pause("The centaur attacks and you cannot defend yourself.")
        return 'lose'
    if answer == 'violence' or answer == 'answer':
        print_pause('"That is a wise choice in a diplomatic world."')
        print_pause('"But that is not where you find yourself."')
        print_pause('"You may pass for now, that you may learn to adapt."')
        return 'win'


def dragon_dialogue():
    print_pause("The dragon peers its slitted eyes at you.")
    answer = valid_input('"Do you think you are wise?"', ['yes', 'no'])
    if answer == 'yes':
        print_pause('"Do you think it wise to think oneself wise?"')
        print_pause('"Better yet, do you think it wise to state it ' +
                    'so freely?"')
        print_pause("The dragon licks its lips. It looks hungry.")
        return 'lose'
    if answer == 'no':
        print_pause('"Is acting humble wise? Or is it just making ' +
                    'the safe choice?"')
        print_pause('"That conundrum gives me a headache. ' +
                    'Pass and leave me be."')
        return 'win'


def fairy_dialogue():
    print_pause("The fairy flies cautiously towards you.")
    name = input('"What is your name, stranger?"\n')
    is_it_though = valid_input('"Oh, I like that name. Is ' + name +
                               ' really your name?"', ['yes', 'no'])
    if is_it_though == 'yes':
        print_pause('"Silly human. Has no one ever told you not to give ' +
                    'a fairy your name?"')
        print_pause("The fairy laughs malevolently for such a small creature,")
        print_pause("for it can now bend you to its will.")
        return 'lose'
    else:
        print_pause('"Hm. You are more clever than you look. You may pass."')
        return 'win'


def phoenix_dialogue():
    print_pause("The phoenix flies close, and lands near you, " +
                "surprisingly quietly.")
    print_pause("It looks up, inspecting you with eyes that know too much.")
    print_pause('It asks, "What do you think is more valuable...')
    answer = valid_input('a longer life, or breathtaking experiences?"',
                         ['long', 'life', 'breath', 'experience'])
    if answer == 'breath' or answer == 'experience':
        print_pause('"If that is what you value more, I can provide that."')
        print_pause("The phoenix flies above you, and magnificent flames")
        print_pause("swirl around it. It is breathtaking.")
        print_pause("And then those flames consume you.")
        return 'lose'
    if answer == 'long' or answer == 'life':
        print_pause('"I suppose that means you are asking to ' +
                    'leave here alive."')
        print_pause('"You should always ask for what you need."')
        return 'win'


def potion_magic(your_enemy):
    print_pause("The " + your_enemy + " watches you, with your potion " +
                "in hand.")
    print_pause("With no other idea in mind, you drink the potion.")
    print_pause("You feel your mind expanding, as though it is " +
                "capable of more.")
    print_pause("...as if you can now understand another form of speech?")
    if your_enemy == 'unicorn':
        result = unicorn_dialogue()
    if your_enemy == 'troll':
        result = troll_dialogue()
    if your_enemy == 'centaur':
        result = centaur_dialogue()
    if your_enemy == 'dragon':
        result = dragon_dialogue()
    if your_enemy == 'fairy':
        result = fairy_dialogue()
    if your_enemy == 'phoenix':
        result = phoenix_dialogue()
    return result


def successful_ending():
    print_pause("Victorious, you hear another door sliding open.")
    print_pause("Through it, there is a long, granite hallway.")
    print_pause("When you reach the end of the hallway,")
    print_pause("you step into a large room built of white marble.")
    print_pause("There is a long table with six wizened individuals in robes.")
    print_pause("They mutter to each other, but barely notice you.")
    print_pause("A man dressed sharply walks to you, " +
                "whispering words in a strange language.")
    print_pause("You feel yourself grow sleepy.")
    print_pause("What is happening? Who are these people? Why are you here?")
    slow_print("You lose consciousness...")


def the_whole_game():
    satchel = first_room()
    your_enemy = second_room()
    if 'potion' in satchel:
        result = potion_magic(your_enemy)
    else:
        print_pause("The " + your_enemy + " sees the " + satchel[0] +
                    " in your hand and aggressively charges towards you.")
        result = battle_system(satchel[0], your_enemy)
    if result == 'win':
        successful_ending()
    else:
        print_pause("You grow faint. It seems the " + your_enemy +
                    " has bested you this time.")
    again = valid_input("Would you like to venture forth again?",
                        ['yes', 'no'])
    if again == 'yes':
        the_whole_game()
    else:
        print_pause("Until next time...")


if __name__ == "__main__":
    the_whole_game()
