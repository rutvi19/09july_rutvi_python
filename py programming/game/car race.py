import pygame
import random
import sys

# ---------- Configuration ----------
WIDTH, HEIGHT = 480, 700
FPS = 60

LANE_COUNT = 3
LANE_PADDING = 20
ROAD_MARGIN = 40

PLAYER_WIDTH, PLAYER_HEIGHT = 40, 70
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 40, 70

BASE_OBSTACLE_SPEED = 6
OBSTACLE_SPAWN_RATE = 800  # milliseconds

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
ROAD_COLOR = (30, 30, 30)
GREEN = (20, 130, 20)
RED = (200, 30, 30)
YELLOW = (240, 200, 10)
BLUE = (0, 120, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Race")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 64)

# ---------- Helper functions ----------
def draw_text(surface, text, pos, font, color=WHITE, center=False):
    img = font.render(text, True, color)
    rect = img.get_rect()
    if center:
        rect.center = pos
    else:
        rect.topleft = pos
    surface.blit(img, rect)

def lanes_positions():
    """Return the x-center positions for each lane."""
    road_w = WIDTH - 2 * ROAD_MARGIN
    lane_w = road_w / LANE_COUNT
    centers = []
    for i in range(LANE_COUNT):
        cx = ROAD_MARGIN + lane_w * i + lane_w / 2
        centers.append(int(cx))
    return centers

LANE_X = lanes_positions()

# ---------- Game objects ----------
class Player:
    def __init__(self):
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.x = WIDTH // 2
        self.y = HEIGHT - self.height - 30
        self.speed_x = 7
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.color = BLUE

    def update(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
            self.x -= self.speed_x
        if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
            self.x += self.speed_x
        # constrain to road
        min_x = ROAD_MARGIN + 10
        max_x = WIDTH - ROAD_MARGIN - self.width - 10
        self.x = max(min_x, min(max_x, self.x))
        self.rect.topleft = (int(self.x), int(self.y))

    def draw(self, surface):
        # simple car shape: rounded-ish rectangle with a windshield
        pygame.draw.rect(surface, self.color, self.rect, border_radius=8)
        # windshield
        wind = pygame.Rect(self.rect.x + 8, self.rect.y + 10, self.width - 16, 18)
        pygame.draw.rect(surface, (180, 220, 255), wind, border_radius=6)

class Obstacle:
    def __init__(self, x, y, speed, color=RED):
        self.width = OBSTACLE_WIDTH
        self.height = OBSTACLE_HEIGHT
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def update(self, dt):
        # move down
        self.y += self.speed * dt
        self.rect.topleft = (int(self.x), int(self.y))

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, border_radius=6)
        # small highlight
        highlight = pygame.Rect(self.rect.x + 6, self.rect.y + 10, 8, 10)
        pygame.draw.rect(surface, (255, 255, 255), highlight)

# ---------- Main Game ----------
def game_loop():
    player = Player()
    obstacles = []
    running = True
    paused = False
    score = 0.0
    speed_multiplier = 1.0
    last_spawn = pygame.time.get_ticks()
    obstacle_speed = BASE_OBSTACLE_SPEED
    spawn_rate = OBSTACLE_SPAWN_RATE

    # Road line animation
    line_offset = 0

    while running:
        dt_ms = clock.tick(FPS)
        dt = dt_ms / 16.0  # normalize by ~16ms frame (so speeds feel similar across FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        keys = pygame.key.get_pressed()
        # speed boost while up arrow pressed
        if keys[pygame.K_UP]:
            speed_multiplier = 1.8
        else:
            speed_multiplier = 1.0

        # update player
        player.update(keys)

        # spawn obstacles
        now = pygame.time.get_ticks()
        if now - last_spawn > spawn_rate:
            last_spawn = now
            # choose lane and x pos
            lane = random.randrange(LANE_COUNT)
            lane_center = LANE_X[lane]
            x = lane_center - OBSTACLE_WIDTH // 2 + random.randint(-10, 10)
            y = -OBSTACLE_HEIGHT - random.randint(0, 150)
            # slight random variation in speed
            color = random.choice([RED, YELLOW, (200, 100, 200)])
            obstacles.append(Obstacle(x, y, obstacle_speed * random.uniform(0.9, 1.2), color))

        # update obstacles
        for ob in obstacles:
            ob.update(dt * speed_multiplier)

        # remove off-screen and increase score
        new_obs = []
        for ob in obstacles:
            if ob.y > HEIGHT + 50:
                score += 10  # dodged one
            else:
                new_obs.append(ob)
        obstacles = new_obs

        # difficulty ramping: every 10 seconds increase obstacle speed slightly and spawn more often
        time_seconds = pygame.time.get_ticks() // 1000
        obstacle_speed = BASE_OBSTACLE_SPEED + (time_seconds // 10) * 0.8
        spawn_rate = max(300, OBSTACLE_SPAWN_RATE - (time_seconds // 6) * 40)

        # collision detection
        collision = any(player.rect.colliderect(ob.rect) for ob in obstacles)
        if collision:
            game_over_screen(score)
            return  # return to allow restart from main

        # draw everything
        screen.fill(GREEN)

        # road
        pygame.draw.rect(screen, ROAD_COLOR, (ROAD_MARGIN, 0, WIDTH - 2 * ROAD_MARGIN, HEIGHT))
        # lane markers
        lane_w = (WIDTH - 2 * ROAD_MARGIN) / LANE_COUNT
        for i in range(1, LANE_COUNT):
            x = ROAD_MARGIN + int(i * lane_w)
            pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT), 4)

        # dashed center-lines (vertical)
        seg_h = 40
        gap = 20
        line_x = WIDTH // 2 - 2
        line_offset = (line_offset + int(6 * speed_multiplier)) % (seg_h + gap)
        y = -line_offset
        while y < HEIGHT:
            pygame.draw.rect(screen, WHITE, (line_x, y, 4, seg_h))
            y += seg_h + gap

        # draw obstacles and player
        for ob in obstacles:
            ob.draw(screen)
        player.draw(screen)

        # HUD
        draw_text(screen, f"Score: {int(score)}", (10, 10), font, WHITE)
        draw_text(screen, f"Speed: {int(obstacle_speed * speed_multiplier)}", (10, 40), font, WHITE)
        draw_text(screen, "Use ← → or A/D to move. ↑ for boost.", (10, HEIGHT - 30), font, WHITE)

        pygame.display.flip()

def game_over_screen(score):
    clock = pygame.time.Clock()
    waiting = True
    while waiting:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                    game_loop()
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.fill(BLACK)
        draw_text(screen, "GAME OVER", (WIDTH // 2, HEIGHT // 2 - 80), big_font, RED, center=True)
        draw_text(screen, f"Score: {int(score)}", (WIDTH // 2, HEIGHT // 2 - 10), font, WHITE, center=True)
        draw_text(screen, "Press R to restart or ESC to quit", (WIDTH // 2, HEIGHT // 2 + 40), font, WHITE, center=True)
        pygame.display.flip()

# ---------- Start ----------
if __name__ == "__main__":
    try:
        game_loop()
    except SystemExit:
        raise
    except Exception as e:
        pygame.quit()
        print("An error occurred:", e)
