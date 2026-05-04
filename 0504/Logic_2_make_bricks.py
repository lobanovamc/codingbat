# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

# make_bricks(3, 1, 8) → True
# make_bricks(3, 1, 9) → False
# make_bricks(3, 2, 10) → True

# def calc_not_covered_size(brick_count, brick_size, row_size):
#     count = row_size / brick_size # number of brick we ideally need to cover as much as possible in this row
#     total_count = min(count, brick_count) # how much bricks we actually have or need

#     return row_size - total_count * brick_size

# def make_bricks(small, big, goal):
#     not_covered = calc_not_covered_size(big, 5, goal)

#     return 0 == calc_not_covered_size(small, 1 , not_covered)


def make_bricks(small, big, goal):
  
  # (1) if we have enough bricks to cover using big brikcs
  if goal / 5 <= big:
    return goal % 5 <= small
  
  # (2) if we don't have enough bricks to cover using big brikcs
  if (goal - (big * 5)) <= small:
    return True
    
  return False 
