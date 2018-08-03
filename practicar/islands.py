# Assume you need to find the number of islands in a grid, in 4 directions
# 0 1
# 0 1
#
# or
#
# 1 1 0
# 0 0 0
# 1 1 1
#

def valid(next_i, next_j, m):
    return (next_i > -1) and (next_i < len(m)) and (next_j > -1) and (next_j < len(m[0]))

def unseen(next_i, next_j, seen):
    return not seen[next_i][next_j]

def land(next_i, next_j, m):
    return m[next_i][next_j] == 1

def next_elements(i, j):
    return [[i-1, j], [i, j+1], [i+1, j], [i, j-1]]

def bfs(i, j, m, seen):
    seen[i][j] = True
    for next_i, next_j in next_elements(i, j):
        if valid(next_i, next_j, m) and unseen(next_i, next_j, seen) and land(next_i, next_j, m):
            bfs(next_i, next_j, m, seen)

def number_of_islands(m):
    islands = 0
    seen = [[False for j in range(len(m[0]))] for i in range(len(m))]

    for i, row in enumerate(m):
        for j, entry in enumerate(row):
            if seen[i][j]:
                continue

            if (m[i][j] == 1):
                islands += 1
                bfs(i, j, m, seen)
    return islands


m0 = []
m1 = [[1]]
m2 = [[1, 0, 1], [1, 1, 0], [1, 0, 0]]
m3 = [[1, 0], [1, 1]]
m4 = [[1, 0, 1], [1, 0, 1]]

assert number_of_islands(m0) == 0
assert number_of_islands(m1) == 1
assert number_of_islands(m2) == 2
assert number_of_islands(m3) == 1
assert number_of_islands(m4) == 2

