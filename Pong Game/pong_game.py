import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PADDLE_SPEED = 5
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

clock = pygame.time.Clock()
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, PADDLE_WIDTH, PADDLE_HEIGHT))

    def move_up(self):
        self.y -= PADDLE_SPEED
        if self.y < 0:
            self.y = 0

    def move_down(self):
        self.y += PADDLE_SPEED
        if self.y > SCREEN_HEIGHT - PADDLE_HEIGHT:
            self.y = SCREEN_HEIGHT - PADDLE_HEIGHT
class Ball:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
        self.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
        self.speed_x = random.choice([-BALL_SPEED_X, BALL_SPEED_X])
        self.speed_y = random.choice([-BALL_SPEED_Y, BALL_SPEED_Y])

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, BALL_SIZE, BALL_SIZE))

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bounce(self):
        self.speed_y = -self.speed_y

    def hit_paddle(self, paddle):
        if self.x < paddle.x + PADDLE_WIDTH and self.x + BALL_SIZE > paddle.x:
            if self.y < paddle.y + PADDLE_HEIGHT and self.y + BALL_SIZE > paddle.y:
                return True
        return False

    def hit_wall(self):
        return self.y <= 0 or self.y + BALL_SIZE >= SCREEN_HEIGHT

    def off_screen(self):
        return self.x + BALL_SIZE < 0 or self.x > SCREEN_WIDTH

def main():
    player1 = Paddle(20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    player2 = Paddle(SCREEN_WIDTH - 30, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player1.move_up()
        if keys[pygame.K_s]:
            player1.move_down()
        if keys[pygame.K_UP]:
            player2.move_up()
        if keys[pygame.K_DOWN]:
            player2.move_down()

        ball.move()

        if ball.hit_paddle(player1) or ball.hit_paddle(player2):
            ball.speed_x = -ball.speed_x
            ball.move()

        if ball.hit_wall():
            ball.bounce()
            ball.move()

        if ball.off_screen():
            ball.reset()

        screen.fill(BLACK)
        player1.draw()
        player2.draw()
        ball.draw()

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    main()
