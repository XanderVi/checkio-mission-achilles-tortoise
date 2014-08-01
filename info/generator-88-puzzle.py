from collections import deque

GOAL = (1, 2, 1, 0, 2, 0, 0, 3, 0, 4, 3, 4)

def rotate(state, ring):
    s = list(state)
    i = (0, 1, 5, 6)[ring - 1]
    s[i], s[i+3], s[i+5], s[i+2] = s[i+2], s[i+0], s[i+3], s[i+5]
    return tuple(s)


def puzzle88(state):
    visited = set()
    queue = deque(((state, ""),))
    goal_path = []
    while queue:
        st, path = queue.popleft()
        if st == GOAL:
            goal_path.append(path)
        if goal_path and len(path) > len(goal_path[0]):
            return goal_path
        if len(path) > 9:
            return None
        # if st in visited:
        #     continue
        visited.add(st)
        for r in "1234":
            new_st = rotate(st, int(r))
            queue.append((new_st, path + r))
    return goal_path or "IMPOSSIBLE"

def monkey_shuffle(state):
    from random import randint
    steps_L = randint(1, 100)
    # print("STEPS: ", steps_L)
    moves = ""
    for _ in range(steps_L):
        m = str(randint(1, 4))
        moves += m
        state = rotate(state, int(m))
    # print("MOVES: ", moves)
    # print("STATE: ", state)

    return state

from time import time

test = GOAL
for r in "111222333444":
    test = rotate(test, int(r))

# for r in "4231":
#     test = rotate(test, int(r))

# print(test)

T = [
    (0,2,1,3,2,1,4,0,0,4,0,3),
    test
]

# for _ in range(100):
for state in T:
    start = time()
    # state = monkey_shuffle(GOAL)
    ans = puzzle88(state)
    if ans is None:
        continue
    print("""{{
    "input": {},
    "answer": {},
    "time": {}
    }},""".format(state, ans, time() - start))
    # print("SOLUTION: ", puzzle88(monkey_shuffle(GOAL)))
    # print("TIME: ", time() - start)
    # print("=" * 50)
# monkey_shuffle(GOAL)
# monkey_shuffle(GOAL)
# monkey_shuffle(GOAL)

print(puzzle88((0,2,1,3,2,1,4,0,0,4,0,3)))