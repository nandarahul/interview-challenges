
class Exression(object):
    def __init__(self):
        self.name = None


class Equation(Exression):
    def __init__(self, string):
        if not self.check_valid(string):
            raise Exception("Invalid Equation")
        self.string = string
        self.valid_operators = []
        self.valid_operands = []

    def check_valid(self, string):
        pass

    def evaluate_left_to_right(self):
        pass

    def evaluate_right_to_left(self):
        pass

class URL(Exression):
    def __init__(self, string):
        self.string = string

    def check_valid(self):
        pass

    def evaluate_http_status_code(self):
        pass

class SetExpression(Exression):
    def __init__(self, string, operator):
        self.string = string
        self.operator = operator

    def check_valid(self):
        pass

    def evaluate_intersection(self):
        pass


