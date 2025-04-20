import random

class Game2048:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]
        self.spawn()
        self.spawn()

    def spawn(self):
        empty = [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] == 0]
        if empty:
            r, c = random.choice(empty)
            self.grid[r][c] = 2 if random.random() < 0.9 else 4

    def move_left(self):
        moved = False
        new_grid = []
        for row in self.grid:
            tight = [i for i in row if i != 0]
            merged = []
            i = 0
            while i < len(tight):
                if i + 1 < len(tight) and tight[i] == tight[i+1]:
                    merged.append(tight[i] * 2)
                    i += 2
                    moved = True
                else:
                    merged.append(tight[i])
                    i += 1
            merged += [0] * (self.size - len(merged))
            if merged != row:
                moved = True
            new_grid.append(merged)
        self.grid = new_grid
        return moved

    def move(self, direction):
        rotated = False
        if direction == 'up':
            self.grid = list(map(list, zip(*self.grid[::-1])))
            rotated = True
        elif direction == 'down':
            self.grid = list(map(list, zip(*self.grid)))[::-1]
            rotated = True
        elif direction == 'right':
            self.grid = [row[::-1] for row in self.grid]

        moved = self.move_left()

        if direction == 'up' and rotated:
            self.grid = list(map(list, zip(*self.grid)))[::-1]
        elif direction == 'down' and rotated:
            self.grid = list(map(list, zip(*self.grid[::-1])))
        elif direction == 'right':
            self.grid = [row[::-1] for row in self.grid]

        if moved:
            self.spawn()
        return moved

    def get_grid(self):
        return self.grid
