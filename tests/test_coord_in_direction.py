from maze import coord_in_direction

assert (2, 2) == coord_in_direction((2, 3), "up")
assert (6, 0) == coord_in_direction((5, 0), "right")
assert (-1, 21) == coord_in_direction((0, 21), "left")
assert (32, 21) == coord_in_direction((32, 20), "down")

print("All test passed!")
