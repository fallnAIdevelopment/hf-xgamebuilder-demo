#!/usr/bin/env python3
"""
Game Reiteration Tool
Use this script to edit and improve your game
"""

import json
import os
import sys

def load_game_config():
    with open('game_config.json', 'r') as f:
        return json.load(f)

def save_game_config(config):
    with open('game_config.json', 'w') as f:
        json.dump(config, f, indent=2)

def edit_game_mechanics():
    print("\n=== Edit Game Mechanics ===")
    config = load_game_config()
    
    print("Current mechanics:", config.get('mechanics', {}))
    print("\nEnter new mechanic (key=value) or 'done' to finish:")
    
    while True:
        user_input = input("> ").strip()
        if user_input.lower() == 'done':
            break
        
        if '=' in user_input:
            key, value = user_input.split('=', 1)
            if 'mechanics' not in config:
                config['mechanics'] = {}
            config['mechanics'][key.strip()] = value.strip()
            print(f"Added: {key} = {value}")
    
    save_game_config(config)
    print("Game mechanics updated!")

def edit_visuals():
    print("\n=== Edit Visual Settings ===")
    config = load_game_config()
    
    print("1. Change color scheme")
    print("2. Adjust lighting")
    print("3. Modify effects")
    print("4. Back")
    
    choice = input("Select option: ").strip()
    
    if choice == '1':
        primary = input("Primary color (hex): ").strip()
        secondary = input("Secondary color (hex): ").strip()
        if 'visuals' not in config:
            config['visuals'] = {}
        config['visuals']['colors'] = {
            'primary': primary,
            'secondary': secondary
        }
    
    save_game_config(config)
    print("Visual settings updated!")

def rebuild_game():
    print("\n=== Rebuilding Game ===")
    print("Running build process...")
    os.system('npm run build')
    print("Build complete!")

def main():
    print("""
    ╔═══════════════════════════════════════╗
    ║   Game Reiteration Tool               ║
    ║   Edit and improve your game          ║
    ╚═══════════════════════════════════════╝
    """)
    
    while True:
        print("\n=== Main Menu ===")
        print("1. Edit game mechanics")
        print("2. Edit visual settings")
        print("3. Rebuild game")
        print("4. Exit")
        
        choice = input("\nSelect option: ").strip()
        
        if choice == '1':
            edit_game_mechanics()
        elif choice == '2':
            edit_visuals()
        elif choice == '3':
            rebuild_game()
        elif choice == '4':
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
