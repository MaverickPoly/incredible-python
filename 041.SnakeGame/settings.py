RECORD_FILENAME = "record.txt"

CELL_SIZE = 40
ROWS, COLS = 20, 20

# WINDOW
FPS = 60
TITLE = "Snake Game"
WIDTH, HEIGHT = CELL_SIZE * ROWS, CELL_SIZE * COLS

# Colors
LIGHT_GREEN = (170, 215, 81)
DARK_GREEN = (152, 198, 60)
BLUE = (70, 110, 250)
RED = (200, 40, 50)
BLACK = (20, 20, 20)
WHITE = (248, 247, 237)

# Snake configurations
SNAKE_MOVE_TIMEOUT = 150

# Fruit configurations
FRUIT_GENERATE_TIMEOUT = 3000


# Directions
LEFT =  -1, 0
RIGHT = +1, 0
UP =    0, -1
DOWN =  0, +1
