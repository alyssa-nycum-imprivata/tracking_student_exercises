from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

# Create 4, or more, exercises.

python_lists = Exercise("lists", "python")
python_dictionaries = Exercise("dictionaries", "python")
python_tuples = Exercise("tuples", "python")
python_sets = Exercise("sets", "python")

# Create 3, or more, cohorts.

cohort_38 = Cohort(38)
cohort_37 = Cohort(37)
cohort_36 = Cohort(36)

# Create 4, or more, students and assign them to one of the cohorts.

alyssa_nycum = Student("Alyssa", "Nycum", "alyssanycum")
john_long = Student("John", "Long", "johnlong")
onterio_wright = Student("Onterio", "Wright", "onteriowright")
katie_wohl = Student("Katie", "Wohl", "katiewohl")

cohort_38.students.append(alyssa_nycum)
alyssa_nycum.cohort = cohort_38.name
cohort_38.students.append(katie_wohl)
katie_wohl.cohort = cohort_38.name
cohort_37.students.append(onterio_wright)
onterio_wright.cohort = cohort_37.name
cohort_36.students.append(john_long)
john_long.cohort = cohort_36.name

# Create 3, or more, instructors and assign them to one of the cohorts.

bryan_neilson = Instructor("Bryan", "Neilson", "bryanneilson", "dad jokes")
kristen_norris = Instructor("Kristen", "Norris", "kristennorris", "to-the-point responses")
andy_collins = Instructor("Andy", "Collins", "andycollins", "dry humor")

cohort_36.instructors.append(andy_collins)
andy_collins.cohort = cohort_36.name
cohort_37.instructors.append(bryan_neilson)
bryan_neilson.cohort = cohort_37.name
cohort_38.instructors.append(kristen_norris)
kristen_norris.cohort = cohort_38.name

# Have each instructor assign 2 exercises to each of the students.

kristen_norris.assign_exercise(python_dictionaries, alyssa_nycum)
kristen_norris.assign_exercise(python_lists, alyssa_nycum)
kristen_norris.assign_exercise(python_sets, alyssa_nycum)
kristen_norris.assign_exercise(python_sets, katie_wohl)
kristen_norris.assign_exercise(python_tuples, katie_wohl)
bryan_neilson.assign_exercise(python_dictionaries, onterio_wright)
bryan_neilson.assign_exercise(python_lists, onterio_wright)
andy_collins.assign_exercise(python_sets, john_long)
andy_collins.assign_exercise(python_tuples, john_long)

# Create a list of students. Add all of the student instances to it.

students = [alyssa_nycum, katie_wohl, john_long, onterio_wright]

# Create a list of exercises. Add all of the exercise instances to it.

exercises = [python_lists, python_dictionaries, python_sets, python_tuples]

# Now, generate a report that displays which students are working on which exercises.

for student in students:
    student.exercise_report()

