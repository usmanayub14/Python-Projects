import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()
class Snake:
    def __init__(self):
        self.snake_segments = [(100, 100), (80, 100), (60, 100)]
        self.direction = 'RIGHT'

    def move(self):
        head_x, head_y = self.snake_segments[0]

        if self.direction == 'RIGHT':
            new_segment = (head_x + CELL_SIZE, head_y)
        elif self.direction == 'LEFT':
            new_segment = (head_x - CELL_SIZE, head_y)
        elif self.direction == 'UP':
            new_segment = (head_x, head_y - CELL_SIZE)
        elif self.direction == 'DOWN':
            new_segment = (head_x, head_y + CELL_SIZE)

        self.snake_segments = [new_segment] + self.snake_segments[:-1]

    def change_direction(self, direction):
        if direction == 'RIGHT' and self.direction != 'LEFT':
            self.direction = 'RIGHT'
        elif direction == 'LEFT' and self.direction != 'RIGHT':
            self.direction = 'LEFT'
        elif direction == 'UP' and self.direction != 'DOWN':
            self.direction = 'UP'
        elif direction == 'DOWN' and self.direction != 'UP':
            self.direction = 'DOWN'

    def grow(self):
        tail_x, tail_y = self.snake_segments[-1]
        self.snake_segments.append((tail_x, tail_y))

    def get_head_position(self):
        return self.snake_segments[0]

    def hit_wall(self):
        head_x, head_y = self.get_head_position()
        return head_x >= SCREEN_WIDTH or head_x < 0 or head_y >= SCREEN_HEIGHT or head_y < 0

    def hit_self(self):
        return any(segment == self.get_head_position() for segment in self.snake_segments[1:])
class Food:
    def __init__(self):
        self.position = (random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                         random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

    def randomize_position(self):
        self.position = (random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                         random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE)

    def get_position(self):
        return self.position
def main():
    snake = Snake()
    food = Food()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')
                elif event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')

        snake.move()

        if snake.hit_wall() or snake.hit_self():
            pygame.quit()
            quit()

        if snake.get_head_position() == food.get_position():
            snake.grow()
            food.randomize_position()

        screen.fill(BLACK)

        for segment in snake.snake_segments:
            pygame.draw.rect(screen, WHITE, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(screen, RED, (food.get_position()[0], food.get_position()[1], CELL_SIZE, CELL_SIZE))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == '__main__':
    main()
