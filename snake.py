import random, sys

#  --------------->
# 

class Snake:
    def __init__(self):
        self.body = [(0, 0), (1, 0)]
        self.color = "#a1bff0"
        self.direction = "right"

    def print(self):
        for x, y in self.body:
            print(f'paint {x} {y} {self.color}')

    def change_direction(self, direction):
        if direction in ['up', 'down', 'right', 'left']:
            if self.direction in ["up", "down"] and direction in ['right', 'left']:
                self.direction = direction

            elif self.direction in ['right', 'left'] and direction in ['up', 'down']:
                self.direction = direction

    
    def move(self, food):
        head = self.body[-1]
        new_head = head # (1, 0)

        if self.direction == "right":
            new_head = (head[0]+1, head[1])

        elif self.direction == "left":
            new_head = (head[0]-1, head[1])

        elif self.direction == "up":
            new_head = (head[0], head[1]+1)

        elif self.direction == "down":
            new_head = (head[0], head[1]-1)

        self.body.append(new_head)

        if food.position == new_head:
            return True
        elif food != new_head:
            x,y = self.body.pop(0)
            print(f'unpaint {x} {y}')



class Food:
    def __init__(self, height, width):
        x = random.randint(0, width)
        y = random.randint(0, height)
        self.position = (x,y)
        self.color = "#a3251c"

    def print(self):
        x, y = self.position
        print(f'paint {x} {y} {self.color}')

height, width = 30,30
snake = Snake()
food = Food(height, width)
print(f'init {height} {width}')
print('---')

while True:
    command = input()

    if command == 'q':
        print('stop 0')
        print('---')
        break

    direction = command
    snake.change_direction(direction)
    if snake.move(food):
        food = Food(height, width)
    snake.print()
    food.print()
    print('---')

    sys.stdout.flush()
