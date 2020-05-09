from RubiksCube import RubiksCube
from collections import deque

rc = RubiksCube()
opMap = {'F': rc.front, 'FP': rc.front_prime,
         'L': rc.left, 'LP': rc.left_prime,
         'U': rc.up, 'UP': rc.up_prime,
         'D': rc.down, 'DP': rc.down_prime,
         'R': rc.right, 'RP': rc.right_prime,
         'B': rc.back, 'BP': rc.back_prime}


def process(seq):
    for t in seq:
        opMap[t]()


def invert(seq):
    n = len(seq)
    for i in range(n):
        if len(seq[n - 1 - i]) == 2:
            print(seq[n - 1 - i][0])
            opMap[seq[n - 1 - i][0]]()
        else:
            print(seq[n - 1 - i] + 'P')
            opMap[seq[n - 1 - i] + 'P']()


def solve():
    return


if __name__ == '__main__':
    seq = ['R', 'FP', 'L', 'D', 'R', 'BP']
    process(seq)
    invert(seq)
    print(rc)
