class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        str2 = ''
        for i in self.matrix:
            for a in i:
                a = str(a)
                str2 = str2 + a + ' '
            str2 = str2 + '\n'
        return f'{str2}'

    def __add__(self, other):

        count = len(self.matrix)  #for any matrix size
        list = []
        i = 0

        while i < count:
            k = 0
            s_list = []
            count2 = len(self.matrix[k])  #for any matrix size
            while k < count2:
                f = self.matrix[i][k] + other.matrix[i][k]
                s_list.append(f)
                k += 1
            i += 1
            list.append(s_list)
        return Matrix(list)


m1 = Matrix([[4, 3, 4], [2, 8, 1], [4, 2, 1], [4, 2, 1]])
m2 = Matrix([[2, 1, 5], [1, 4, 5], [1, 1, 1], [4, 2, 1]])
m3 = Matrix([[5, 2, 4], [7, 2, 7], [2, 1, 4], [4, 2, 1]])

print(m1)
print(m2)
print(m3)

print(m1 + m2 + m3)
