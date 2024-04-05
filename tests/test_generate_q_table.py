from learning import generate_q_table

# Test 1
expected = {(0, 0): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0}}
assert expected == generate_q_table(1, 1), "Test 1 failed!"

# Test 2
expected = {
    (0, 0): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (0, 1): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (1, 0): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (1, 1): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (2, 0): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (2, 1): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
}
assert expected == generate_q_table(2, 3), "Test 2 failed!"

# Test 3
expected = {
    (0, 0): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (0, 1): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (0, 2): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (0, 3): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (1, 0): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (1, 1): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (1, 2): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (1, 3): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (2, 0): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (2, 1): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (2, 2): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (2, 3): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (3, 0): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (3, 1): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (3, 2): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (3, 3): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (4, 0): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (4, 1): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (4, 2): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
    (4, 3): {"left": 0.0, "right": 0.0, "up": 0.0, "down": 0.0},
}
assert expected == generate_q_table(4, 5), "Test 3 failed!"

print("All test passed!")
