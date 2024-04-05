from learning import reward_function

maze = [[1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0],
        [0, 1, 2, 0, 0],
        [0, 1, 0, 1, 1]]

agent_pos = (1, 2)
direction = "left"
assert -0.1 == reward_function(agent_pos, direction, maze)

agent_pos = (4, 2)
direction = "up"
assert -1.0 == reward_function(agent_pos, direction, maze)

agent_pos = (2, 4)
direction = "up"
assert 1.0 == reward_function(agent_pos, direction, maze)

agent_pos = (0, 3)
direction = "right"
assert -1.0 == reward_function(agent_pos, direction, maze)

agent_pos = (3, 3)
direction = "down"
assert -1.0 == reward_function(agent_pos, direction, maze)

agent_pos = (3, 3)
direction = "right"
assert -0.1 == reward_function(agent_pos, direction, maze)

print("All test passed!")

