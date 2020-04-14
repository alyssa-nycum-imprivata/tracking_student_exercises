class Instructor:

    def __init__(self, first_name, last_name, slack_handle, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack_handle
        self.cohort = ""
        self.specialty = specialty

    def assign_exercise(self, exercise, student):
        student.exercises.append(exercise)