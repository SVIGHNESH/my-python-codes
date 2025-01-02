import pygame
import random
import math

# Initialize pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Ball with Bouncy Basket and Spark Effects")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)  # Color for sparks

# Basket properties
basket_width = 100  
basket_height = 20
basket_y = screen_height - basket_height - 10
basket_bounce_offset = 0  # Used for the bouncy effect
basket_bounce_direction = 0  # 0 means not bouncing, -1 means moving up, 1 means moving down

# Ball properties
ball_radius = 15
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = random.randint(ball_radius, screen_height // 2)
ball_velocity_x = 4  # Initial horizontal speed
ball_velocity_y = 4  # Initial vertical speed

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Speed increase threshold
speed_increase_threshold = 5  # Increase speed after every 5 touches
speed_increase_amount = 1  # How much to increase the speed by

# Spark effects
sparks = []

# Game over flag
game_over = False

# Function to create sparks
def create_sparks(x, y, num_sparks=10):
    for _ in range(num_sparks):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 5)
        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed
        lifespan = random.randint(20, 40)
        sparks.append({"x": x, "y": y, "vx": vx, "vy": vy, "life": lifespan})

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check if game is over
    if game_over:
        # Display "Game Over" message
        game_over_text = font.render(f"Game Over! Final Score: {score}", True, BLACK)
        screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 20))

        # Animate the ball falling out of the screen
        if ball_y < screen_height + ball_radius:  # Ball keeps falling
            ball_y += 5  # Slow falling speed

        # Draw the ball while falling
        pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

        pygame.display.flip()
        pygame.time.wait(3000)  # Wait 3 seconds before closing
        running = False  # End the game after the animation
        continue

    # Move the basket using the mouse
    mouse_x, _ = pygame.mouse.get_pos()  # Get the mouse position (only x-axis)
    basket_x = mouse_x - basket_width // 2  # Center the basket under the mouse

    # Bounce the basket if it's in the bouncing state
    if basket_bounce_direction == -1:  # Moving up
        basket_bounce_offset -= 2
        if basket_bounce_offset <= -10:  # Max height reached
            basket_bounce_direction = 1  # Start moving down
    elif basket_bounce_direction == 1:  # Moving down
        basket_bounce_offset += 2
        if basket_bounce_offset >= 0:  # Back to original position
            basket_bounce_direction = 0  # Stop bouncing

    # Move the ball (bouncing mechanics)
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    # Check for collisions with the screen edges (bounce)
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_velocity_x = -ball_velocity_x  # Reverse horizontal direction
        create_sparks(ball_x, ball_y)  # Create sparks on bounce
    if ball_y - ball_radius <= 0:
        ball_velocity_y = -ball_velocity_y  # Reverse vertical direction
        create_sparks(ball_x, ball_y)  # Create sparks on bounce

    # Check for collision with the basket (only when the ball is falling)
    if ball_velocity_y > 0 and ball_y + ball_radius >= basket_y and basket_x < ball_x < basket_x + basket_width:
        score += 1
        ball_velocity_y = -ball_velocity_y  # Reverse vertical direction after hitting the basket
        basket_bounce_direction = -1  # Start bouncing the basket up
        create_sparks(ball_x, ball_y)  # Create sparks on bounce

        # Increase speed if score crosses the threshold (every 5 touches)
        if score > 0 and score % speed_increase_threshold == 0:
            if ball_velocity_x > 0:
                ball_velocity_x += speed_increase_amount  # Increase horizontal speed
            else:
                ball_velocity_x -= speed_increase_amount

            if ball_velocity_y > 0:
                ball_velocity_y += speed_increase_amount  # Increase vertical speed
            else:
                ball_velocity_y -= speed_increase_amount

    # Check if the ball touches the lower side (game over condition)
    if ball_y + ball_radius >= screen_height:
        game_over = True

    # Draw the basket and the ball with the bounce offset applied
    pygame.draw.rect(screen, BLACK, (basket_x, basket_y + basket_bounce_offset, basket_width, basket_height))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Update and draw sparks
    for spark in sparks[:]:
        spark["x"] += spark["vx"]
        spark["y"] += spark["vy"]
        spark["life"] -= 1

        # Draw the spark
        pygame.draw.circle(screen, YELLOW, (int(spark["x"]), int(spark["y"])), 3)

        # Remove dead sparks
        if spark["life"] <= 0:
            sparks.remove(spark)

    # Display score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit pygame
pygame.quit()