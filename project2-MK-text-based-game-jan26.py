
# Mudhassir Khan
# new change
# Course-end Project 2: Text Based Adventure Game

"""
Overview
In this project, you will build a text-based adventure game using Python and GitHub Copilot.
The game will allow users to explore different locations, make choices, and complete a simple quest, 
focusing on fundamental Python concepts such as variables, lists, loops, conditionals, and functions. 
You will use GitHub Copilot to assist in writing functions and improving code efficiency.
By completing this project, you will reinforce core Python skills in a fun and interactive way.

Tool: VS Code with GitHub Copilot extension

Dataset: None

Instructions
• Read the situation, tasks and actions, and result sections carefully to understand the assignment thoroughly
• Follow the tasks and actions provided below to develop the game
• Create a brief report (PDF) summarizing how GitHub Copilot assisted in writing and optimizing the code, the key challenges faced, and any enhancements or modifications made to the original game structure
• Complete and submit your assignment via the Learning Management System (LMS)

Situation
You are a Python programmer looking to practice writing functions and working with conditionals.
You decide to create a text-based adventure game where users explore different locations, encounter challenges, and complete a quest.
You will use GitHub Copilot to help generate and refine your code to speed up development.
The final product should be an interactive command-line interface (CLI) where players can make choices and navigate the game world.
"""

# ============================================================================
# TEXT-BASED ADVENTURE GAME - DRAGON'S QUEST
# ============================================================================

import random
from typing import List, Dict

# ============================================================================
# GAME SETUP AND CONSTANTS
# ============================================================================

LOCATIONS = {
    "village": {
        "description": "You are in a quiet village. There's a tavern to the NORTH and a forest to the EAST.",
        "exits": {"north": "tavern", "east": "forest", "south": None},
        "items": ["map", "torch"]
    },
    "tavern": {
        "description": "A bustling tavern filled with adventurers. You see the bartender and a mysterious stranger in the corner.",
        "exits": {"south": "village", "east": "inn", "west": None},
        "items": ["sword", "ale"]
    },
    "inn": {
        "description": "A cozy inn. The innkeeper eyes you suspiciously. You can rest here.",
        "exits": {"west": "tavern", "north": "mountain", "south": None},
        "items": ["key", "journal"]
    },
    "forest": {
        "description": "A dark forest with towering trees. You hear strange noises in the distance.",
        "exits": {"west": "village", "north": "castle", "south": None},
        "items": ["mushroom", "rope"]
    },
    "castle": {
        "description": "An ancient castle looms before you. A dragon's roar echoes from within!",
        "exits": {"south": "forest", "east": "dragon_chamber", "west": None},
        "items": ["shield", "armor"]
    },
    "dragon_chamber": {
        "description": "You enter the dragon's chamber. The dragon stands before you, eyes glowing red!",
        "exits": {"west": "castle", "south": None, "north": None},
        "items": ["treasure", "ancient_scroll"]
    },
    "mountain": {
        "description": "A snow-covered mountain with a small cabin. You can see for miles from here.",
        "exits": {"south": "inn", "east": None, "west": None},
        "items": ["herbs", "golden_compass"]
    }
}

# ============================================================================
# GAME STATE CLASS
# ============================================================================

class Player:
    """Represents the player character with inventory and stats."""
    
    def __init__(self, name: str):
        self.name = name
        self.inventory: List[str] = []
        self.health = 100
        self.gold = 0
        self.current_location = "village"
        self.quests_completed = []
        self.has_defeated_dragon = False
    
    def take_damage(self, damage: int) -> None:
        """Reduce player health."""
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def heal(self, amount: int) -> None:
        """Increase player health."""
        self.health = min(self.health + amount, 100)
    
    def add_item(self, item: str) -> None:
        """Add item to inventory."""
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"✓ You picked up: {item}")
        else:
            print(f"You already have {item}.")
    
    def remove_item(self, item: str) -> bool:
        """Remove item from inventory. Returns True if successful."""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False
    
    def has_item(self, item: str) -> bool:
        """Check if player has an item."""
        return item in self.inventory
    
    def show_status(self) -> None:
        """Display player status."""
        print(f"\n{'='*50}")
        print(f"PLAYER STATUS")
        print(f"{'='*50}")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}/100 {'❤️' if self.health > 50 else '⚠️'}")
        print(f"Gold: {self.gold}")
        print(f"Location: {self.current_location.upper()}")
        print(f"Inventory: {self.inventory if self.inventory else 'Empty'}")
        print(f"Quests Completed: {len(self.quests_completed)}")
        if self.has_defeated_dragon:
            print(f"✓ DRAGON DEFEATED!")
        print(f"{'='*50}\n")

# ============================================================================
# GAME FUNCTIONS
# ============================================================================

