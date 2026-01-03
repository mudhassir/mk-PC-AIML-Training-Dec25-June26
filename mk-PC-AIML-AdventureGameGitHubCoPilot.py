"""
Docstring for mk-PC-AIML-Training-Dec25-June26.mk-PC-AIML-AdventureGameGitHubCoPilot

You are a Python programmer looking to practice writing functions and working with conditionals.
You decide to create a text-based adventure game where users explore different locations, encounter challenges, and complete a quest.
You will use GitHub Copilot to help generate and refine your code to speed up development.
The final product should be an interactive command-line interface (CLI) where players can make choices and navigate the game world.
"""


# You are a Python programmer looking to practice writing functions and working with conditionals. You decide to create a text-based adventure game where users explore different locations, encounter challenges, and complete a quest. You will use GitHub Copilot to help generate and refine your code to speed up development. The final product should be an interactive command-line interface (CLI) where players can make choices and navigate the game world.
# 
# Text-Based Adventure Game with GitHub Copilot
# I'll help you create an interactive text-based adventure game! This project will be perfect for practicing functions, conditionals, and user input handling. Let me create a comprehensive game structure that you can expand with GitHub Copilot's help.
# 
# Text-Based Adventure Game
# Code 
# I've created a complete text-based adventure game that's perfect for practicing with GitHub Copilot! Here's what's included:
# 
# Key Features:
# Core Mechanics:
# 
# Player stats (health, inventory, location)
# Multiple locations to explore
# Item collection and quest system
# Win/lose conditions
# Functions to Practice:
# 
# move_player() - Navigation with conditionals
# encounter_*() - Location-based events
# process_command() - Input parsing
# check_win_condition() - Game state evaluation
# Learning Opportunities:
# 
# Dictionary data structures for game state
# Conditional logic for encounters and choices
# User input handling and validation
# Game loop architecture
# How to Use with GitHub Copilot:
# Expand Locations - Add new location dictionaries, Copilot will suggest similar structures
# Add Items - Create new encounter functions,
# 
# 
# Want to be notified when Claude responds?
# 
# 
# 
# Claude is AI and can make mistakes. Please double-check responses.
"""
Text-Based Adventure Game - Quest for the Crystal of Light
A practice project for functions, conditionals, and user interaction
"""

import time
import sys

# Game State
player = {
    "name": "",
    "health": 100,
    "inventory": [],
    "location": "village",
    "has_crystal": False
}

# Game Data
locations = {
    "village": {
        "name": "Village Square",
        "description": "You stand in the center of a peaceful village. The elder's house is to the north, a dark forest lies east, and mountains rise to the west.",
        "exits": ["north", "east", "west"]
    },
    "elder_house": {
        "name": "Elder's House",
        "description": "A cozy cottage filled with ancient books and mysterious artifacts.",
        "exits": ["south"]
    },
    "forest": {
        "name": "Dark Forest",
        "description": "Twisted trees block most sunlight. You hear strange sounds in the distance.",
        "exits": ["west", "north"]
    },
    "cave": {
        "name": "Crystal Cave",
        "description": "A glittering cave illuminated by magical crystals embedded in the walls.",
        "exits": ["south"]
    },
    "mountains": {
        "name": "Mountain Path",
        "description": "A treacherous path winds up the rocky mountainside. The air grows thin.",
        "exits": ["east", "up"]
    },
    "peak": {
        "name": "Mountain Peak",
        "description": "You've reached the summit. A magnificent view stretches before you.",
        "exits": ["down"]
    }
}

def clear_screen():
    """Simulate clearing the screen with newlines"""
    print("\n" * 2)

