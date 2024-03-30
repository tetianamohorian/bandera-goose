# Bandera goose
### 1. Game description

The player controls a bandera goose that moves up, down, left and right. The player must avoid collisions with rockets and catch parachutes with bonuses. If the player collides with a rocket, the game is over.  If the player catches a bonus, he gets + point.

### 2. How to translate and run the game ?


- Run and compile the program using the command
    
    ````c
    python main.py
    ````

### 3. Instructions on how to play the game

- The game starts with your goose character in the center of the screen.

- The background continuously scrolls from right to left, creating the illusion of movement.

- Enemies will appear at random intervals on the right side of the screen and fly towards the left.

- Bonuses will also appear at random intervals from the top of the screen and move downwards.

- Your goal is to navigate the goose character using the arrow keys to avoid colliding with any enemies.

- Your score is displayed in the top right corner of the screen.

- If your goose touches an enemy, the game ends.

- Collect the bonuses by flying your goose through them. Each collected bonus increases your score.

- To quit the game, click on the cross.

### 4. How is the game programmed?

- The most important game features and their functions

    * The create_enemy() function. Creates a new enemy.
        - Determines the size of the enemy.
        - Loads an image of the enemy with transparency.
        - Resizes the enemy image.
        - Creates a rectangle to define the enemy's position.
        - Sets the initial velocity of the enemy.
        - Returns a list with the enemy's image, position and speed.

    * Create_bonus() function: Creates a new bonus.
        - Determines the size of the bonus.
        - Loads a bonus image with transparency.
        - Resizes the bonus image.
        - Creates a rectangle to define the position of the bonus.
        - Sets the initial velocity of the bonus.
        - Returns a list with the image, position and speed of the bonus.

- Important constructions in this game are:
    * Level Initialization: The game to have continuous enemy and bonus creation. Enemy speed (enemy_move) and bonus speed (bonus_move) are configurable and could be used to create easier or harder difficulties. Initial positions for enemies (enemy_rect.x set to screen width) and bonuses (bonus_rect.y set to 0) are determined in the create_enemy and create_bonus functions.
    * Game World Event Processing: The game checks for pressed arrow keys (K_DOWN, K_UP, K_LEFT, K_RIGHT) to move the player (player_rect.move). Enemies move left (enemy_move = [-16, 0]) and are removed when they go off-screen (enemy[1].right <= 0). Bonuses move down (bonus_move = [0, 8]) and are removed when they go off-screen (bonus[1].bottom >= HEIGHT). Background image scrolls left (bg_x1 -= bg_move, bg_x2 -= bg_move) and wraps around the screen when it goes off-screen. The game checks for collisions between the player and enemies (player_rect.colliderect(enemy[1])) using the colliderect method. If a collision occurs, the game ends (playing = False).
    * Displaying Game State: The draw_game function (not explicitly shown in the code, but likely exists based on the comments) is likely responsible for drawing the following elements on the screen: 
        - Background image (main_display.blit(bg, (bg_x1,0)) and main_display.blit(bg, (bg_x2,0)))
        - Enemies (main_display.blit(enemy[0], enemy[1]))
        - Bonuses (main_display.blit(bonus[0], bonus[1]))
        - Player (main_display.blit(player,player_rect))
        - Score (main_display.blit(FONT.render(str(score),True, COLOR_BLUE), (WIDTH-50, 20)))
        - This information is used to update the visuals on the screen (pygame.display.flip).

### 5. Links to source code and websites that were used in the solution

-   [Go IT Telegram](https://t.me/python_goit_bot)
   
-   [Python](https://education.yandex.ru/handbook/python)

-   [Go IT Youtube](https://www.youtube.com/@GoIT/videos)