def display_location(location_name: str) -> None:
    """Display information about the current location."""
    if location_name not in LOCATIONS:
        print("Error: Location not found!")
        return
    
    location = LOCATIONS[location_name]
    print(f"\n{'='*50}")
    print(f"📍 {location_name.upper()}")
    print(f"{'='*50}")
    print(location["description"])
    
    if location["items"]:
        print(f"\nItems here: {', '.join(location['items'])}")
    else:
        print("\nNo items here.")
    
    print(f"\n{'='*50}\n")

def get_available_exits(location_name: str) -> List[str]:
    """Return list of available exits from current location."""
    location = LOCATIONS[location_name]
    exits = [direction for direction, dest in location["exits"].items() if dest is not None]
    return exits

def move_to_location(player: Player, direction: str) -> bool:
    """Move player to a new location. Returns True if successful."""
    current_location = player.current_location
    
    if current_location not in LOCATIONS:
        print("Error: Invalid location!")
        return False
    
    location = LOCATIONS[current_location]
    
    if direction not in location["exits"] or location["exits"][direction] is None:
        print(f"❌ You can't go {direction} from here.")
        print(f"Available exits: {', '.join(get_available_exits(current_location))}")
        return False
    
    next_location = location["exits"][direction]
    player.current_location = next_location
    print(f"→ Moving {direction}...\n")
    display_location(next_location)
    return True

def pick_up_item(player: Player, item_name: str) -> bool:
    """Pick up an item from the current location."""
    location = LOCATIONS[player.current_location]
    
    item_name_lower = item_name.lower()
    available_items = [item.lower() for item in location["items"]]
    
    if item_name_lower not in available_items:
        print(f"❌ '{item_name}' is not here.")
        return False
    
    # Find the original item name (with correct casing)
    original_item = next(item for item in location["items"] if item.lower() == item_name_lower)
    player.add_item(original_item)
    location["items"].remove(original_item)
    return True

def encounter_enemy(player: Player, enemy_name: str) -> bool:
    """Simulate a battle encounter. Returns True if player wins."""
    print(f"\n⚔️  A wild {enemy_name} appears!")
    
    enemy_health = random.randint(30, 50)
    player_has_weapon = player.has_item("sword")
    
    print(f"Your health: {player.health}")
    print(f"{enemy_name} health: {enemy_health}\n")
    
    while player.health > 0 and enemy_health > 0:
        action = input("Do you want to (A)ttack, (D)efend, or (R)un? ").lower()
        
        if action == 'a':
            damage = random.randint(10, 25) if player_has_weapon else random.randint(5, 15)
            enemy_health -= damage
            print(f"→ You attack! Damage: {damage}")
            print(f"  {enemy_name} health: {enemy_health}\n")
            
        elif action == 'd':
            damage = random.randint(5, 12)
            player.take_damage(damage)
            print(f"→ You defend! {enemy_name} deals {damage} damage")
            print(f"  Your health: {player.health}\n")
            
        elif action == 'r':
            print("→ You run away!")
            return False
        
        else:
            print("Invalid action! Try again.")
            continue
        
        if enemy_health > 0:
            damage = random.randint(8, 18)
            player.take_damage(damage)
            print(f"→ {enemy_name} attacks! Damage: {damage}")
            print(f"  Your health: {player.health}\n")
    
    if player.health > 0:
        print(f"✓ You defeated the {enemy_name}!")
        player.gold += random.randint(50, 150)
        return True
    else:
        print(f"❌ You were defeated by the {enemy_name}!")
        return False

def dragon_boss_fight(player: Player) -> bool:
    """Special encounter with the dragon boss."""
    if not player.has_item("sword") or not player.has_item("shield"):
        print("\n❌ You need a sword and shield to fight the dragon!")
        print("The dragon's flame scorches you!")
        player.take_damage(30)
        return False
    
    print("\n" + "="*60)
    print("🐉 EPIC DRAGON BOSS FIGHT! 🐉")
    print("="*60)
    print("A massive dragon with scales of steel and eyes of fire!")
    print("This is the final battle!\n")
    
    dragon_health = 100
    
    while player.health > 0 and dragon_health > 0:
        action = input("Choose: (A)ttack, (S)pell, (D)efend, or (R)un? ").lower()
        
        if action == 'a':
            damage = random.randint(15, 30)
            dragon_health -= damage
            print(f"→ You slash with your sword! Damage: {damage}")
            print(f"  Dragon health: {dragon_health}\n")
            
        elif action == 's':
            damage = random.randint(20, 40)
            dragon_health -= damage
            print(f"→ You cast a powerful spell! Damage: {damage}")
            print(f"  Dragon health: {dragon_health}\n")
            
        elif action == 'd':
            damage = random.randint(10, 20)
            player.take_damage(damage)
            print(f"→ You raise your shield! Dragon deals reduced {damage} damage")
            print(f"  Your health: {player.health}\n")
            
        elif action == 'r':
            print("→ You cannot flee from the dragon!")
            damage = random.randint(20, 35)
            player.take_damage(damage)
            print(f"  Dragon attacks! Damage: {damage}")
            print(f"  Your health: {player.health}\n")
            continue
        
        else:
            print("Invalid action!")
            continue
        
        if dragon_health > 0:
            damage = random.randint(15, 35)
            player.take_damage(damage)
            print(f"→ Dragon breathes fire! Damage: {damage}")
            print(f"  Your health: {player.health}\n")
    
    if player.health > 0:
        print("\n" + "="*60)
        print("✓✓✓ YOU DEFEATED THE DRAGON! ✓✓✓")
        print("="*60)
        player.gold += 500
        player.has_defeated_dragon = True
        player.quests_completed.append("Defeat the Dragon")
        return True
    else:
        print("\n❌ The dragon was too strong...")
        return False

