class Cohort:

    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructors = []

    def __repr__(self):
        return f'{self.name}'