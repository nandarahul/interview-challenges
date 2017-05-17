from csvfile import CSVFile

class Evaluator(object):
    def __init__(self, csv_path, csv_format):
        self.CSVObj = CSVFile(csv_path, csv_format)

    def evaluate(self):
        self.CSVObj.read_line()