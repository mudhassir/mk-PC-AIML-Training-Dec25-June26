#!/usr/bin/env python3
### Building a Python Adventure Game with GitHub Copilot (Text Based)
### main.py
### Developers: Mudhassir Khan & Aariz Khan + GitHub Copilot
### Date: January 7 2026
### Description: This is the main file for a text-based adventure game built using Python and GitHub Copilot.

import random
import time

def slow_print(text):
    """Print text slowly for NPC dialogue"""
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(.05)
    print()

def print_text(text):
    """Normal print with newline"""
    print(text)

# ===================== ORE DATA =====================
ORES = {
    "Stone": {"rarity": "Common", "rocks": ["Pebble"], "chance": "1/1", "multiplier": 0.2, "price": 3},
    "Sand Stone": {"rarity": "Common", "rocks": ["Pebble", "Rock"], "chance": "1/2", "multiplier": 0.25, "price": 3.75},
    "Copper": {"rarity": "Common", "rocks": ["Pebble", "Rock", "Boulder"], "chance": "1/3", "multiplier": 0.3, "price": 4.5},
    "Iron": {"rarity": "Common", "rocks": ["Pebble", "Rock", "Boulder"], "chance": "1/5", "multiplier": 0.35, "price": 5.25},
    "Tin": {"rarity": "Uncommon", "rocks": ["Rock", "Boulder"], "chance": "1/7", "multiplier": 0.425, "price": 6.38},
    "Silver": {"rarity": "Uncommon", "rocks": ["Rock", "Boulder", "Basalt Rock"], "chance": "1/12", "multiplier": 0.5, "price": 7.5},
    "Gold": {"rarity": "Uncommon", "rocks": ["Boulder", "Basalt Rock"], "chance": "1/16", "multiplier": 0.65, "price": 19.5},
    "Mushroomite": {"rarity": "Rare", "rocks": ["Rock", "Boulder"], "chance": "1/22", "multiplier": 0.8, "price": 12},
    "Platinum": {"rarity": "Rare", "rocks": ["Boulder", "Basalt Rock"], "chance": "1/28", "multiplier": 0.8, "price": 12},
    "Bananite": {"rarity": "Uncommon", "rocks": ["Rock", "Boulder"], "chance": "1/30", "multiplier": 0.85, "price": 12.75},
    "Cardboardite": {"rarity": "Common", "rocks": ["Rock", "Boulder"], "chance": "1/31", "multiplier": 0.7, "price": 10.5},
    "Aite": {"rarity": "Epic", "rocks": ["Boulder"], "chance": "1/44", "multiplier": 1.1, "price": 16.5},
    "Poopite": {"rarity": "Epic", "rocks": ["Pebble", "Rock", "Boulder"], "chance": "1/131", "multiplier": 1.2, "price": 18}
}

