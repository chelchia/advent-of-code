import math

puzzle = 361527

def gridlength(x):
	sq = math.floor(math.sqrt(puzzle))
	if sq % 2 == 0:
		sq = sq + 1
	else:
		sq = sq + 2
	return sq

# finds coords of x, provided x is on the outer ring
# taking top left corner as (1, 1)
def coords(x, gridlen):
	gridsize = gridlen * gridlen
	diff = gridsize - x
	loc = math.ceil(diff / (gridlen - 1))
	position = diff % (gridlen - 1)
	if loc == 1:
		# x is on the lowest row
		coord = [gridlen, gridlen - position]
	if loc == 2:
		# x is on the leftmost col
		coord = [gridlen - position, 1]
	if loc == 3:
		# x is on the top row
		coord = [1, position + 1]
	if loc == 4:
		# x is on the rightmost col
		coord = [position + 1, gridlen]
	return coord

def center(gridlen):
	midpt = math.ceil(gridlen / 2)
	return [midpt, midpt]

def man_dist(pt1, pt2):
	x1 = pt1[0]
	y1 = pt1[1]
	x2 = pt2[0]
	y2 = pt2[1]
	return math.fabs(x1 - x2) + math.fabs(y1 - y2)

len_of_grid = gridlength(puzzle)
coord_of_puzzle = coords(puzzle, len_of_grid)
coord_of_1 = center(len_of_grid)
steps_needed = man_dist(coord_of_puzzle, coord_of_1)

print("steps needed ", steps_needed)