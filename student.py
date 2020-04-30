class Student():

    def __init__(self, first, last, slack, cohort):
        self.first_name = first
        self.last_name = last
        self.slack = slack
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'



# from person import Person

# class Student(Person):

#     def __init__(self, first_name, last_name, slack_handle):
#         super().__init__(first_name, last_name, slack_handle)
#         self.cohort = ""
#         self.exercises = []

#     def exercise_report(self):
#         exercises = []
#         for exercise in self.exercises:
#             exercises.append(exercise.name)
#         last_exercise = exercises[-1]
#         exercises.pop()
#         joined_exercises = ", ".join(exercises)
#         print(f"{self.first_name} is working on {joined_exercises} and {last_exercise}")