# ===================== WEAPON DATA =====================
WEAPONS = {
    # Daggers
    "Dagger": {"damage": 4.3, "atk_speed": 0.35, "size": 6, "price": 68, "chance": "1/1"},
    "Falchion Knife": {"damage": 4.3, "atk_speed": 0.35, "size": 6, "price": 45, "chance": "1/2"},
    "Gladius Dagger": {"damage": 4.3, "atk_speed": 0.35, "size": 6, "price": 68, "chance": "1/4"},
    "Hook": {"damage": 4.73, "atk_speed": 0.39, "size": 6, "price": 68, "chance": "1/16"},
    
    # Swords
    "Falchion Sword": {"damage": 7.5, "atk_speed": 0.59, "size": 8, "price": 120, "chance": "1/1"},
    "Gladius Sword": {"damage": 7.875, "atk_speed": 0.62, "size": 8, "price": 120, "chance": "1/2"},
    "Cutlass": {"damage": 9.375, "atk_speed": 0.66, "size": 8, "price": 120, "chance": "1/2"},
    "Rapier": {"damage": 7.5, "atk_speed": 0.49, "size": 8, "price": 120, "chance": "1/4"},
    "Chaos": {"damage": 9.75, "atk_speed": 0.59, "size": 8, "price": 120, "chance": "1/16"},
    "Candy Cane": {"damage": 7.5, "atk_speed": 0.44, "size": 8, "price": 120, "chance": "1/8"},
    "Hell Slayer": {"damage": 10.125, "atk_speed": 0.59, "size": 8, "price": 120, "chance": "1/10"},
    
    # Maces
    "Mace": {"damage": 6, "atk_speed": 0.46, "size": 8, "price": 205, "chance": "1/1"},
    "Spiked Mace": {"damage": 6.3, "atk_speed": 0.46, "size": 8, "price": 205, "chance": "1/2"},
    "Winged Mace": {"damage": 6.6, "atk_speed": 0.46, "size": 8, "price": 205, "chance": "1/4"},
    "Hammerhead Mace": {"damage": 6.9, "atk_speed": 0.46, "size": 8, "price": 205, "chance": "1/8"},
    "Grave Maker": {"damage": 7.8, "atk_speed": 0.46, "size": 8, "price": 205, "chance": "1/16"},
    
    # Gloves
    "Ironhand": {"damage": 7.6, "atk_speed": 0.51, "size": 6, "price": 205, "chance": "1/1"},
    "Boxing Gloves": {"damage": 8, "atk_speed": 0.59, "size": 6, "price": 153, "chance": "1/4"},
    "Relevator": {"damage": 9.6, "atk_speed": 0.69, "size": 6, "price": 205, "chance": "1/4"},
    "Savage Claws": {"damage": 8, "atk_speed": 0.47, "size": 6, "price": 205, "chance": "1/4"},
    
    # Axes
    "Axe": {"damage": 7, "atk_speed": 0.48, "size": 8, "price": 205, "chance": "1/1"},
    "Battleaxe": {"damage": 7.35, "atk_speed": 0.48, "size": 8, "price": 205, "chance": "1/2"},
    "Curved Handle Axe": {"damage": 7.7, "atk_speed": 0.48, "size": 8, "price": 205, "chance": "1/4"},
    "Spade Armed Axe": {"damage": 8.05, "atk_speed": 0.48, "size": 8, "price": 205, "chance": "1/8"},
    
    # Katanas
    "Uchigatana": {"damage": 8.5, "atk_speed": 0.6, "size": 9, "price": 324, "chance": "1/1"},
    "Tachi": {"damage": 8.925, "atk_speed": 0.63, "size": 9, "price": 243, "chance": "1/4"},
    
    # Crusader Swords
    "Crusader Sword": {"damage": 12, "atk_speed": 1, "size": 9, "price": 485, "chance": "1/1"},
    "Long Sword": {"damage": 12, "atk_speed": 1.11, "size": 9, "price": 485, "chance": "1/2"},
    
    # Spears
    "Spear": {"damage": 7.5, "atk_speed": 0.45, "size": 11, "price": 120, "chance": "1/1"},
    "Trident": {"damage": 7.5, "atk_speed": 0.45, "size": 11, "price": 120, "chance": "1/2"},
    "Angelic Spear": {"damage": 9.75, "atk_speed": 0.41, "size": 11, "price": 120, "chance": "1/8"},
    
    # Two-Handed Weapons
    "Double Battle Axe": {"damage": 15.75, "atk_speed": 1.05, "size": 9, "price": 850, "chance": "1/1"},
    "Scythe": {"damage": 14.25, "atk_speed": 0.95, "size": 9, "price": 850, "chance": "1/4"},
    "Greater Battle Axe": {"damage": 17.25, "atk_speed": 1, "size": 9, "price": 850, "chance": "1/4"},
    "Wyvern Axe": {"damage": 18.25, "atk_speed": 0.91, "size": 9, "price": 850, "chance": "1/4"},
    
    # Great Weapons
    "Great Sword": {"damage": 20, "atk_speed": 1.2, "size": 10, "price": 1355, "chance": "1/1"},
    "Hammer": {"damage": 22, "atk_speed": 1.24, "size": 10, "price": 1355, "chance": "1/4"},
    "Skull Crusher": {"damage": 24, "atk_speed": 1.4, "size": 10, "price": 1355, "chance": "1/8"},
    "Dragon Slayer": {"damage": 22, "atk_speed": 1.2, "size": 10, "price": 1355, "chance": "1/16"},
    "Comically Large Spoon": {"damage": 18, "atk_speed": 1.12, "size": 10, "price": 1355, "chance": "1/16"},
    "Excalibur": {"damage": 26, "atk_speed": 1.12, "size": 10, "price": 1355, "chance": "1/1000"}
}

# ===================== ARMOR DATA =====================
ARMOR = {
    # Light Armor
    "Light Helmet": {"hp_boost": 3.75, "chance": "1/1", "price": 65, "ore_needed": 3},
    "Light Leggings": {"hp_boost": 4.375, "chance": "1/2", "price": 112.50, "ore_needed": 7},
    "Light Chestplate": {"hp_boost": 5, "chance": "1/3", "price": 225, "ore_needed": 10},
    
    # Medium Armor
    "Medium Helmet": {"hp_boost": 6.25, "chance": "1/1", "price": 335, "ore_needed": "10-17"},
    "Medium Chestplate": {"hp_boost": 8.75, "chance": "1/3", "price": 850, "ore_needed": "17-30"},
    "Medium Leggings": {"hp_boost": 7.5, "chance": "1/2", "price": 485, "ore_needed": "17-27"},
    
    # Knight Armor
    "Knight Helmet": {"hp_boost": 12.5, "chance": "1/1", "price": 1020, "ore_needed": "20-35"},
    "Knight Chestplate": {"hp_boost": 16.25, "chance": "1/3", "price": 1355, "ore_needed": "27-46"},
    "Knight Leggings": {"hp_boost": 13.75, "chance": "1/2", "price": 1200, "ore_needed": "30-46"}
}

