#Before execution of file please provide the path of car.png on line no 32.
import pygame
import math
import sys

WIDTH, HEIGHT = 900, 600
ROAD_WIDTH = 400
ROAD_EDGE_WIDTH = 10
GRASS_COLOR = (9,149,78)
ROAD_COLOR = (60, 60, 60)
EDGE_COLOR = (255, 255, 255)
FPS = 90
SEGMENT_HEIGHT = 4

# Pygame init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racing Track using 2D Transformations")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)


pause_button = pygame.Rect(10, 10, 80, 30)
play_button = pygame.Rect(100, 10, 80, 30)
quit_button = pygame.Rect(WIDTH - 90, 10, 80, 30)

paused = False
running = True
frame_count = 0

#image
car_img = pygame.image.load('copy path for car.png').convert_alpha()
car_img = pygame.transform.scale(car_img, (60, 120))

#path
STRAIGHT_SEGMENT = 150
WAVE_SEGMENT = 700
TOTAL_SEGMENT = STRAIGHT_SEGMENT * 2 + WAVE_SEGMENT

path = []
# 2D TRANSFORMATIONS 
#straight path
for _ in range(STRAIGHT_SEGMENT):
    path.append(WIDTH // 2)

# Curvy middle
for i in range(WAVE_SEGMENT):
    angle = (i / WAVE_SEGMENT) * 2 * math.pi
    offset = math.sin(angle * 2) * 150
    x = WIDTH // 2 + offset
    path.append(int(x))

# End straight
for _ in range(STRAIGHT_SEGMENT):
    path.append(WIDTH // 2)

# Loop path
path = path + path[:HEIGHT // SEGMENT_HEIGHT]

# Car y-position
MARKER_Y = HEIGHT // 2

def draw_button(rect, text, mouse_pos):
    color = (150, 150, 150) if rect.collidepoint(mouse_pos) else (200, 200, 200)
    pygame.draw.rect(screen, color, rect)
    text_surf = font.render(text, True, (0, 0, 0))
    text_rect = text_surf.get_rect(center=rect.center)
    screen.blit(text_surf, text_rect)

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pause_button.collidepoint(event.pos):
                paused = True
            elif play_button.collidepoint(event.pos):
                paused = False
            elif quit_button.collidepoint(event.pos):
                running = False

    screen.fill(GRASS_COLOR)

    # Draw road
    for i in range(HEIGHT // SEGMENT_HEIGHT):
        path_index = (frame_count + i) % len(path)
        center_x = path[path_index]
        y = HEIGHT - i * SEGMENT_HEIGHT

        left_edge = center_x - ROAD_WIDTH // 2
        right_edge = center_x + ROAD_WIDTH // 2

        # Road and Edges
        pygame.draw.rect(screen, ROAD_COLOR, (left_edge, y, ROAD_WIDTH, SEGMENT_HEIGHT))
        pygame.draw.rect(screen, EDGE_COLOR, (left_edge, y, ROAD_EDGE_WIDTH, SEGMENT_HEIGHT))
        pygame.draw.rect(screen, EDGE_COLOR, (right_edge - ROAD_EDGE_WIDTH, y, ROAD_EDGE_WIDTH, SEGMENT_HEIGHT))

        # Dotted center line
        if ((i + frame_count) % 20) < SEGMENT_HEIGHT:
            dot_width = 10
            pygame.draw.rect(screen, EDGE_COLOR, (center_x - dot_width // 2, y, dot_width, SEGMENT_HEIGHT))

    

    # Draw car
    car_center_x = path[(frame_count + (HEIGHT // SEGMENT_HEIGHT) // 2) % len(path)]
    car_rect = car_img.get_rect(center=(car_center_x, MARKER_Y))
    screen.blit(car_img, car_rect)

    # Buttons
    draw_button(pause_button, 'Pause', mouse_pos)
    draw_button(play_button, 'Play', mouse_pos)
    draw_button(quit_button, 'Quit', mouse_pos)

    pygame.display.flip()
    if not paused:
        frame_count = (frame_count + 1) % len(path)
    clock.tick(FPS)

pygame.quit()
sys.exit()
