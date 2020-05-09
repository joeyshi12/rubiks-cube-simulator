from RubiksCube import RubiksCube
from collections import deque

rc = RubiksCube()
op_map = {'F': rc.front, 'FP': rc.front_prime,
          'L': rc.left,  'LP': rc.left_prime,
          'U': rc.up,    'UP': rc.up_prime,
          'D': rc.down,  'DP': rc.down_prime,
          'R': rc.right, 'RP': rc.right_prime,
          'B': rc.back,  'BP': rc.back_prime}


def process(seq):
    for t in seq:
        op_map[t]()


def invert(seq):
    n = len(seq)
    for i in range(n):
        if len(seq[n - 1 - i]) == 2:
            print(seq[n - 1 - i][0])
            op_map[seq[n - 1 - i][0]]()
        else:
            print(seq[n - 1 - i] + 'P')
            op_map[seq[n - 1 - i] + 'P']()


def check(seq: list, next_op):
    seq.append(next_op)
    process(seq)
    if rc.is_solved():
        return True
    invert(seq)
    seq.pop()
    return False


def solve():
    print("WORK IN PROGRESS")


if __name__ == '__main__':
    seq = ['R', 'L', 'D', 'R', 'F']
    process(seq)
    invert(seq)
    print(rc)
