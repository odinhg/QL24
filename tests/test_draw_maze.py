from uib_inf100_graphics.simple import canvas, display
from maze import draw_maze

maze = [[1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 2, 0, 0],
        [0, 1, 0, 1, 1]]

agent_pos = (1, 2)

draw_maze(canvas, maze, 20, 20, 220, 220, agent_pos)

display(canvas)
