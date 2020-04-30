class Exercise:

    def __init__(self, name, language):
        self.name = name
        self.language = language

    def __repr__(self):
        return f'The {self.name} exercise is in {self.language}'