# ===================== PICKAXES DATA =====================
PICKAXES = {
    "Stone Pickaxe": {"price": 0, "mining_power": 3, "luck": 0, "rune_slots": 0},
    "Bronze Pickaxe": {"price": 150, "mining_power": 7, "luck": 0, "rune_slots": 0},
    "Iron Pickaxe": {"price": 500, "mining_power": 10, "luck": 5, "rune_slots": 0},
    "Gold Pickaxe": {"price": 1500, "mining_power": 16, "luck": 15, "rune_slots": 1},
    "Platinum Pickaxe": {"price": 5000, "mining_power": 24, "luck": 25, "rune_slots": 2},
    "Stonewake's Pickaxe": {"price": 3333, "mining_power": 33, "luck": 10, "rune_slots": 3},
    "Arcane Pickaxe": {"price": 125000, "mining_power": 115, "luck": 50, "rune_slots": 3}
}

# ===================== ENEMIES DATA =====================
ENEMIES = {
    "Zombie": {
        "health": (20, 52),
        "damage": (6, 11.2),
        "level": (1, 5),
        "gold_loot": (5, 10),
        "exp_loot": (10, 20)
    },
    "Elite Zombie": {
        "health": (70, 295),
        "damage": (20, 20),
        "level": (1, 10),
        "gold_loot": (5, 10),
        "exp_loot": (10, 20)
    },
    "Delver Zombie": {
        "health": (40, 175),
        "damage": (12, 30.4),
        "level": (1, 10),
        "gold_loot": (10, 20),
        "exp_loot": (20, 40)
    },
    "Brute Zombie": {
        "health": (220, 370),
        "damage": (28, 47.5),
        "level": (5, 10),
        "gold_loot": (32.5, 45),
        "exp_loot": (43.33, 60)
    }
}

# ===================== PLAYER CLASS =====================
class Player:
    def __init__(self, name):
        self.name = name
        self.level = 0
        self.exp = 0
        self.gold = 1000
        self.max_hp = 100
        self.hp = 100
        self.pickaxe = None
        self.inventory = {ore: 0 for ore in ORES}
        self.weapons = {}
        self.armor = {}
        self.island = 1
        
    def add_ore(self, ore_name, amount=1):
        if ore_name in self.inventory:
            self.inventory[ore_name] += amount
    
    def remove_ore(self, ore_name, amount):
        if ore_name in self.inventory and self.inventory[ore_name] >= amount:
            self.inventory[ore_name] -= amount
            return True
        return False
    
    def get_total_ores(self):
        return sum(self.inventory.values())
    
    def add_gold(self, amount):
        self.gold += amount
    
    def remove_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False
    
    def add_exp(self, amount):
        self.exp += amount
        # Level up every 100 exp
        if self.exp >= 100:
            self.level += 1
            self.exp = 0
            self.max_hp += 10
            self.hp = self.max_hp

