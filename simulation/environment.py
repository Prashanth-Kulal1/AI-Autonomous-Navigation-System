import pygame
import random

CELL_SIZE = 30

class Environment:
    def __init__(self, rows, cols):
        pygame.init()
        self.rows = rows
        self.cols = cols
        self.width = cols * CELL_SIZE
        self.height = rows * CELL_SIZE
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.grid = self.generate_grid()

    def generate_grid(self):
        grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                if random.random() < 0.2:
                    row.append(1)  # obstacle
                else:
                    row.append(0)
            grid.append(row)
        return grid

    def get_grid(self):
        return self.grid

    def draw(self, agent, path):
        self.screen.fill((255, 255, 255))

        for i in range(self.rows):
            for j in range(self.cols):
                rect = pygame.Rect(j*CELL_SIZE, i*CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if self.grid[i][j] == 1:
                    pygame.draw.rect(self.screen, (0, 0, 0), rect)
                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

        for node in path:
            pygame.draw.rect(self.screen, (0, 255, 0),
                             (node[1]*CELL_SIZE, node[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(self.screen, (255, 0, 0),
                         (agent.pos[1]*CELL_SIZE, agent.pos[0]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.update()

    def run_simulation(self, agent, path):
        clock = pygame.time.Clock()

        for step in path:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            agent.move(step)
            self.draw(agent, path)
            clock.tick(5)

        pygame.quit()