from maze import move_agent

maze = [[1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 1, 2],
        [0, 1, 2, 0, 0],
        [0, 1, 0, 1, 1]]

agent_pos = (1, 2)
direction = "left"
assert (0, 2) == move_agent(agent_pos, direction, maze)
direction = "up"
assert (1, 1) == move_agent(agent_pos, direction, maze)
direction = "down"
assert (1, 2) == move_agent(agent_pos, direction, maze)
direction = "right"
assert (1, 2) == move_agent(agent_pos, direction, maze)

agent_pos = (3, 3)
direction = "left"
assert (2, 3) == move_agent(agent_pos, direction, maze)
direction = "up"
assert (3, 3) == move_agent(agent_pos, direction, maze)
direction = "down"
assert (3, 3) == move_agent(agent_pos, direction, maze)
direction = "right"
assert (4, 3) == move_agent(agent_pos, direction, maze)

print("All test passed!")
