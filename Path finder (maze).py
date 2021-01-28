# Task
# You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
# (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.
# Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases.

# TO DO:
# fix the stop condition
# update alghoritm to find the SHORTEST path, not any possible


def path_finder(maze):
    if maze == []: return True
    maze_matrix = translate_maze(maze) # translates maze to matrix where 1: walls, 0:no walls
    start = 0, 0
    end = len(maze_matrix)-1, len(maze_matrix)-1

    m = [] # zeros matrix where we mark path
    for i in range(len(maze_matrix)):
        m.append([0])
        for j in range(len(maze_matrix[i])-1):
            m[-1].append(0)
    i,j = start
    m[i][j] = 1

    # function checks if/where we can make step no. k
    def make_step(k):
        is_changed = False
        for i in range(len(m)):
            for j in range(len(m[i])):
                if m[i][j] == k:
                    if i > 0 and m[i - 1][j] == 0 and maze_matrix[i - 1][j] == 0:
                        m[i - 1][j] = k + 1
                        is_changed = True
                    elif j > 0 and m[i][j - 1] == 0 and maze_matrix[i][j - 1] == 0:
                        m[i][j - 1] = k + 1
                        is_changed = True
                    elif i < len(m) - 1 and m[i + 1][j] == 0 and maze_matrix[i + 1][j] == 0:
                        m[i + 1][j] = k + 1
                        is_changed = True
                    elif j < len(m[i]) - 1 and m[i][j+1] == 0 and maze_matrix[i][j+1] == 0:
                        m[i][j + 1] = k + 1
                        is_changed = True
        return is_changed



    # checking all possible steps
    next = True
    k = 0
    while m[end[0]][end[1]] == 0:
        temp = m
        k += 1
        next = make_step(k)
        if next == False:
            return False
        # if m == temp :
        #     return False

    #finding the shortest path
    i, j = end
    k = m[i][j]
    the_path = [(i, j)]
    while k > 1:
        if i > 0 and m[i - 1][j] == k - 1:
            i, j = i - 1, j
            the_path.append((i, j))
            k -= 1
        elif j > 0 and m[i][j - 1] == k - 1:
            i, j = i, j - 1
            the_path.append((i, j))
            k -= 1
        elif i < len(m) - 1 and m[i + 1][j] == k - 1:
            i, j = i + 1, j
            the_path.append((i, j))
            k -= 1
        elif j < len(m[i]) - 1 and m[i][j + 1] == k - 1:
            i, j = i, j + 1
            the_path.append((i, j))
            k -= 1

    # print(m)
    print(the_path)
    return len(the_path)-1


def translate_maze(maze):
    new_maze = []
    maze = maze.replace('.', '0')
    maze = maze.replace('W', '1')
    for line in maze.splitlines():
        temp = []
        for item in line:
            temp.append(int(item))
        new_maze.append(temp)
    return new_maze


b = "\n".join([
  ".W.",
  ".W.",
  "..."
])

print(path_finder(b))