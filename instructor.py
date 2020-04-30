class Instructor():

    def __init__(self, first, last, slack, specialty, cohort):
        self.first_name = first
        self.last_name = last
        self.slack = slack
        self.specialty = specialty
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is instructing {self.cohort}'



# from person import Person

# class Instructor(Person):

#     def __init__(self, first_name, last_name, slack_handle, specialty):
#         super().__init__(first_name, last_name, slack_handle)
#         self.cohort = ""
#         self.specialty = specialty

#     def assign_exercise(self, exercise, student):
#         student.exercises.append(exercise)