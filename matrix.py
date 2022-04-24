class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string  = matrix_string

    def get_rows(self):
        matrix_list = []
        for dirty in self.matrix_string.split("\n"):
            matrix_list.append([int(clean) for clean in dirty.split()])
        return matrix_list

    def get_columns(self):
        matrix_list = []
        for element in zip(*self.get_rows()):
            matrix_list.append(list(element))
        return matrix_list
    
    def row(self, index):
        matrix = self.get_rows()
        print(matrix)
        return matrix[index - 1]

    def column(self, index):
        matrix = self.get_columns()
        return matrix[index - 1]
