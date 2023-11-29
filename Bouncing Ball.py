import pygame
import sys
import math
import random

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncy Ball ")

ball_radius = 1
ball_speed_y = 10
ball_speed_x = -10
ball_color = (255, 255, 255)

ball_x = 300
ball_y = 100

speed_increment_factor = 1

game_running = False
show_info_message = True

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_running = not game_running
                show_info_message = False

    screen.fill((0, 0, 0))

    if show_info_message:
        font = pygame.font.Font(None, 36)
        info_text = font.render("Press SPACE to start", True, (255, 255, 255))
        screen.blit(info_text, (width // 2 - info_text.get_width() // 2, height // 2 - info_text.get_height() // 2))
    else:
        if game_running:
            ball_y += ball_speed_y
            ball_x += ball_speed_x

            if ball_y - ball_radius < 0 or ball_y + ball_radius > height:
                ball_speed_y = -ball_speed_y

            if ball_x - ball_radius < 0 or ball_x + ball_radius > width:
                ball_speed_x = -ball_speed_x

            ball_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            if abs(ball_speed_x) < 1:
                ball_speed_x = 5

            if abs(ball_speed_y) < 1:
                ball_speed_y = 5

            yellow = (255, 255, 0)
            circle_center = (width // 2, height // 2)
            circle_radius = 300
            circle_thickness = 5
            pygame.draw.circle(screen, yellow, circle_center, circle_radius, circle_thickness)

            pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

            distance = math.sqrt((ball_x - circle_center[0]) ** 2 + (ball_y - circle_center[1]) ** 2)
            if distance + ball_radius > circle_radius - circle_thickness:
                angle = math.atan2(ball_y - circle_center[1], ball_x - circle_center[0])
                new_angle = math.atan2(-ball_speed_y, ball_speed_x)
                angle_after_collision = 2 * angle - new_angle
                ball_speed_x = ball_speed_y * math.cos(angle_after_collision)
                ball_speed_y = ball_speed_y * math.sin(angle_after_collision)

                ball_x = circle_center[0] + (circle_radius - circle_thickness - ball_radius) * math.cos(angle)
                ball_y = circle_center[1] + (circle_radius - circle_thickness - ball_radius) * math.sin(angle)

                ball_speed_x += speed_increment_factor
                ball_speed_y += speed_increment_factor

                ball_radius += 1

            if ball_radius == 300:
                game_running = False
        else:
            # Oyun durduğunda son çizilen görüntüyü göster
            yellow = (255, 255, 0)
            circle_center = (width // 2, height // 2)
            circle_radius = 300
            circle_thickness = 5
            pygame.draw.circle(screen, yellow, circle_center, circle_radius, circle_thickness)

            pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)

    pygame.display.flip()

    clock.tick(60)
