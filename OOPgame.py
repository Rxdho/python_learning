# The code structure, logic, or algorithms here were built within a day of learning them. Feel free to tweak or simplify anything if you’ve got a more effective or shorter way to do it. Everything here comes from my own learning process.


import random
import time
import sys

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLACK = "\033[30m"
BLUE = "\033[34m"
BRIGHT_YELLOW = "\033[93m"
MAHO = "\033[38;5;124m"
SUKU = "\033[38;5;90m"
GOJO = "\033[94m"
RESET = "\033[0m"

def type_input(prompt, delay=0.03):
    for char in prompt:
        print(char, end='', flush=True)
        time.sleep(delay)
    return input()

def loading_animation(lines, delay=0.5):
    for char in lines:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def loading_down(lines, delay=0.5):
    for char in lines:
        print(char, flush=True)
        time.sleep(delay)
    print()

def type_text(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def dual_text(text1, text2, delay=0.03):
    combined = f"{text1}  \033[3m{text2}\033[0m"
    for char in combined:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# SUKUNA DIALOG
sukuna_dialog_high = [
    ("くだらん、潰れろ。", "Pathetic, get crushed."),
    ("脆いな。次で終わりだ。", "Fragile. You're done next time."),
    ("面白い、もっと苦しめ。", "Interesting... Suffer more."),
    ("無様だな。", "How pitiful."),
    ("壊してやるよ、全部な。", "I'll destroy everything."),
]

sukuna_dialog_low = [
    ("そんなものか？", "Is that all?"),
    ("遊んでいるのか？", "Are you playing around?"),
    ("失望させるな。", "Don't disappoint me."),
    ("まだ生きてるのか。", "Still alive, huh?"),
    ("痛くも痒くもない。", "Doesn't even tickle."),
]

sukuna_dialog_defense = [
    ("回復か、無駄だ。", "Healing? Pointless."),
    ("時間稼ぎか？見苦しいな。", "Stalling? How pathetic."),
    ("癒しても無意味だ。", "Healing is useless."),
    ("再生したところで変わらん。", "Regenerating won't change your fate."),
    ("ほう…まだ足掻くか。", "Hmph... still struggling?"),
]

sukuna_dialog_victory = [
    ("終わりだ。塵に帰れ。", "It's over. Return to dust."),
    ("これが呪いの王だ。", "This is the King of Curses."),
    ("雑魚が吠えるな。", "Don't bark, you insect."),
    ("まだやる気か？死にたいのか？", "Still want to fight? Want to die?"),
    ("つまらん。次を呼べ。", "Boring. Call the next one."),
]

sukuna_dialog_defeat = [
    ("馬鹿な…この俺が…", "Impossible... I lost..."),
    ("ふん、面白い…", "Hmph... interesting..."),
    ("まだ…終わって…ない…", "Not... over yet..."),
    ("この俺が負けるだと…？", "Me, lose?"),
    ("貴様…覚えておけ…", "You... I'll remember this..."),
]

# GOJO SATORU DIALOG
gojo_dialog_high = [
    ("ほら、これが無下限呪術だよ。", "Look, this is the Limitless technique."),
    ("間に合わなかったね。", "Too late to dodge, huh?"),
    ("もっと楽しませてよ。", "Come on, entertain me more."),
    ("強いでしょ？", "Pretty strong, right?"),
    ("痛かった？ならごめんね。", "Did that hurt? Sorry~"),
]

gojo_dialog_low = [
    ("あれ？それだけ？", "Huh? That's it?"),
    ("今の本気？", "Was that for real?"),
    ("もっと頑張ってよ。", "Try harder, come on."),
    ("全然効かないな。", "That didn't do anything."),
    ("うーん、イマイチ。", "Hmm, kinda lame."),
]

gojo_dialog_defense = [
    ("ちょっと一息ね。", "Taking a quick break~"),
    ("僕を倒すには早すぎるよ。", "Too soon to beat me."),
    ("回復っと。", "Time to heal~"),
    ("まだ終われないからね。", "Can't end this yet."),
    ("無限は止まらないよ。", "The Limitless won't stop."),
]

gojo_dialog_victory = [
    ("やっぱ僕って最強だからね！", "I'm the strongest, after all!"),
    ("どう？楽しかった？", "So, was it fun?"),
    ("また戦いたい？無理だよ。", "Wanna fight again? No chance."),
    ("勝っちゃった〜", "I won again~"),
    ("無下限呪術、最高でしょ？", "Limitless technique, pretty cool, right?"),
]

gojo_dialog_defeat = [
    ("まさか…僕が…", "No way... I lost..."),
    ("冗談でしょ…？", "You're kidding, right?"),
    ("うーん…これは予想外だね。", "Hmm... didn't see that coming."),
    ("強いじゃん、認めるよ。", "You're strong, I'll give you that."),
    ("またやろう。今度は負けない。", "Let's do this again. I won't lose next time."),
]

# MAHORAGA DIALOG
mahoraga_dialog_high = [
    ("グルルル…ドンッ！", "Grrr… *Boom!*"),
    ("ガアアアッ！！", "*GRAAAHH!!*"),
    ("……（唸り声）", "……(heavy growl)"),
    ("ギィィ…ドシュッ", "*Kreeekk…* *Braak!*"),
    ("……ガガガガッ！", "*GRRRRRHHH!!*"),
]

mahoraga_dialog_low = [
    ("……（微動だにせず）", "……(doesn't move an inch)"),
    ("グゥゥ…", "*Grrr…*"),
    ("……カンッ（跳ね返す音）", "*Tang!* (sound of deflecting)"),
    ("フシュウゥ…", "*Fsshh…*"),
    ("……（首を傾ける）", "……(tilts head in confusion)"),
]

mahoraga_dialog_defense = [
    ("……（身体が再生していく）", "……(body starts regenerating)"),
    ("ギギギ…（体が回復）", "*Grrhh…* (body heals)"),
    ("……（青白い光が走る）", "……(blue light flashes on body)"),
    ("フウゥゥ…", "*Fuuuuu…*"),
    ("……（環が回る音）", "……(sound of spinning wheel)"),
]

mahoraga_dialog_victory = [
    ("……（勝利の咆哮）", "……(victory roar)"),
    ("ギィィ…ガアアッ！", "*Kreeek… GRAHH!*"),
    ("……（敵の残骸を見下ろす）", "……(stares down at enemy's remains)"),
    ("……（無音で立ち尽くす）", "……(stands silently)"),
    ("……（環が静かに止まる）", "……(wheel slowly stops spinning)"),
]

mahoraga_dialog_defeat = [
    ("……（崩れ落ちる）", "……(collapses slowly)"),
    ("ギィ…ギギ…", "*Gii… gigi…*"),
    ("……（環が止まる音）", "……(sound of wheel stopping)"),
    ("……（膝をつく）", "……(falls to knees)"),
    ("……（沈黙）", "……(silent...)"),
]

# PLAYER_ENEMY_SYSTEM

class Player:
    def __init__(self, name, health=100, max_health=100):
        self.name = name
        self.health = health
        self.maxhealth = max_health

    def attack(self, target):
        damage = [12, 18, 25, 35, 50, 28, 40, 60, 22, 32]
        damage_choiced = random.choice(damage)  
        target.health -= damage_choiced
        if target.health < 0:
            target.health = 0

        print(f"[{BLUE}{self.name}{RESET} attacks {RED}{target.name}{RESET}!]")    
        time.sleep(1)
        print(f"Damage: {RED}{damage_choiced}{RESET}")
        time.sleep(1)
        print(f"{target.name} Health Points: {GREEN}{target.health}{RESET}/{GREEN}{target.maxhealth}{RESET}")
        print()

        return damage_choiced

    def defense(self):
        regen = [5, 8, 10, 15, 30, 12, 6, 9, 13, 20]
        regen_choiced = random.choice(regen)
        self.health += regen_choiced
        if self.health > self.maxhealth:
            self.health = self.maxhealth

        print(f"[{BLUE}{self.name}{RESET} performs {GREEN}DEFENSE{RESET}]")
        time.sleep(1)
        print(f"Health Points restored: {GREEN}{regen_choiced} +HP{RESET}")
        time.sleep(1)
        print(f"Total Health Points now: {GREEN}{self.health}{RESET}/{GREEN}{self.maxhealth}{RESET}")
        print()

class SignPlayer(Player):
    def __init__(self, name, health, max_health):
        super().__init__(name, health, max_health)
        
class Enemy:
    def __init__(self, name, health=100, max_health=100):
        self.name = name
        self.health = health
        self.maxhealth = max_health

    def attack(self, target):
        damage = [10, 15, 20, 30, 50, 12, 14, 18, 22, 27]
        damage_choiced = random.choice(damage)  
        target.health -= damage_choiced
        if target.health < 0:
            target.health = 0
        
        print(f"[{self.name} attacks {BLUE}{target.name}{RESET}!]")    
        time.sleep(1)
        print(f"Damage: {RED}{damage_choiced}{RESET}")
        time.sleep(1)
        print(f"{BLUE}{target.name}{RESET} Health Points: {GREEN}{target.health}{RESET}/{GREEN}{target.maxhealth}{RESET}")
        print()

    def defense(self):
        regen = [5, 8, 10, 11, 15, 18, 22, 25, 20, 16]
        regen_choiced = random.choice(regen)
        self.health += regen_choiced
        if self.health > self.maxhealth:
            self.health = self.maxhealth
        
        print(f"[{self.name} performs {GREEN}DEFENSE{RESET}]")
        time.sleep(1)
        print(f"Health Points restored: {GREEN}{regen_choiced} +HP{RESET}")
        time.sleep(1)
        print(f"Total Health Points now: {GREEN}{self.health}{RESET}/{GREEN}{self.maxhealth}{RESET}")
        print()

# PLAYER_ENEMY_PLAYED

type_text("Welcome to Crimson Valor! Please register!")
player = type_input("Username: ")
player = BRIGHT_YELLOW + player.title() + RESET
time.sleep(2)

return_to_menu = True

if return_to_menu:
    while True:
        print(f"{player}, ready to take on a new challenge!")
        time.sleep(2)

        loading_animation(['=>  ', '=>  ', '=>  ', '=>  ', '=>  '])
        opponents = {
            GOJO + "1": "Gojo Satoru" + RESET,
            SUKU + "2": "Ryomen Sukuna" + RESET,
            MAHO + "3": "Mahoraga" + RESET,
            BLACK + "4": "Leave" + RESET
        }

        for number, name in opponents.items():
            type_text(f"{number}. {name}")

        opponent_choice = type_input(f"{player}: ").lower()

        if opponent_choice in ['leave', '4']:
            time.sleep(1)
            print("See you again in Crimson Valor!")
            time.sleep(2)
            break

        # ------------------------ GOJO BATTLE ------------------------
        if opponent_choice in ["gojo", "satoru", "1"]:
            battle_gojo = True
            while battle_gojo:
                battle_gojo = False
                enemy_name = GOJO + "Gojo" + RESET
                player1 = SignPlayer(player, health=100, max_health=100)
                enemy = Enemy(enemy_name, health=210, max_health=300)

                loading_animation(['=>  ', '=>  ', '=>  ', '=>  ', '=>  '])
                print(" ")
                type_text(f"'Suddenly, {enemy_name} stands before {player}. A smirk appears.'", delay=0.1)
                time.sleep(1)
                loading_animation(['.', '.', '.'])
                dual_text("やれやれ、面倒だなあ", "Tch, what a hassle", delay=0.1)
                time.sleep(2)
                dual_text("でも手加減しないよ", "But I won't hold back", delay=0.1)
                print(" ")
                loading_animation(['=>  ', '=>  ', '=>  '], delay=0.5)
                print(" ")

                type_text("Information: ")
                time.sleep(1)
                game_info = {
                    "Player": player,
                    "Health": GREEN + str(player1.health) + " HP" + RESET,
                    "Skill": "Attack and Defense"
                }
                for key, value in game_info.items():
                    type_text(f"{key}: {value}")
                print(" ")
                loading_animation(['=>  ', '=>  ', '=>  '])
                print(" ")

                type_text(f"Crimson Valor: Who doesn't know {enemy_name}? Behind that blindfold, never underestimate him, {player}. He can heal up to {GREEN}300 HP{RESET}", delay=0.01)
                type_text(f"Use defense to heal yourself, and attack when you get the chance!", delay=0.01)
                type_text("Victory is in your hands, stay focused!", delay=0.01)
                print(" ")
                loading_animation(['=>  ', '=>  ', '=>  '], delay=1)

                while True:
                    if player1.health == 0:
                        gojo_wins = random.choice(gojo_dialog_victory)
                        dual_text(*gojo_wins, delay=0.07)
                        print(' ')
                        print(' ')
                        time.sleep(2)
                        loading_down(['↓', '↓', '↓'], delay=1.5)
                        type_text(f"Crimson Valor: We... honor your struggle, {player}")
                        print(" ")
                        loading_animation(['=>  ', '=>  ', '=>  '])
                        type_text("Crimson Valor: Retrying won't erase your spirit!")

                        options_after_loss = {
                            "1": "Try again",
                            "2": "Main Menu",
                            "3": "Leave"
                        }

                        for number, option in options_after_loss.items():
                            type_text(f"{number}. {option}")

                        player_choice = type_input(f"{player}: ").lower()

                        if player_choice in ["1", "try again", "one"]:
                            type_text(f"Good luck fighting again, {player}!")
                            battle_gojo = True
                            break

                        elif player_choice in ["2", "main menu", "two"]:
                            return_to_menu = True
                            loading_animation(['=>  ', '=>  ', '=>  '])
                            print(" ")
                            break  

                        elif player_choice in ["3", "leave", "three"]:
                            type_text(f"Goodbye {player}, see you again!")
                            loading_animation(['=>  ', '=>  ', '=>  '], delay=1)
                            exit()
                        else:
                            type_text("Invalid choice. Returning to main menu.")
                            break

                    type_text(f"{enemy_name}: {GREEN}{enemy.health} HP{RESET}")
                    type_text(f"{player}: {GREEN}{player1.health} HP{RESET}")

                    player_options = {
                        "1": "Attack",
                        "2": "Defense"
                    }

                    for number, option in player_options.items():
                        type_text(f"{number}. {option}")

                    decision = type_input(f"{player}: ")

                    loading_animation(['=>  ', '=>  ', '=>  '])
                    print(' ')

                    if decision == "1":
                        damage = player1.attack(enemy)
                        time.sleep(2)
                    elif decision == "2":
                        player1.defense()

                    loading_animation(['=>  ', '=>  ', '=>  '])
                    print(" ")

                    if enemy.health == 0:
                        gojo_loses = random.choice(gojo_dialog_defeat)
                        dual_text(*gojo_loses, delay=0.07)
                        print(' ')
                        print(' ')
                        time.sleep(2)
                        type_text(f"Crimson Valor: Congratulations {player}! You defeated {enemy_name}!")
                        time.sleep(2)
                        type_text("Reward has been sent!")
                        loading_animation(['=>  ', '=>  ', '=>  '])

                        options_after_win = {
                            "1": "Main Menu",
                            "2": f"Fight {enemy_name} again!",
                            "3": "Leave with victory"
                        }

                        for number, option in options_after_win.items():
                            type_text(f"{number}. {option}")

                        player_choice = type_input(f"{player}: ").lower()

                        if player_choice in ["1", "main menu", "one"]:
                            return_to_menu = True
                            loading_animation(['=>  ', '=>  ', '=>  '])
                            print(" ")
                            break

                        if player_choice in ["2", "fight gojo", "two"]:
                            type_text(f"Good luck fighting again, {player}!")
                            battle_gojo = True
                            break

                        elif player_choice in ["3", "leave", "three", "leave with victory"]:
                            type_text(f"Goodbye {player}, see you again!")
                            loading_animation(['=>  ', '=>  ', '=>  '], delay=1)
                            exit()
                        else:
                            type_text("Invalid choice. Returning to main menu.")
                            break

                    enemy_attack = lambda: enemy.attack(player1)
                    enemy_defense = lambda: enemy.defense()

                    enemy_choice = random.choice([
                        enemy_attack, enemy_defense,
                        enemy_attack, enemy_defense,
                        enemy_defense
                    ])
                    if damage <= 25:
                        if random.choices([True, False], weights=[9, 7])[0]:
                            gojo_taunt = random.choice(gojo_dialog_low)
                            dual_text(*gojo_taunt, delay=0.05)
                    if damage > 25:
                        if random.choices([True, False], weights=[9, 7])[0]:
                            gojo_impressed = random.choice(gojo_dialog_high)
                            dual_text(*gojo_impressed, delay=0.05)

                    if enemy_choice == enemy_defense:
                        if random.choices([True, False], weights=[9, 7])[0]:
                            gojo_defense = random.choice(gojo_dialog_defense)
                            dual_text(*gojo_defense, delay=0.05)

                    enemy_choice()
                    loading_animation(['=>  ', '=>  ', '=>  '])

        # ------------------------ SUKUNA BATTLE ------------------------
        if opponent_choice in ['sukuna', '2']:
            battle_sukuna = True
            while battle_sukuna:
                battle_sukuna = False  
                enemy_name = SUKU + "Sukuna" + RESET
                player1 = SignPlayer(player, health=100, max_health=100)
                enemy = Enemy(enemy_name, health=199, max_health=285)

                loading_animation(['=>  ', '=>  ', '=>  ', '=>  ', '=>  '])
                print(" ")
                type_text(f"'{enemy_name} approaches. His gaze is sharp towards {player}'", delay=0.1)
                time.sleep(1)
                loading_animation(['.', '.', '.'])
                dual_text("まったく鬱陶しいガキだな", "Annoying brat", delay=0.1)
                time.sleep(2)
                dual_text("いいだろう、ここで死ね", "Fine, die here", delay=0.1)
                print(" ")
                loading_animation(['=>  ', '=>  ', '=>  '], delay=0.5)
                print(" ")

                type_text("Information: ")
                time.sleep(1)
                game_info = {
                    "Player": player,
                    "Health": GREEN + str(player1.health) + " HP" + RESET,
                    "Skill": "Attack and Defense"
                }
                for key, value in game_info.items():
                    type_text(f"{key}: {value}")
                print(" ")
                loading_animation(['=>  ', '=>  ', '=>  '])
                print(" ")

                type_text(f"Crimson Valor: Be careful {player}! {enemy_name} has regeneration abilities exceeding {GREEN}285 HP{RESET}", delay=0.01)
                type_text(f"Use defense to heal and attack to strike!", delay=0.01)
                type_text("We wish you the best", delay=0.01)
                print(" ")
                loading_animation(['=>  ', '=>  ', '=>  '], delay=1)

                while True:
                    if player1.health == 0:
                        sukuna_wins = random.choice(sukuna_dialog_victory)
                        dual_text(*sukuna_wins, delay=0.07)
                        print(' ')
                        print(' ')
                        time.sleep(2)
                        loading_down(['↓', '↓', '↓'], delay=1.5)
                        type_text(f"Crimson Valor: We... honor your struggle, {player}")
                        print(" ")
                        loading_animation(['=>  ', '=>  ', '=>  '])
                        type_text("Crimson Valor: Retrying won't erase your spirit!")

                        options_after_loss = {
                            "1": "Try again",
                            "2": "Main Menu",
                            "3": "Leave"
                        }

                        for number, option in options_after_loss.items():
                            type_text(f"{number}. {option}")

                        player_choice = type_input(f"{player}: ").lower()

                        if player_choice in ["1", "try again", "one"]:
                            type_text(f"Good luck fighting again, {player}!")
                            battle_sukuna = True
                            break

                        elif player_choice in ["2", "main menu", "two"]:
                            return_to_menu = True
                            loading_animation(['=>  ', '=>  ', '=>  '])
                            print(" ")
                            break  

                        elif player_choice in ["3", "leave", "three"]:
                            type_text(f"Goodbye {player}, see you again!")
                            loading_animation(['=>  ', '=>  ', '=>  '], delay=1)
                            exit()
                        else:
                            type_text("Invalid choice. Returning to main menu.")
                            break

                    type_text(f"{enemy_name}: {GREEN}{enemy.health} HP{RESET}")
                    type_text(f"{player}: {GREEN}{player1.health} HP{RESET}")

                    player_options = {
                        "1": "Attack",
                        "2": "Defense"
                    }

                    for number, option in player_options.items():
                        type_text(f"{number}. {option}")

                    decision = type_input(f"{player}: ")

                    loading_animation(['=>  ', '=>  ', '=>  '])
                    print(" ")

                    if decision == "1":
                        damage = player1.attack(enemy)
                        time.sleep(2)
                    elif decision == "2":
                        player1.defense()

                    loading_animation(['=>  ', '=>  ', '=>  '])
                    print(" ")

                    if enemy.health == 0:
                        sukuna_loses = random.choice(sukuna_dialog_defeat)
                        dual_text(*sukuna_loses, delay=0.07)
                        print(' ')
                        print(' ')
                        time.sleep(2)
                        type_text(f"Crimson Valor: Congratulations {player}! You defeated {enemy_name}!")
                        time.sleep(2)
                        type_text("Reward has been sent!")
                        loading_animation(['=>  ', '=>  ', '=>  '])

                        options_after_win = {
                            "1": "Main Menu",
                            "2": f"Fight {RED}Sukuna{RESET} again!",
                            "3": "Leave with victory"
                        }

                        for number, option in options_after_win.items():
                            type_text(f"{number}. {option}")

                        player_choice = type_input(f"{player}: ").lower()

                        if player_choice in ["1", "main menu", "one"]:
                            return_to_menu = True
                            loading_animation(['=>  ', '=>  ', '=>  '])
                            print(" ")
                            break

                        if player_choice in ["2", "fight sukuna", "two"]:
                            type_text(f"Good luck fighting again, {player}!")
                            battle_sukuna = True
                            break

                        elif player_choice in ["3", "leave", "three", "leave with victory"]:
                            type_text(f"Goodbye {player}, see you again!")
                            loading_animation(['=>  ', '=>  ', '=>  '], delay=1)
                            exit()
                        else:
                            type_text("Invalid choice. Returning to main menu.")
                            break

                    enemy_attack = lambda: enemy.attack(player1)
                    enemy_defense = lambda: enemy.defense()

                    enemy_choice = random.choice([
                        enemy_attack, enemy_defense,
                        enemy_attack, enemy_defense,
                        enemy_defense
                    ])
                    if damage <= 25:
                        if random.choices([True, False], weights=[9, 7])[0]:
                            sukuna_taunt = random.choice(sukuna_dialog_low)
                            dual_text(*sukuna_taunt, delay=0.05)
                    if damage > 25:
                        if random.choices([True, False], weights=[9, 7])[0]:
                            sukuna_impressed = random.choice(sukuna_dialog_high)
                            dual_text(*sukuna_impressed, delay=0.05)

                    if enemy_choice == enemy_defense:
                        if random.choices([True, False], weights=[9, 7])[0]:
                            sukuna_defense = random.choice(sukuna_dialog_defense)
                            dual_text(*sukuna_defense, delay=0.05)

                    enemy_choice()
                    loading_animation(['=>  ', '=>  ', '=>  '])

        # ------------------------ MAHORAGA BATTLE ------------------------
        if opponent_choice in ['mahoraga', '3']:
            battle_mahoraga = True
            while battle_mahoraga:
                battle_mahoraga = False  
                enemy_name = MAHO + "Mahoraga" + RESET
                player1 = SignPlayer(player, health=100, max_health=100)
                enemy = Enemy(enemy_name, health=240, max_health=370)
                loading_animation(['=>  ', '=>  ', '=>  ', '=>  ', '=>  '])
                print(" ")
                type_text(f"'Heavy footsteps echo. {enemy_name} slowly appears before {player}.'", delay=0.1)
                time.sleep(1)
                time.sleep(2)
                print(' ')
                dual_text("……（ギィィィン…）", "……Sound of a wheel spinning slowly", delay=0.1)
                time.sleep(2)
                dual_text("……（目が光る）", "……Its eyes glow sharply", delay=0.1)
                print(" ")
                loading_animation(['=>  ', '=>  ', '=>  '], delay=0.5)
                print(" ")

                type_text("Information: ")
                time.sleep(1)
                game_info = {
                    "Player": player,
                    "Health": GREEN + str(player1.health) + " HP" + RESET,
                    "Skill": "Attack and Defense"
                }
                for key, value in game_info.items():
                    type_text(f"{key}: {value}")
                print(" ")
                loading_animation(['=>  ', '=>  ', '=>  '])
                print(" ")

                type_text(f"Crimson Valor: {enemy_name} is no weak opponent, {player}! Its power can reach {GREEN}370 HP{RESET}!", delay=0.01)
                type_text(f"Always use defense when critical!", delay=0.01)
                type_text("May this be the best path to save the world", delay=0.01)
                print(" ")
                loading_animation(['=>  ', '=>  ', '=>  '], delay=1)

                while True:
                    if player1.health == 0:
                        maho_wins = random.choice(mahoraga_dialog_victory)
                        dual_text(*maho_wins, delay=0.07)
                        print(' ')
                        print(' ')
                        time.sleep(2)
                        loading_down(['↓', '↓', '↓'], delay=1.5)
                        type_text(f"Crimson Valor: We... honor your struggle, {player}")
                        print(" ")
                        loading_animation(['=>  ', '=>  ', '=>  '])
                        type_text("Crimson Valor: Retrying won't erase your spirit!")

                        options_after_loss = {
                            "1": "Try again",
                            "2": "Main Menu",
                            "3": "Leave"
                        }

                        for number, option in options_after_loss.items():
                            type_text(f"{number}. {option}")

                        player_choice = type_input(f"{player}: ").lower()

                        if player_choice in ["1", "try again", "one"]:
                            type_text(f"Good luck fighting again, {player}!")
                            battle_mahoraga = True
                            break

                        elif player_choice in ["2", "main menu", "two"]:
                            return_to_menu = True
                            loading_animation(['=>  ', '=>  ', '=>  '])
                            print(" ")
                            break  

                        elif player_choice in ["3", "leave", "three"]:
                            type_text(f"Goodbye {player}, see you again!")
                            loading_animation(['=>  ', '=>  ', '=>  '], delay=1)
                            exit()
                        else:
                            type_text("Invalid choice. Returning to main menu.")
                            break

                    type_text(f"{enemy_name}: {GREEN}{enemy.health} HP{RESET}")
                    type_text(f"{player}: {GREEN}{player1.health} HP{RESET}")

                    player_options = {
                        "1": "Attack",
                        "2": "Defense"
                    }

                    for number, option in player_options.items():
                        type_text(f"{number}. {option}")

                    decision = type_input(f"{player}: ")

                    loading_animation(['=>  ', '=>  ', '=>  '])
                    print(" ")

                    if decision == "1":
                        damage = player1.attack(enemy)
                        time.sleep(2)
                    elif decision == "2":
                        player1.defense()

                    loading_animation(['=>  ', '=>  ', '=>  '])
                    print(" ")

                    if enemy.health == 0:
                        maho_loses = random.choice(mahoraga_dialog_defeat)
                        dual_text(*maho_loses, delay=0.07)
                        print(' ')
                        print(' ')
                        time.sleep(2)
                        type_text(f"Crimson Valor: Congratulations {player}! You defeated {enemy_name}!")
                        time.sleep(2)
                        type_text("Reward has been sent!")
                        loading_animation(['=>  ', '=>  ', '=>  '])

                        options_after_win = {
                            "1": "Main Menu",
                            "2": f"Fight {enemy_name} again!",
                            "3": "Leave with victory"
                        }

                        for number, option in options_after_win.items():
                            type_text(f"{number}. {option}")

                        player_choice = type_input(f"{player}: ").lower()

                        if player_choice in ["1", "main menu", "one"]:
                            return_to_menu = True
                            loading_animation(['=>  ', '=>  ', '=>  '])
                            print(" ")
                            break

                        if player_choice in ["2", "fight mahoraga", "two"]:
                            type_text(f"Good luck fighting again, {player}!")
                            battle_mahoraga = True
                            break

                        elif player_choice in ["3", "leave", "three", "leave with victory"]:
                            type_text(f"Goodbye {player}, see you again!")
                            loading_animation(['=>  ', '=>  ', '=>  '], delay=1)
                            exit()
                        else:
                            type_text("Invalid choice. Returning to main menu.")
                            break

                    enemy_attack = lambda: enemy.attack(player1)
                    enemy_defense = lambda: enemy.defense()

                    enemy_choice = random.choice([
                        enemy_attack, enemy_defense,
                        enemy_attack, enemy_defense,
                        enemy_defense
                    ])
                    if damage <= 25:
                        if random.choices([True, False], weights=[9, 7])[0]:
                            maho_taunt = random.choice(mahoraga_dialog_low)
                            dual_text(*maho_taunt, delay=0.05)
                    if damage > 25:
                        if random.choices([True, False], weights=[9, 7])[0]:
                            maho_impressed = random.choice(mahoraga_dialog_high)
                            dual_text(*maho_impressed, delay=0.05)

                    if enemy_choice == enemy_defense:
                        if random.choices([True, False], weights=[9, 7])[0]:
                            maho_defense = random.choice(mahoraga_dialog_defense)
                            dual_text(*maho_defense, delay=0.05)

                    enemy_choice()
                    loading_animation(['=>  ', '=>  ', '=>  '])






