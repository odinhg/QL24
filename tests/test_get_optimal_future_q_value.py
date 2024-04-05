from learning import get_optimal_future_q_value

maze = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

q_table = {
    (0, 0): {"left": -1.0, "right": 1.0, "up": 2.0, "down": 0.0},
    (0, 1): {"left": 4.1, "right": 4.0, "up": 1.0, "down": -12.0},
    (1, 0): {"left": 2.0, "right": 2.0, "up": 1.0, "down": -4.0},
    (1, 1): {"left": 3.0, "right": 4.0, "up": 4.0, "down": 4.0},
    (2, 0): {"left": -5.0, "right": -4.0, "up": -3.0, "down": -2.0},
    (2, 1): {"left": 1.0, "right": 0.5, "up": 1.0, "down": 0.0},
}

agent_pos = (2, 1)
direction = "left"
assert 4.0 == get_optimal_future_q_value(q_table, agent_pos, direction, maze)

agent_pos = (2, 1)
direction = "up"
assert -2.0 == get_optimal_future_q_value(q_table, agent_pos, direction, maze)

agent_pos = (1, 1)
direction = "left"
assert 4.1 == get_optimal_future_q_value(q_table, agent_pos, direction, maze)

agent_pos = (1, 1)
direction = "up"
assert 2.0 == get_optimal_future_q_value(q_table, agent_pos, direction, maze)

agent_pos = (1, 1)
direction = "right"
assert 1.0 == get_optimal_future_q_value(q_table, agent_pos, direction, maze)

agent_pos = (0, 1)
direction = "up"
assert 2.0 == get_optimal_future_q_value(q_table, agent_pos, direction, maze)

print("All test passed!")

