from collections import deque

row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]


def is_safe(mat, x, y, processed):
    return 0 <= x < len(processed) and 0 <= y < len(processed[0]) and mat[x][y] == 1 and not processed[x][y]


def BFS(mat, processed, i, j):
    q = deque()
    q.append((i, j))
    processed[i][j] = True

    while q:
        x, y = q.popleft()

        for k in range(8):
            if is_safe(mat, x + row[k], y + col[k], processed):
                processed[x + row[k]][y + col[k]] = True
                q.append(([x + row[k], y + col[k]]))


if __name__ == "__main__":
    my_map = [[1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
              [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
              [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
              [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
              [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
              [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
              [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
              [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
              [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]]

    (M, N) = (len(my_map), len(my_map[0]))
    check = [[False for i in range(N)] for j in range(M)]
    islands = 0

    for i in range(M):
        for j in range(N):
            if my_map[i][j] == 1 and not check[i][j]:
                BFS(my_map, check, i, j)
                islands += 1

    print("Tổng số đảo:", islands)