# ===================== GAME CLASS =====================
class Game:
    def __init__(self):
        self.player = None
        self.game_running = True
        
    def start(self):
        """Start the game"""
        slow_print("Welcome young traveller, to the world of Stonewalks Cross!")
        time.sleep(1)
        slow_print("You have arrived in this new, small city to start a new life...")
        time.sleep(1)
        
        # Get player name
        print_text("\nWhat is your name, young traveller?")
        name = input("> ").strip()
        self.player = Player(name)
        
        time.sleep(1)
        slow_print(f"Welcome, {name}. I am Sensei Moro, and I will teach you the basics of survival.")
        time.sleep(1)
        self.main_menu()
    
    def main_menu(self):
        """Main menu loop"""
        self.introduce_sensei_moro()
        
        while self.game_running:
            print_text("\n" + "="*50)
            print_text(f"Level: {self.player.level} | Gold: ${self.player.gold} | HP: {self.player.hp}/{self.player.max_hp}")
            print_text(f"Total Ores: {self.player.get_total_ores()}")
            print_text("="*50)
            print_text("\n1. Go to Forge")
            print_text("2. Go to Marketplace")
            print_text("3. Go to Caves (Mining)")
            print_text("4. Use Portal (Travel)")
            print_text("5. Check Inventory")
            print_text("6. Talk to Sensei Moro")
            print_text("7. Visit Maxacioussess (Pickaxe Shop)")
            print_text("8. Quit Game")
            
            choice = input("\nWhat would you like to do? > ").strip()
            
            if choice == "1":
                self.forge_menu()
            elif choice == "2":
                self.marketplace_menu()
            elif choice == "3":
                self.mining_menu()
            elif choice == "4":
                self.use_portal()
            elif choice == "5":
                self.check_inventory()
            elif choice == "6":
                self.talk_to_sensei_moro()
            elif choice == "7":
                self.pickaxe_shop()
            elif choice == "8":
                slow_print("Thank you for playing! Goodbye!")
                self.game_running = False
            else:
                print_text("Invalid choice. Please try again.")
    
    def introduce_sensei_moro(self):
        """Initial introduction from Sensei Moro"""
        time.sleep(1)
        slow_print("Sensei Moro: Greetings, traveller! You have arrived in Stonewalks Cross.")
        time.sleep(0.5)
        slow_print("Sensei Moro: To help you get started, I give you a magical Portal...")
        time.sleep(0.5)
        slow_print("Sensei Moro: The Portal is FREE! I also give you 1000 gold coins.")
        time.sleep(0.5)
        
        # Force player to buy pickaxe
        slow_print("Sensei Moro: Now, you must visit Maxacioussess to buy a pickaxe.")
        time.sleep(0.5)
        slow_print("Sensei Moro: He will give you a special offer on the Bronze Pickaxe for only 150 gold!")
        
        self.player.pickaxe = "Bronze Pickaxe"
        self.player.remove_gold(150)
        
        slow_print(f"Sensei Moro: Excellent! You now have the Bronze Pickaxe. Your gold: ${self.player.gold}")
        time.sleep(1)
    
    def talk_to_sensei_moro(self):
        """Talk to Sensei Moro"""
        print_text("\n" + "="*50)
        slow_print("Sensei Moro: Ah, hello again, " + self.player.name + "!")
        time.sleep(0.5)
        slow_print("Sensei Moro: You are level " + str(self.player.level) + ".")
        time.sleep(0.5)
        
        if self.player.level >= 10:
            slow_print("Sensei Moro: You are strong enough to use the Portal!")
        else:
            slow_print("Sensei Moro: You need to reach level 10 to use the Portal.")
        
        time.sleep(0.5)
        slow_print("Sensei Moro: Keep training and gathering resources!")
        print_text("="*50)
    
    def mining_menu(self):
        """Mining menu"""
        if not self.player.pickaxe:
            slow_print("You don't have a pickaxe! Visit Maxacioussess to buy one.")
            return
        
        print_text("\n" + "="*50)
        print_text("Welcome to the CAVES!")
        print_text("="*50)
        print_text(f"\nYou have: {self.player.pickaxe}")
        print_text(f"Mining Power: {PICKAXES[self.player.pickaxe]['mining_power']}")
        print_text(f"Luck Boost: {PICKAXES[self.player.pickaxe]['luck']}%")
        
        print_text("\nHow many rocks do you want to mine? (1-20)")
        try:
            num_rocks = int(input("> ").strip())
            if 1 <= num_rocks <= 20:
                self.mine_rocks(num_rocks)
            else:
                print_text("Please enter a number between 1 and 20.")
        except ValueError:
            print_text("Invalid input. Please enter a number.")
    
    def mine_rocks(self, num_rocks):
        """Mine rocks and get ores"""
        rock_types = ["Pebble", "Rock", "Boulder"]
        ores_found = {}
        
        slow_print(f"\nYou begin mining {num_rocks} rocks...\n")
        
        for i in range(num_rocks):
            rock = random.choice(rock_types)
            ore_found = self.get_ore_from_rock(rock)
            
            if ore_found:
                print_text(f"Rock {i+1}: {rock} -> Found {ore_found}!")
                ores_found[ore_found] = ores_found.get(ore_found, 0) + 1
                self.player.add_ore(ore_found, 1)
            else:
                print_text(f"Rock {i+1}: {rock} -> Nothing valuable...")
            
            time.sleep(0.3)
        
        print_text("\n" + "="*50)
        print_text("Mining Complete! Here's what you found:")
        for ore, count in ores_found.items():
            print_text(f"{ore}: {count}")
        print_text("="*50)
        
        # Random encounter with zombie
        if random.randint(1, 5) == 1:  # 20% chance
            self.encounter_enemy()
    
    def get_ore_from_rock(self, rock_type):
        """Determine which ore comes from a rock"""
        luck_bonus = PICKAXES[self.player.pickaxe]["luck"] / 100
        
        for ore_name, ore_data in ORES.items():
            if rock_type not in ore_data["rocks"]:
                continue
            
            chance_str = ore_data["chance"].split("/")
            numerator = int(chance_str[0])
            denominator = int(chance_str[1])
            
            # Apply luck bonus
            adjusted_chance = numerator / denominator + (numerator / denominator * luck_bonus)
            
            if random.random() < adjusted_chance:
                return ore_name
        
        return None
    
    def encounter_enemy(self):
        """Random enemy encounter"""
        enemy_type = random.choice(list(ENEMIES.keys()))
        enemy_data = ENEMIES[enemy_type]
        
        health = random.uniform(enemy_data["health"][0], enemy_data["health"][1])
        damage = random.uniform(enemy_data["damage"][0], enemy_data["damage"][1])
        level = random.randint(enemy_data["level"][0], enemy_data["level"][1])
        
        print_text("\n" + "="*50)
        slow_print(f"A wild {enemy_type} appears!")
        time.sleep(0.5)
        print_text(f"Level: {level} | Health: {int(health)} | Damage: {damage:.1f}")
        print_text("="*50)
        
        self.combat(enemy_type, health, damage, level, enemy_data)
    
    def combat(self, enemy_type, health, damage, level, enemy_data):
        """Combat system"""
        in_combat = True
        player_hp = self.player.hp
        
        while in_combat and health > 0 and player_hp > 0:
            print_text("\n1. Attack")
            print_text("2. Defend")
            print_text("3. Run")
            
            choice = input("\nWhat do you do? > ").strip()
            
            if choice == "1":
                # Player attacks
                player_damage = random.uniform(5, 15)
                health -= player_damage
                print_text(f"You deal {player_damage:.1f} damage!")
                
                if health <= 0:
                    print_text(f"\nYou defeated the {enemy_type}!")
                    gold_loot = random.uniform(enemy_data["gold_loot"][0], enemy_data["gold_loot"][1])
                    exp_loot = random.uniform(enemy_data["exp_loot"][0], enemy_data["exp_loot"][1])
                    
                    self.player.add_gold(gold_loot)
                    self.player.add_exp(int(exp_loot))
                    
                    print_text(f"Gold: +${int(gold_loot)}")
                    print_text(f"Experience: +{int(exp_loot)}")
                    break
                
                # Enemy attacks
                enemy_damage = random.uniform(damage * 0.8, damage)
                player_hp -= enemy_damage
                print_text(f"The {enemy_type} deals {enemy_damage:.1f} damage to you!")
            
            elif choice == "2":
                # Defend reduces damage
                enemy_damage = random.uniform(damage * 0.2, damage * 0.5)
                player_hp -= enemy_damage
                slow_print("You brace for impact...")
                print_text(f"You take {enemy_damage:.1f} reduced damage!")
            
            elif choice == "3":
                # Attempt to run
                if random.randint(1, 2) == 1:
                    print_text("You managed to escape!")
                    in_combat = False
                else:
                    print_text("The enemy blocked your escape!")
                    enemy_damage = random.uniform(damage * 0.9, damage)
                    player_hp -= enemy_damage
                    print_text(f"The {enemy_type} deals {enemy_damage:.1f} damage!")
            
            print_text(f"Your HP: {int(player_hp)}")
        
        self.player.hp = int(player_hp)
        
        if player_hp <= 0:
            slow_print("You have been defeated...")
            self.player.hp = self.player.max_hp
            print_text("You respawn at the entrance of the cave.")
    
    def forge_menu(self):
        """Forge menu"""
        print_text("\n" + "="*50)
        print_text("Welcome to the FORGE!")
        print_text("="*50)
        
        print_text("\n1. Forge Weapon")
        print_text("2. Forge Armor")
        print_text("3. Back to Menu")
        
        choice = input("\nWhat would you like to do? > ").strip()
        
        if choice == "1":
            self.forge_weapon_menu()
        elif choice == "2":
            self.forge_armor_menu()
    
    def forge_weapon_menu(self):
        """Weapon forging menu"""
        print_text("\n" + "="*50)
        print_text("WEAPON FORGE")
        print_text("="*50)
        
        weapons_list = list(WEAPONS.keys())
        for i, weapon in enumerate(weapons_list, 1):
            weapon_data = WEAPONS[weapon]
            print_text(f"{i}. {weapon} - {weapon_data['damage']} DMG - ${weapon_data['price']}")
        
        print_text(f"{len(weapons_list) + 1}. Back")
        
        try:
            choice = int(input("\nSelect weapon to forge: > ").strip())
            if 1 <= choice <= len(weapons_list):
                weapon_name = weapons_list[choice - 1]
                self.forge_weapon(weapon_name)
            elif choice == len(weapons_list) + 1:
                return
            else:
                print_text("Invalid choice.")
        except ValueError:
            print_text("Invalid input.")
    
    def forge_weapon(self, weapon_name):
        """Forge a specific weapon"""
        weapon_data = WEAPONS[weapon_name]
        
        print_text(f"\n" + "="*50)
        print_text(f"Forging: {weapon_name}")
        print_text(f"Damage: {weapon_data['damage']} | Speed: {weapon_data['atk_speed']}s")
        print_text(f"Success Chance: {weapon_data['chance']}")
        print_text("="*50)
        
        print_text("\nYour current inventory:")
        total_ores = 0
        main_ore = None
        max_ore_count = 0
        
        for ore_name, count in self.player.inventory.items():
            if count > 0:
                print_text(f"{ore_name}: {count}")
                total_ores += count
                if count > max_ore_count:
                    max_ore_count = count
                    main_ore = ore_name
        
        if total_ores == 0:
            print_text("You don't have any ores! Mine some first.")
            return
        
        ore_cost = weapon_data['size']
        if total_ores < ore_cost:
            print_text(f"You need at least {ore_cost} ores to forge this weapon. You have {total_ores}.")
            return
        
        # Ask player to confirm and use ores
        print_text(f"\nThis weapon requires {ore_cost} ores to forge.")
        
        # Remove ores from inventory
        ores_used = 0
        for ore_name in self.player.inventory:
            if ores_used >= ore_cost:
                break
            available = self.player.inventory[ore_name]
            if available > 0:
                use_amount = min(available, ore_cost - ores_used)
                self.player.remove_ore(ore_name, use_amount)
                ores_used += use_amount
        
        # Roll for success
        chance_str = weapon_data['chance'].split("/")
        success_chance = int(chance_str[0]) / int(chance_str[1])
        
        if random.random() < success_chance:
            slow_print("You successfully forged the weapon!")
            if weapon_name not in self.player.weapons:
                self.player.weapons[weapon_name] = 0
            self.player.weapons[weapon_name] += 1
            print_text(f"You now have {self.player.weapons[weapon_name]} {weapon_name}(s)")
        else:
            slow_print("The forging failed... Your ores were lost.")
    
    def forge_armor_menu(self):
        """Armor forging menu"""
        print_text("\n" + "="*50)
        print_text("ARMOR FORGE")
        print_text("="*50)
        
        armor_list = list(ARMOR.keys())
        for i, armor in enumerate(armor_list, 1):
            armor_data = ARMOR[armor]
            print_text(f"{i}. {armor} - +{armor_data['hp_boost']}% HP - ${armor_data['price']}")
        
        print_text(f"{len(armor_list) + 1}. Back")
        
        try:
            choice = int(input("\nSelect armor to forge: > ").strip())
            if 1 <= choice <= len(armor_list):
                armor_name = armor_list[choice - 1]
                self.forge_armor(armor_name)
            elif choice == len(armor_list) + 1:
                return
            else:
                print_text("Invalid choice.")
        except ValueError:
            print_text("Invalid input.")
    
    def forge_armor(self, armor_name):
        """Forge armor"""
        armor_data = ARMOR[armor_name]
        
        print_text(f"\n" + "="*50)
        print_text(f"Forging: {armor_name}")
        print_text(f"HP Boost: +{armor_data['hp_boost']}%")
        print_text(f"Success Chance: {armor_data['chance']}")
        print_text("="*50)
        
        print_text("\nYour current inventory:")
        total_ores = 0
        
        for ore_name, count in self.player.inventory.items():
            if count > 0:
                print_text(f"{ore_name}: {count}")
                total_ores += count
        
        if total_ores == 0:
            print_text("You don't have any ores! Mine some first.")
            return
        
        ore_cost = armor_data['ore_needed']
        if isinstance(ore_cost, str):
            parts = ore_cost.split("-")
            min_ore = int(parts[0])
            max_ore = int(parts[1])
            ore_cost = random.randint(min_ore, max_ore)
        
        if total_ores < ore_cost:
            print_text(f"You need at least {ore_cost} ores. You have {total_ores}.")
            return
        
        # Remove ores
        ores_used = 0
        for ore_name in self.player.inventory:
            if ores_used >= ore_cost:
                break
            available = self.player.inventory[ore_name]
            if available > 0:
                use_amount = min(available, ore_cost - ores_used)
                self.player.remove_ore(ore_name, use_amount)
                ores_used += use_amount
        
        # Roll for success
        chance_str = armor_data['chance'].split("/")
        success_chance = int(chance_str[0]) / int(chance_str[1])
        
        if random.random() < success_chance:
            slow_print("You successfully forged the armor!")
            if armor_name not in self.player.armor:
                self.player.armor[armor_name] = 0
            self.player.armor[armor_name] += 1
            
            # Apply HP boost
            hp_increase = int(self.player.max_hp * armor_data['hp_boost'] / 100)
            self.player.max_hp += hp_increase
            self.player.hp = self.player.max_hp
            
            print_text(f"You now have {self.player.armor[armor_name]} {armor_name}(s)")
            print_text(f"Max HP increased by {hp_increase}! New max HP: {self.player.max_hp}")
        else:
            slow_print("The forging failed... Your ores were lost.")
    
    def marketplace_menu(self):
        """Marketplace with Marbles"""
        print_text("\n" + "="*50)
        slow_print("Welcome to the MARKETPLACE!")
        time.sleep(0.5)
        slow_print("Marbles: Hello there! What can I do for you?")
        time.sleep(0.5)
        print_text("="*50)
        
        print_text("\n1. Sell Ores")
        print_text("2. Sell Weapons")
        print_text("3. Sell Armor")
        print_text("4. Leave Marketplace")
        
        choice = input("\nWhat would you like to do? > ").strip()
        
        if choice == "1":
            self.sell_ores()
        elif choice == "2":
            self.sell_weapons()
        elif choice == "3":
            self.sell_armor()
    
    def sell_ores(self):
        """Sell ores"""
        print_text("\n" + "="*50)
        print_text("SELL ORES")
        print_text("="*50)
        
        ores_to_sell = []
        for ore_name, count in self.player.inventory.items():
            if count > 0:
                ores_to_sell.append((ore_name, count))
        
        if not ores_to_sell:
            print_text("You don't have any ores to sell!")
            return
        
        for i, (ore_name, count) in enumerate(ores_to_sell, 1):
            ore_price = ORES[ore_name]["price"]
            total_value = ore_price * count
            print_text(f"{i}. {ore_name}: {count} x ${ore_price} = ${total_value:.2f}")
        
        print_text(f"{len(ores_to_sell) + 1}. Sell All")
        print_text(f"{len(ores_to_sell) + 2}. Cancel")
        
        try:
            choice = int(input("\nWhat would you like to sell? > ").strip())
            
            if choice == len(ores_to_sell) + 1:
                # Sell all
                total_gold = 0
                for ore_name, count in ores_to_sell:
                    ore_price = ORES[ore_name]["price"]
                    total_gold += ore_price * count
                    self.player.remove_ore(ore_name, count)
                
                self.player.add_gold(total_gold)
                slow_print(f"Marbles: Excellent choice! I've paid you ${total_gold:.2f}")
                print_text(f"Your new gold: ${self.player.gold}")
            
            elif 1 <= choice <= len(ores_to_sell):
                ore_name, count = ores_to_sell[choice - 1]
                ore_price = ORES[ore_name]["price"]
                total_value = ore_price * count
                
                print_text(f"\nYou want to sell all {count} {ore_name}? (y/n)")
                confirm = input("> ").strip().lower()
                
                if confirm == 'y':
                    self.player.remove_ore(ore_name, count)
                    self.player.add_gold(total_value)
                    slow_print(f"Marbles: Great! Here's ${total_value:.2f}")
                    print_text(f"Your new gold: ${self.player.gold}")
        
        except ValueError:
            print_text("Invalid input.")
    
    def sell_weapons(self):
        """Sell weapons"""
        print_text("\n" + "="*50)
        print_text("SELL WEAPONS")
        print_text("="*50)
        
        weapons_to_sell = [(w, c) for w, c in self.player.weapons.items() if c > 0]
        
        if not weapons_to_sell:
            print_text("You don't have any weapons to sell!")
            return
        
        for i, (weapon_name, count) in enumerate(weapons_to_sell, 1):
            weapon_price = WEAPONS[weapon_name]["price"]
            total_value = weapon_price * count
            print_text(f"{i}. {weapon_name}: {count} x ${weapon_price} = ${total_value}")
        
        print_text(f"{len(weapons_to_sell) + 1}. Cancel")
        
        try:
            choice = int(input("\nWhat would you like to sell? > ").strip())
            
            if 1 <= choice <= len(weapons_to_sell):
                weapon_name, count = weapons_to_sell[choice - 1]
                
                print_text(f"How many would you like to sell? (1-{count})")
                amount = int(input("> ").strip())
                
                if 1 <= amount <= count:
                    weapon_price = WEAPONS[weapon_name]["price"]
                    total_value = weapon_price * amount
                    
                    self.player.weapons[weapon_name] -= amount
                    self.player.add_gold(total_value)
                    
                    slow_print(f"Marbles: Excellent! Here's ${total_value}")
                    print_text(f"Your new gold: ${self.player.gold}")
        
        except ValueError:
            print_text("Invalid input.")
    
    def sell_armor(self):
        """Sell armor"""
        print_text("\n" + "="*50)
        print_text("SELL ARMOR")
        print_text("="*50)
        
        armor_to_sell = [(a, c) for a, c in self.player.armor.items() if c > 0]
        
        if not armor_to_sell:
            print_text("You don't have any armor to sell!")
            return
        
        for i, (armor_name, count) in enumerate(armor_to_sell, 1):
            armor_price = ARMOR[armor_name]["price"]
            total_value = armor_price * count
            print_text(f"{i}. {armor_name}: {count} x ${armor_price} = ${total_value}")
        
        print_text(f"{len(armor_to_sell) + 1}. Cancel")
        
        try:
            choice = int(input("\nWhat would you like to sell? > ").strip())
            
            if 1 <= choice <= len(armor_to_sell):
                armor_name, count = armor_to_sell[choice - 1]
                
                print_text(f"How many would you like to sell? (1-{count})")
                amount = int(input("> ").strip())
                
                if 1 <= amount <= count:
                    armor_price = ARMOR[armor_name]["price"]
                    total_value = armor_price * amount
                    
                    self.player.armor[armor_name] -= amount
                    self.player.add_gold(total_value)
                    
                    slow_print(f"Marbles: Great! Here's ${total_value}")
                    print_text(f"Your new gold: ${self.player.gold}")
        
        except ValueError:
            print_text("Invalid input.")
    
    def pickaxe_shop(self):
        """Pickaxe shop with Maxacioussess"""
        print_text("\n" + "="*50)
        slow_print("Welcome to the PICKAXE SHOP!")
        time.sleep(0.5)
        slow_print("Maxacioussess: Hello! Looking for a new pickaxe?")
        time.sleep(0.5)
        print_text("="*50)
        
        pickaxe_list = list(PICKAXES.keys())
        
        for i, pickaxe in enumerate(pickaxe_list, 1):
            pickaxe_data = PICKAXES[pickaxe]
            price = "Free" if pickaxe_data["price"] == 0 else f"${pickaxe_data['price']}"
            print_text(f"{i}. {pickaxe} - {price} - Power: {pickaxe_data['mining_power']}")
        
        print_text(f"{len(pickaxe_list) + 1}. Leave Shop")
        
        try:
            choice = int(input("\nWhat pickaxe would you like to buy? > ").strip())
            
            if 1 <= choice <= len(pickaxe_list):
                pickaxe_name = pickaxe_list[choice - 1]
                pickaxe_data = PICKAXES[pickaxe_name]
                
                if self.player.gold >= pickaxe_data["price"]:
                    self.player.remove_gold(pickaxe_data["price"])
                    self.player.pickaxe = pickaxe_name
                    
                    slow_print(f"Maxacioussess: Excellent choice! Here's your {pickaxe_name}")
                    time.sleep(0.5)
                    print_text(f"Your new gold: ${self.player.gold}")
                else:
                    slow_print(f"Maxacioussess: You don't have enough gold!")
        
        except ValueError:
            print_text("Invalid input.")
    
    def check_inventory(self):
        """Check player inventory"""
        print_text("\n" + "="*50)
        print_text("INVENTORY")
        print_text("="*50)
        
        print_text(f"\nLevel: {self.player.level} | Experience: {self.player.exp}")
        print_text(f"Gold: ${self.player.gold}")
        print_text(f"HP: {self.player.hp}/{self.player.max_hp}")
        print_text(f"Current Pickaxe: {self.player.pickaxe if self.player.pickaxe else 'None'}")
        
        print_text("\n--- ORES ---")
        has_ores = False
        for ore_name, count in self.player.inventory.items():
            if count > 0:
                ore_price = ORES[ore_name]["price"]
                total_value = ore_price * count
                print_text(f"{ore_name}: {count} (${total_value:.2f})")
                has_ores = True
        if not has_ores:
            print_text("No ores")
        
        print_text("\n--- WEAPONS ---")
        has_weapons = False
        for weapon_name, count in self.player.weapons.items():
            if count > 0:
                print_text(f"{weapon_name}: {count}")
                has_weapons = True
        if not has_weapons:
            print_text("No weapons")
        
        print_text("\n--- ARMOR ---")
        has_armor = False
        for armor_name, count in self.player.armor.items():
            if count > 0:
                print_text(f"{armor_name}: {count}")
                has_armor = True
        if not has_armor:
            print_text("No armor")
        
        print_text("="*50)
    
    def use_portal(self):
        """Use the portal to travel"""
        print_text("\n" + "="*50)
        print_text("THE PORTAL")
        print_text("="*50)
        
        if self.player.level < 10:
            slow_print(f"Portal: You are level {self.player.level}. You need to be level 10 to travel.")
            print_text("Come back when you're stronger!")
        else:
            slow_print("Portal: Welcome, strong traveller!")
            time.sleep(0.5)
            slow_print("Portal: Island 2 is under construction... Please check back later!")
        
        print_text("="*50)

# ===================== MAIN =====================
if __name__ == "__main__":
    try:
        game = Game()
        game.start()
    except KeyboardInterrupt:
        print("\nGame interrupted. Goodbye!")