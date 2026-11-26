from collections import deque


def find_char(maze, target):
	for r, row in enumerate(maze):
		for c, value in enumerate(row):
			if value == target:
				return r, c
	return None


def solve_maze(maze_lines):
	maze = [list(row) for row in maze_lines]

	start = find_char(maze, "S")
	end = find_char(maze, "E")

	if start is None or end is None:
		print("Maze must include 'S' (start) and 'E' (end).")
		return

	rows = len(maze)
	cols = len(maze[0]) if rows > 0 else 0

	queue = deque([start])
	visited = {start}
	parent = {}

	# 4-direction movement: down, up, right, left
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

	found = False
	while queue:
		current = queue.popleft()
		if current == end:
			found = True
			break

		r, c = current
		for dr, dc in directions:
			nr, nc = r + dr, c + dc
			if 0 <= nr < rows and 0 <= nc < cols:
				if maze[nr][nc] != "#" and (nr, nc) not in visited:
					visited.add((nr, nc))
					parent[(nr, nc)] = current
					queue.append((nr, nc))

	if not found:
		print("No path found.")
		return

	# Rebuild path from E back to S
	path = []
	node = end
	while node != start:
		path.append(node)
		node = parent[node]
	path.reverse()

	# Mark path using '.' but keep S and E unchanged
	for r, c in path:
		if maze[r][c] not in ("S", "E"):
			maze[r][c] = "."

	print("Solved maze:")
	for row in maze:
		print("".join(row))


if __name__ == "__main__":
	sample_maze = [
		"##########",
		"#S#   #  #",
		"# # # ## #",
		"# # #    #",
		"#   #### #",
		"###    #E#",
		"##########",
	]

	solve_maze(sample_maze)
