from maze import is_wall, is_goal 

maze = [[1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 1, 2],
        [0, 1, 2, 0, 0],
        [0, 1, 0, 1, 1]]

assert is_wall(maze, (0, 0)) 
assert is_wall(maze, (3, 2)) 
assert not is_wall(maze, (1, 2)) 
assert not is_wall(maze, (2, 3)) 

assert is_goal(maze, (2, 3)) 
assert is_goal(maze, (4, 2)) 
assert not is_goal(maze, (1, 2)) 
assert not is_goal(maze, (3, 4)) 

print("All test passed!")
