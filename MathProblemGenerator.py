import random

class MathProblemGenerator:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.operator = '+'
        self.solution = 0

    def generate_math_problem(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.operator = random.choice(['+', '-'])

        if self.operator == '+':
            self.solution = self.num1 + self.num2
        else:
            if self.num1 < self.num2:
                self.num1, self.num2 = self.num2, self.num1
            self.solution = self.num1 - self.num2

        problem = f"What is {self.num1} {self.operator} {self.num2}?"

        return problem, self.solution
