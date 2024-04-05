from learning import get_policy_direction

q_table = {
    (0, 0): {"left": 1.002, "right": -2.1, "up": 1.001, "down": 0.0},
    (0, 1): {"left": -1000000.0, "right": 0.0, "up": 1000000.0, "down": 20.0},
    (1, 0): {"left": 2.0, "right": 3.0, "up": 4.0, "down": 5.0},
    (1, 1): {"left": -3.15, "right": -4.0, "up": -3.14, "down": -20.0},
    (2, 0): {"left": 1.0, "right": 0.0, "up": 1.0, "down": 0.0},
    (2, 1): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
}

agent_pos = (0, 0)
assert "left" == get_policy_direction(agent_pos, q_table)

agent_pos = (0, 1)
assert "up" == get_policy_direction(agent_pos, q_table)

agent_pos = (1, 0)
assert "down" == get_policy_direction(agent_pos, q_table)

agent_pos = (1, 1)
assert "up" == get_policy_direction(agent_pos, q_table)

agent_pos = (2, 0)
assert get_policy_direction(agent_pos, q_table) in ["left", "up"]

agent_pos = (2, 1)
assert get_policy_direction(agent_pos, q_table) in ["left", "up", "right", "down"]

print("All test passed!")

