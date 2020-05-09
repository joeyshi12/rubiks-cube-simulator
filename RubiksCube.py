import random


class RubiksCube:
    # white  = 0 (front)
    # red    = 1 (left)
    # green  = 2 (top)
    # blue   = 3 (bottom)
    # orange = 4 (right)
    # yellow = 5 (back)
    COLOURS = ['W', 'R', 'G', 'B', 'O', 'Y']
    COLOUR_MAP = {'W': (255, 255, 255), 'R': (255, 0, 0), 'G': (0, 255, 0),
                  'B': (0, 0, 255), 'O': (255, 165, 0), 'Y': (255, 255, 0)}

    def __init__(self):
        self.inverse_ops = []
        self.faces = []
        for i in range(6):
            self.faces.append([[self.COLOURS[i] for _ in range(3)] for _ in range(3)])

    def __str__(self):
        W = self.faces[0]
        R = self.faces[1]
        G = self.faces[2]
        B = self.faces[3]
        O = self.faces[4]
        Y = self.faces[5]
        return """
                %s %s %s
                %s %s %s
                %s %s %s

        %s %s %s   %s %s %s   %s %s %s   %s %s %s
        %s %s %s   %s %s %s   %s %s %s   %s %s %s
        %s %s %s   %s %s %s   %s %s %s   %s %s %s

                %s %s %s
                %s %s %s
                %s %s %s""" % (G[0][0], G[0][1], G[0][2], G[1][0], G[1][1], G[1][2], G[2][0], G[2][1], G[2][2],
                               R[0][0], R[0][1], R[0][2], W[0][0], W[0][1], W[0][2], O[0][0], O[0][1], O[0][2], Y[0][0],
                               Y[0][1], Y[0][2],
                               R[1][0], R[1][1], R[1][2], W[1][0], W[1][1], W[1][2], O[1][0], O[1][1], O[1][2], Y[1][0],
                               Y[1][1], Y[1][2],
                               R[2][0], R[2][1], R[2][2], W[2][0], W[2][1], W[2][2], O[2][0], O[2][1], O[2][2], Y[2][0],
                               Y[2][1], Y[2][2],
                               B[0][0], B[0][1], B[0][2], B[1][0], B[1][1], B[1][2], B[2][0], B[2][1], B[2][2])

    def shuffle(self):
        cube_ops = [self.right, self.up, self.left, self.down, self.front, self.back]
        for _ in range(10):
            random.choice(cube_ops)()

    def is_solved(self) -> bool:
        for c in range(6):
            for i in range(3):
                for j in range(3):
                    if self.faces[c][i][j] != self.COLOURS[c]:
                        return False
        return True

    def step_back(self):
        op = self.inverse_ops.pop()
        op()
        self.inverse_ops.pop()

    def __rotate_clockwise(self, face_idx):
        face = self.faces[face_idx]
        self.faces[face_idx] = [[face[2][0], face[1][0], face[0][0]],
                                [face[2][1], face[1][1], face[0][1]],
                                [face[2][2], face[1][2], face[0][2]]]

    def __rotate_counter_clockwise(self, face_idx):
        face = self.faces[face_idx]
        self.faces[face_idx] = [[face[0][2], face[1][2], face[2][2]],
                                [face[0][1], face[1][1], face[2][1]],
                                [face[0][0], face[1][0], face[2][0]]]

    def front(self):
        temp = [self.faces[2][2][0], self.faces[2][2][1], self.faces[2][2][2]]
        for i in range(3):
            self.faces[2][2][i] = self.faces[1][2 - i][2]
            self.faces[1][2 - i][2] = self.faces[3][0][2 - i]
            self.faces[3][0][2 - i] = self.faces[4][i][0]
            self.faces[4][i][0] = temp[i]
        self.__rotate_clockwise(0)
        self.inverse_ops.append(self.front_prime)

    def front_prime(self):
        temp = [self.faces[2][2][0], self.faces[2][2][1], self.faces[2][2][2]]
        for i in range(3):
            self.faces[2][2][i] = self.faces[4][i][0]
            self.faces[4][i][0] = self.faces[3][0][2 - i]
            self.faces[3][0][2 - i] = self.faces[1][2 - i][2]
            self.faces[1][2 - i][2] = temp[i]
        self.__rotate_counter_clockwise(0)
        self.inverse_ops.append(self.front)

    def left(self):
        temp = [self.faces[0][0][0], self.faces[0][1][0], self.faces[0][2][0]]
        for i in range(3):
            self.faces[0][i][0] = self.faces[2][i][0]
            self.faces[2][i][0] = self.faces[5][2 - i][2]
            self.faces[5][2 - i][2] = self.faces[3][i][0]
            self.faces[3][i][0] = temp[i]
        self.__rotate_clockwise(1)
        self.inverse_ops.append(self.left_prime)

    def left_prime(self):
        temp = [self.faces[0][0][0], self.faces[0][1][0], self.faces[0][2][0]]
        for i in range(3):
            self.faces[0][i][0] = self.faces[3][i][0]
            self.faces[3][i][0] = self.faces[5][2 - i][2]
            self.faces[5][2 - i][2] = self.faces[2][i][0]
            self.faces[2][i][0] = temp[i]
        self.__rotate_counter_clockwise(1)
        self.inverse_ops.append(self.left)

    def up(self):
        temp = self.faces[0][0]
        self.faces[0][0] = self.faces[4][0]
        self.faces[4][0] = self.faces[5][0]
        self.faces[5][0] = self.faces[1][0]
        self.faces[1][0] = temp
        self.__rotate_clockwise(2)
        self.inverse_ops.append(self.up_prime)

    def up_prime(self):
        temp = self.faces[0][0]
        self.faces[0][0] = self.faces[1][0]
        self.faces[1][0] = self.faces[5][0]
        self.faces[5][0] = self.faces[4][0]
        self.faces[4][0] = temp
        self.__rotate_counter_clockwise(2)
        self.inverse_ops.append(self.up)

    def down(self):
        temp = self.faces[0][2]
        self.faces[0][2] = self.faces[1][2]
        self.faces[1][2] = self.faces[5][2]
        self.faces[5][2] = self.faces[4][2]
        self.faces[4][2] = temp
        self.__rotate_clockwise(3)
        self.inverse_ops.append(self.down_prime)

    def down_prime(self):
        temp = self.faces[0][2]
        self.faces[0][2] = self.faces[4][2]
        self.faces[4][2] = self.faces[5][2]
        self.faces[5][2] = self.faces[1][2]
        self.faces[1][2] = temp
        self.__rotate_counter_clockwise(3)
        self.inverse_ops.append(self.down)

    def right(self):
        temp = [self.faces[0][0][2], self.faces[0][1][2], self.faces[0][2][2]]
        for i in range(3):
            self.faces[0][i][2] = self.faces[3][i][2]
            self.faces[3][i][2] = self.faces[5][2 - i][0]
            self.faces[5][2 - i][0] = self.faces[2][i][2]
            self.faces[2][i][2] = temp[i]
        self.__rotate_clockwise(4)
        self.inverse_ops.append(self.right_prime)

    def right_prime(self):
        temp = [self.faces[0][0][2], self.faces[0][1][2], self.faces[0][2][2]]
        for i in range(3):
            self.faces[0][i][2] = self.faces[2][i][2]
            self.faces[2][i][2] = self.faces[5][2 - i][0]
            self.faces[5][2 - i][0] = self.faces[3][i][2]
            self.faces[3][i][2] = temp[i]
        self.__rotate_counter_clockwise(4)
        self.inverse_ops.append(self.right)

    def back(self):
        temp = [self.faces[2][0][0], self.faces[2][0][1], self.faces[2][0][2]]
        for i in range(3):
            self.faces[2][0][i] = self.faces[4][i][2]
            self.faces[4][i][2] = self.faces[3][2][2 - i]
            self.faces[3][2][2 - i] = self.faces[1][2 - i][0]
            self.faces[1][2 - i][0] = temp[i]
        self.__rotate_clockwise(5)
        self.inverse_ops.append(self.back_prime)

    def back_prime(self):
        temp = [self.faces[2][0][0], self.faces[2][0][1], self.faces[2][0][2]]
        for i in range(3):
            self.faces[2][0][i] = self.faces[1][2 - i][0]
            self.faces[1][2 - i][0] = self.faces[3][2][2 - i]
            self.faces[3][2][2 - i] = self.faces[4][i][2]
            self.faces[4][i][2] = temp[i]
        self.__rotate_counter_clockwise(5)
        self.inverse_ops.append(self.back)