def quest_forest(player: Player) -> None:
    """Quest: Collect mushrooms from the forest."""
    print("\nAn old wizard asks you to collect 3 mushrooms from the forest.")
    print("He promises a reward!\n")
    
    mushrooms_collected = 0
    while mushrooms_collected < 3:
        action = input("Search for mushrooms? (Y)es or (N)o? ").lower()
        if action == 'y':
            if random.random() > 0.4:
                mushrooms_collected += 1
                print(f"✓ Found a mushroom! ({mushrooms_collected}/3)")
            else:
                print("❌ No mushrooms found here. Keep searching!")
                if random.random() > 0.7:
                    print("⚠️  A wolf approaches!")
                    if not encounter_enemy(player, "Wolf"):
                        print("You flee back to the village.")
                        return
        else:
            print("You abandon the quest.")
            return
    
    print("\n✓ Quest complete! The wizard gives you 100 gold and a potion.")
    player.gold += 100
    player.quests_completed.append("Forest Mushroom Collection")

def main_menu(player: Player) -> str:
    """Display main menu and get player action."""
    print(f"\n{'='*50}")
    print("WHAT DO YOU DO?")
    print(f"{'='*50}")
    print("(M)ove - travel to another location")
    print("(L)ook - examine current location")
    print("(T)ake - pick up an item")
    print("(I)nventory - view inventory")
    print("(S)tatus - view player status")
    print("(Q)uest - accept a quest")
    print("(H)eal - rest and recover health")
    print("(E)xit - quit the game")
    print(f"{'='*50}\n")
    
    return input("Choose an action: ").lower()

def heal_player(player: Player) -> None:
    """Allow player to heal by resting."""
    if player.health >= 100:
        print("You are already at full health!")
        return
    
    print("You rest and recover...")
    player.heal(30)
    print(f"✓ You feel refreshed! Health: {player.health}/100")

# ============================================================================
# MAIN GAME LOOP
# ============================================================================

def play_game() -> None:
    """Main game loop."""
    print("\n" + "="*60)
    print("🎮 WELCOME TO THE TEXT-BASED ADVENTURE GAME 🎮")
    print("="*60)
    print("\nYour quest: Defeat the dragon and save the kingdom!\n")
    
    # Player setup
    player_name = input("Enter your character name: ").strip()
    if not player_name:
        player_name = "Adventurer"
    
    player = Player(player_name)
    
    print(f"\n✓ Welcome, {player_name}!")
    print("Your adventure begins in a quiet village...\n")
    
    display_location(player.current_location)
    
    # Main game loop
    game_running = True
    while game_running:
        action = main_menu(player)
        
        if action == 'm':
            direction = input("Which direction? (north/south/east/west): ").lower()
            move_to_location(player, direction)
        
        elif action == 'l':
            display_location(player.current_location)
        
        elif action == 't':
            item = input("What item do you want to take? ").strip()
            pick_up_item(player, item)
        
        elif action == 'i':
            if player.inventory:
                print(f"\n📦 Your inventory: {', '.join(player.inventory)}")
            else:
                print("\n📦 Your inventory is empty.")
        
        elif action == 's':
            player.show_status()
        
        elif action == 'q':
            if player.current_location == "village":
                print("\nThe village elder approaches you...")
                quest_forest(player)
            elif player.current_location == "dragon_chamber":
                print("\n⚔️ The dragon is here! This is your final quest!")
                if dragon_boss_fight(player):
                    print("\n" + "="*60)
                    print("GAME WON! You have saved the kingdom!")
                    print("="*60)
                        print("\n❌ GAME OVER! You were defeated!")
                    game_running = False
                else:
                    if player.health <= 0:
                        game_running = False
            else:
                print("There are no quests available at this location.")
        
        elif action == 'h':
            heal_player(player)
        
        elif action == 'e':
            print(f"\nThanks for playing, {player_name}!")
            print(f"Final Stats - Gold: {player.gold}, Health: {player.health}")
            print(f"Quests Completed: {len(player.quests_completed)}")
            game_running = False
        
        else:
            print("Invalid action! Try again.")
        
        # Check if player is dead
        if player.health <= 0:
            print("\n❌ GAME OVER! You died!")
            game_running = False

# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    play_game()
