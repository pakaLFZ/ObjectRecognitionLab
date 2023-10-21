import numpy as np
class confusionMatrix():
    def __init__(self, fields):
        self.fields = fields

        self.matrix = []
        for i in range(len(fields)):
            row = []
            for j in range(len(fields)):
                row.append(0)
            self.matrix.append(row)
        self.matrix = np.array(self.matrix)
        
        self.data = []
        """
            | field1 | field2 | field3
        No1
        No2
        No3
        
        """
    
    def load(self, output, answer):
        if not len(output) == len(answer) == len(self.fields):
            return "Data error. Please double check."
        row_no = np.argmax(answer)
        column_no = np.argmax(output)
        self.matrix[column_no][row_no] += 1

        self.data.append([output, answer])

        return self.matrix




