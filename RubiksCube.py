import random


class RubiksCube:
    def __init__(self):
        # white  = 0 (front)
        # red    = 1 (left)
        # green  = 2 (top)
        # blue   = 3 (bottom)
        # orange = 4 (right)
        # yellow = 5 (back)
        colours = ['W', 'R', 'G', 'B', 'O', 'Y']
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
        cubeOps = [self.right, self.up, self.left, self.down, self.front, self.back]
        for _ in range(100):
            op = random.choice(cubeOps)
            op()

    def __rotateClockwise(self, faceIdx):
        face = self.faces[faceIdx]
        self.faces[faceIdx] = [[face[2][0], face[1][0], face[0][0]],
                               [face[2][1], face[1][1], face[0][1]],
                               [face[2][2], face[1][2], face[0][2]]]

    def __rotateCounterClockwise(self, faceIdx):
        face = self.faces[faceIdx]
        self.faces[faceIdx] = [[face[0][2], face[1][2], face[2][2]],
                               [face[0][1], face[1][1], face[2][1]],
                               [face[0][0], face[1][0], face[2][0]]]

    def front(self):
        temp = [self.faces[2][2][0], self.faces[2][2][1], self.faces[2][2][2]]
        for i in range(3):
            self.faces[0][i][2] = self.faces[3][i][2]
            self.faces[3][i][2] = self.faces[5][2 - i][0]
            self.faces[5][2 - i][0] = self.faces[2][i][2]
            self.faces[2][i][2] = temp[i]
        self.__rotateClockwise(4)

    def up(self):
        temp = self.faces[0][0]
        self.faces[0][0] = self.faces[4][0]
        self.faces[4][0] = self.faces[5][0]
        self.faces[5][0] = self.faces[1][0]
        self.faces[1][0] = temp
        self.__rotateClockwise(2)

    def left(self):
        temp = [self.faces[0][0][0], self.faces[0][1][0], self.faces[0][2][0]]
        for i in range(3):
            self.faces[0][i][0] = self.faces[2][i][0]
            self.faces[2][i][0] = self.faces[5][2 - i][2]
            self.faces[5][2 - i][2] = self.faces[3][i][0]
            self.faces[3][i][0] = temp[i]
        self.__rotateClockwise(1)

    def down(self):
        temp = self.faces[0][2]
        self.faces[0][2] = self.faces[1][2]
        self.faces[1][2] = self.faces[5][2]
        self.faces[5][2] = self.faces[4][2]
        self.faces[4][2] = temp
        self.__rotateClockwise(3)

    def front(self):
        temp = [self.faces[2][2][0], self.faces[2][2][1], self.faces[2][2][2]]
        for i in range(3):
            self.faces[2][2][i] = self.faces[1][2 - i][2]
            self.faces[1][2 - i][2] = self.faces[3][0][2 - i]
            self.faces[3][0][2 - i] = self.faces[4][i][0]
            self.faces[4][i][0] = temp[i]
        self.__rotateClockwise(0)

    def back(self):
        temp = [self.faces[2][0][0], self.faces[2][0][1], self.faces[2][0][2]]
        for i in range(3):
            self.faces[2][0][i] = self.faces[4][i][2]
            self.faces[4][i][2] = self.faces[3][2][2 - i]
            self.faces[3][2][2 - i] = self.faces[1][2 - i][0]
            self.faces[1][2 - i][0] = temp[i]
        self.__rotateClockwise(5)
