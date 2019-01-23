"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
from random import randint


def solution(edge, you, die):
    d = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    cycle = edge - 1
    y, x = cycle, cycle
    dic = [[y, x]]
    for i in range(cycle * 4 - 1):
        dy, dx = d[i // cycle]
        y += dy
        x += dx
        dic.append([y, x])
    return dic[(you+die) % (cycle*4)]


randoms = []
for _ in range(10):
    e = randint(3, 11)
    c = (e-1)*4
    y = randint(0, c-1)
    s = randint(0, c) * [1, 1, -1][randint(0, 2)]*[1, 1, 1, 1, 1, 1, 1, 1, 2, 3][randint(0, 9)]
    randoms.append({'input': [e, y, s], 'answer': solution(e, y, s)})

TESTS = {
    "Randoms": randoms,
    "Basics": [
        {
            "input": [4, 1, 4],
            "answer": [1, 0],
        },
        {
            "input": [6, 2, -3],
            "answer": [4, 5],
        },
    ],
}