def slow_print(text, delay=0.03):
    """Print text with a typewriter effect"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_header():
    """Display game header"""
    print("=" * 60)
    print("  QUEST FOR THE CRYSTAL OF LIGHT".center(60))
    print("=" * 60)
    print()

def display_stats():
    """Display player statistics"""
    print(f"\n{'='*60}")
    print(f"Health: {player['health']} | Location: {locations[player['location']]['name']}")
    print(f"Inventory: {', '.join(player['inventory']) if player['inventory'] else 'Empty'}")
    print(f"{'='*60}\n")

def get_player_name():
    """Get and set player name"""
    print("\nWelcome, brave adventurer!")
    name = input("What is your name? ").strip()
    player["name"] = name if name else "Adventurer"
    print(f"\nGreetings, {player['name']}!")

def intro_story():
    """Display introduction story"""
    slow_print("\nThe village elder approaches you with urgent news...")
    time.sleep(0.5)
    slow_print("'The Crystal of Light has been stolen from our temple!'")
    time.sleep(0.5)
    slow_print("'Without it, darkness will consume our land.'")
    time.sleep(0.5)
    slow_print("'You must venture forth and retrieve it before it's too late!'\n")
    time.sleep(1)

def describe_location():
    """Describe current location"""
    loc = locations[player["location"]]
    print(f"\n--- {loc['name']} ---")
    print(loc["description"])
    print(f"\nExits: {', '.join(loc['exits'])}")

def move_player(direction):
    """Move player to a new location"""
    current_loc = player["location"]
    
    # Define location connections
    connections = {
        "village": {"north": "elder_house", "east": "forest", "west": "mountains"},
        "elder_house": {"south": "village"},
        "forest": {"west": "village", "north": "cave"},
        "cave": {"south": "forest"},
        "mountains": {"east": "village", "up": "peak"},
        "peak": {"down": "mountains"}
    }
    
    if direction not in locations[current_loc]["exits"]:
        print("\nYou can't go that way!")
        return False
    
    player["location"] = connections[current_loc][direction]
    print(f"\nYou travel {direction}...")
    time.sleep(0.5)
    return True

def encounter_elder():
    """Elder house event"""
    if "ancient_map" not in player["inventory"]:
        print("\nThe elder looks at you with wise eyes.")
        print("'Take this ancient map. It will guide you to the Crystal Cave.'")
        player["inventory"].append("ancient_map")
        print("\n[You obtained: Ancient Map]")
    else:
        print("\nThe elder nods encouragingly.")
        print("'Follow the map to the Dark Forest, then head north to the cave.'")

def encounter_forest():
    """Forest encounter event"""
    print("\nA wild goblin jumps out from behind a tree!")
    print("\nWhat do you do?")
    print("1. Fight")
    print("2. Run")
    print("3. Negotiate")
    
    choice = input("\nChoose (1-3): ").strip()
    
    if choice == "1":
        print("\nYou bravely engage in combat!")
        if "sword" in player["inventory"]:
            print("Your sword strikes true! The goblin flees.")
        else:
            print("Without a weapon, you take damage!")
            player["health"] -= 20
            print(f"[-20 Health] Current health: {player['health']}")
    elif choice == "2":
        print("\nYou escape back to the village!")
        player["location"] = "village"
    elif choice == "3":
        print("\nYou offer the goblin some gold.")
        print("The goblin accepts and gives you a rusty sword!")
        player["inventory"].append("sword")
        print("\n[You obtained: Rusty Sword]")
    else:
        print("\nThe goblin attacks while you hesitate!")
        player["health"] -= 15

def encounter_cave():
    """Cave encounter - finding the crystal"""
    if not player["has_crystal"]:
        print("\n✨ In the center of the cave, you see it! ✨")
        slow_print("The Crystal of Light glows with ethereal energy...")
        
        if "ancient_map" in player["inventory"]:
            print("\nUsing the ancient map's knowledge, you safely retrieve the crystal!")
            player["has_crystal"] = True
            player["inventory"].append("Crystal of Light")
            print("\n[You obtained: Crystal of Light]")
            print("\nYou must return it to the village elder!")
        else:
            print("\nBut magical wards protect it. You need the ancient map to proceed safely.")
    else:
        print("\nThe cave is now peaceful, its purpose fulfilled.")

def encounter_mountains():
    """Mountain encounter"""
    print("\nA traveling merchant is resting here.")
    if "sword" not in player["inventory"]:
        print("'Looking for protection? I have this sword for sale - 50 gold.'")
        choice = input("Buy sword? (yes/no): ").strip().lower()
        if choice == "yes":
            print("\nYou don't have gold, but the merchant takes pity on you.")
            player["inventory"].append("sword")
            print("\n[You obtained: Sword]")

def check_win_condition():
    """Check if player has won"""
    if player["has_crystal"] and player["location"] == "elder_house":
        return True
    return False

def game_over():
    """Handle game over"""
    if player["health"] <= 0:
        print("\n" + "="*60)
        print("GAME OVER - You have been defeated!".center(60))
        print("="*60)
        return True
    return False

def victory():
    """Handle victory"""
    clear_screen()
    print("\n" + "="*60)
    print("🎉 VICTORY! 🎉".center(60))
    print("="*60)
    slow_print("\nYou return the Crystal of Light to the elder!")
    slow_print("Light spreads across the land, banishing the darkness.")
    slow_print(f"\nWell done, {player['name']}! You are a true hero!")
    print("\n" + "="*60)

def process_command(command):
    """Process player commands"""
    cmd = command.lower().strip()
    
    # Movement commands
    if cmd in ["north", "south", "east", "west", "up", "down", "n", "s", "e", "w"]:
        direction = {"n": "north", "s": "south", "e": "east", "w": "west"}.get(cmd, cmd)
        move_player(direction)
    
    # Action commands
    elif cmd in ["look", "l"]:
        describe_location()
    elif cmd in ["inventory", "i"]:
        print(f"\nInventory: {', '.join(player['inventory']) if player['inventory'] else 'Empty'}")
    elif cmd in ["stats", "status"]:
        display_stats()
    elif cmd in ["help", "h"]:
        show_help()
    elif cmd in ["quit", "exit", "q"]:
        return False
    else:
        print("\nI don't understand that command. Type 'help' for options.")
    
    return True

def show_help():
    """Display help information"""
    print("\n--- COMMANDS ---")
    print("Movement: north, south, east, west, up, down (or n, s, e, w)")
    print("Actions: look, inventory (i), stats, help (h)")
    print("quit - Exit game")
    print("---------------")

def handle_location_events():
    """Trigger events based on current location"""
    loc = player["location"]
    
    if loc == "elder_house":
        encounter_elder()
    elif loc == "forest" and "forest_cleared" not in player.get("flags", []):
        encounter_forest()
        player.setdefault("flags", []).append("forest_cleared")
    elif loc == "cave":
        encounter_cave()
    elif loc == "mountains" and "mountains_visited" not in player.get("flags", []):
        encounter_mountains()
        player.setdefault("flags", []).append("mountains_visited")

def main_game_loop():
    """Main game loop"""
    running = True
    
    while running:
        if game_over():
            break
        
        if check_win_condition():
            victory()
            break
        
        display_stats()
        describe_location()
        handle_location_events()
        
        command = input(f"\n{player['name']}, what do you do? ").strip()
        
        if not command:
            continue
        
        running = process_command(command)
        
        if running:
            time.sleep(0.3)

def main():
    """Main game function"""
    clear_screen()
    display_header()
    get_player_name()
    intro_story()
    
    print("\nType 'help' at any time for commands.\n")
    time.sleep(1)
    
    main_game_loop()
    
    print("\nThank you for playing!")

if __name__ == "__main__":
    main()
