#!/usr/bin/env python3
from playwright.sync_api import sync_playwright
import time

def test_incha_porco():
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)
        
        # Create two player contexts
        print("Creating two players to test multiplayer...")
        
        # Player 1
        page1 = browser.new_page()
        page1.goto('http://localhost:8080')
        page1.wait_for_load_state('networkidle')
        
        print("Player 1: Taking screenshot of main menu...")
        page1.screenshot(path='/tmp/incha_porco_menu.png', full_page=True)
        
        # Player 1 creates game
        page1.fill('#playerName', 'Player 1')
        page1.click('button:has-text("Create New Game")')
        
        time.sleep(2)
        page1.wait_for_load_state('networkidle')
        
        print("Player 1: Game created, taking screenshot...")
        page1.screenshot(path='/tmp/incha_porco_waiting_p1.png', full_page=True)
        
        # Get game ID
        game_id_element = page1.locator('#displayGameId')
        game_id = game_id_element.text_content()
        print(f"Game ID: {game_id}")
        
        # Player 2 joins
        page2 = browser.new_page()
        page2.goto('http://localhost:8080')
        page2.wait_for_load_state('networkidle')
        
        page2.fill('#playerName', 'Player 2')
        page2.fill('#gameId', game_id)
        page2.click('button:has-text("Join Game")')
        
        time.sleep(2)
        page2.wait_for_load_state('networkidle')
        
        print("Player 2: Joined game, taking screenshot...")
        page2.screenshot(path='/tmp/incha_porco_waiting_p2.png', full_page=True)
        
        # Player 1 starts the game
        page1.click('#startBtn')
        
        time.sleep(3)
        page1.wait_for_load_state('networkidle')
        
        print("Game started! Taking screenshots...")
        page1.screenshot(path='/tmp/incha_porco_game_p1.png', full_page=True)
        page2.screenshot(path='/tmp/incha_porco_game_p2.png', full_page=True)
        
        # Test some card flips
        print("Testing card flips...")
        
        # Player 1 flips cards
        cards = page1.locator('.card').all()
        if len(cards) > 0:
            print(f"Found {len(cards)} cards")
            cards[0].click()
            time.sleep(1)
            cards[1].click()
            time.sleep(1)
            cards[2].click()
            time.sleep(2)
            
            print("After flips, taking screenshots...")
            page1.screenshot(path='/tmp/incha_porco_after_flip_p1.png', full_page=True)
            page2.screenshot(path='/tmp/incha_porco_after_flip_p2.png', full_page=True)
        
        print("\nTest completed successfully!")
        print("\nScreenshots saved:")
        print("  - /tmp/incha_porco_menu.png")
        print("  - /tmp/incha_porco_waiting_p1.png")
        print("  - /tmp/incha_porco_waiting_p2.png")
        print("  - /tmp/incha_porco_game_p1.png")
        print("  - /tmp/incha_porco_game_p2.png")
        print("  - /tmp/incha_porco_after_flip_p1.png")
        print("  - /tmp/incha_porco_after_flip_p2.png")
        
        browser.close()

if __name__ == '__main__':
    test_incha_porco()
