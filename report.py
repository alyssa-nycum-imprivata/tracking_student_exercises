import sqlite3
from student import Student
from instructor import Instructor
from cohort import Cohort
from exercise import Exercise

class StudentExerciseReports():

    print("----------------------------------------")
    print("****STUDENT EXERCISE REPORTS****")
    print("----------------------------------------")

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/alyssanycum/workspace/bootcamp/python/tracking_student_exercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])            
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT s.Id,
                s.First_Name,
                s.Last_Name,
                s.Slack,
                s.CohortId,
                c.Name
            FROM Student s
            JOIN Cohort c ON s.CohortId = c.Id
            ORDER BY s.CohortId
            """)

            all_students = db_cursor.fetchall()

            # print(all_students)

            # for student in all_students:
                # print(student)

            print("****STUDENTS****")
            [print(s) for s in all_students]
            print("----------------------------------------")

    def all_instructors(self):

        """Retrieve all instructors with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row[1], row[2], row[3], row[4], row[6])            
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT i.Id,
                i.First_Name,
                i.Last_Name,
                i.Slack,
                i.Specialty,
                i.CohortId,
                c.Name
            FROM Instructor i
            JOIN Cohort c ON i.CohortId = c.Id
            ORDER BY i.CohortId
            """)

            all_instructors = db_cursor.fetchall()

            print("****INSTRUCTORS****")
            [print(i) for i in all_instructors]
            print("----------------------------------------")

    def all_cohorts(self):

        """Retrieve all cohorts"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[1])      
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT Id,
                Name
            FROM Cohort
            ORDER BY Id
            """)

            all_cohorts = db_cursor.fetchall()

            print("****COHORTS****")
            [print(c) for c in all_cohorts]
            print("----------------------------------------")

    def all_exercises(self):

        """Retrieve all exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2]) 
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT Id,
                Name,
                Language
            FROM Exercise
            ORDER BY Id
            """)

            all_exercises = db_cursor.fetchall()

            print("****EXERCISES****")
            [print(e) for e in all_exercises]
            print("----------------------------------------")

    def javascript_exercises(self):

        """Retrieve JavaScript exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2]) 
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT Id,
                Name,
                Language
            FROM Exercise
            WHERE Language LIKE "javascript"
            ORDER BY Id
            """)

            javascript_exercises = db_cursor.fetchall()

            print("****JAVASCRIPT EXERCISES****")
            for e in javascript_exercises:
                print(e.name)
            print("----------------------------------------")

    def python_exercises(self):

        """Retrieve Python exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2]) 
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT Id,
                Name,
                Language
            FROM Exercise
            WHERE Language LIKE "python"
            ORDER BY Id
            """)

            python_exercises = db_cursor.fetchall()

            print("****PYTHON EXERCISES****")
            for e in python_exercises:
                print(e.name)
            print("----------------------------------------")

    def cSharp_exercises(self):

        """Retrieve C# exercises"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[1], row[2]) 
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT Id,
                Name,
                Language
            FROM Exercise
            WHERE Language LIKE "cSharp"
            ORDER BY Id
            """)

            cSharp_exercises = db_cursor.fetchall()

            print("****C# EXERCISES****")
            if len(cSharp_exercises) == 0:
                    print("No exercises")
            else:
                for e in cSharp_exercises:
                    print(e.name)
            print("----------------------------------------")

    def exercises_with_students(self):

        """Retrieve all exercises with the students assigned to each exercise"""

        exercises = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    e.Id AS ExerciseId,
                    e.Name,
                    s.Id,
                    s.First_Name,
                    s.Last_Name
                FROM Exercise e
                JOIN Student_Exercises se ON se.ExerciseId = e.Id
                JOIN Student s ON s.Id = se.StudentId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                student_id = row[2]
                student_name = f'{row[3]} {row[4]}'

                if exercise_name not in exercises:
                    exercises[exercise_name] = [student_name]
                else:
                    exercises[exercise_name].append(student_name)

            print("****EXERCISES WITH ASSIGNED STUDENTS****")
            for exercise_name, students in exercises.items():
                print(exercise_name)
                for student in students:
                    print(f'\t* {student}')
            print("----------------------------------------")

    def students_with_exercises(self):
        
        """Retrieve all students with the exercises assigned to each student"""

        students = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    s.Id AS StudentId,
                    s.First_Name,
                    s.Last_Name,
                    e.Id AS ExerciseId,
                    e.Name
                FROM Student s
                JOIN Student_Exercises se ON se.StudentId = s.Id
                JOIN Exercise e ON e.Id = se.ExerciseId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                student_id = row[0]
                student_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]

                if student_name not in students:
                    students[student_name] = [exercise_name]
                else:
                    students[student_name].append(exercise_name)

            print("****STUDENTS WITH ASSIGNED EXERCISES****")
            for student_name, exercises in students.items():
                print(f'{student_name} is working on:')
                for exercise in exercises:
                    print(f'\t* {exercise}')
            print("----------------------------------------")

    def instructors_with_exercises(self):

        """Retrieve all instructors with the exercises each instructor assigns"""

        instructors = dict()

        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    i.Id AS InstructorId,
                    i.First_Name,
                    i.Last_Name,
                    e.Id AS ExerciseId,
                    e.Name
                FROM Instructor i
                JOIN Student_Exercises se ON i.Id = se.InstructorId
                JOIN Exercise e ON e.Id = se.ExerciseId
                GROUP BY ExerciseId
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                instructor_id = row[0]
                instructor_name = f'{row[1]} {row[2]}'
                exercise_id = row[3]
                exercise_name = row[4]

                if instructor_name not in instructors:
                    instructors[instructor_name] = [exercise_name]
                else:
                    instructors[instructor_name].append(exercise_name)

            print("****INSTRUCTORS WITH ASSIGNED EXERCISES****")
            for instructor_name, exercises in instructors.items():
                print(f'{instructor_name} has assigned:')
                for exercise in exercises:
                    print(f'\t* {exercise}')
            print("----------------------------------------")

    def exercises_with_instructors_and_students(self):

        """Retrieve all exercises with the instructors that assign each exercise and which students they assign each exercise to"""

        exercises = dict()
    
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
                SELECT
                    e.Id AS ExerciseId,
                    e.Name,
                    i.Id AS InstructorId,
                    i.First_Name,
                    i.Last_Name,
                    s.Id AS StudentId,
                    s.First_Name,
                    s.Last_Name
                FROM Instructor i 
                JOIN Student_Exercises se ON i.Id = se.InstructorId
                JOIN Exercise e ON e.Id = se.ExerciseId
                JOIN Student s ON s.Id = se.StudentId
                GROUP BY se.ExerciseId, s.Id
            """)

            dataset = db_cursor.fetchall()

            for row in dataset:
                exercise_id = row[0]
                exercise_name = row[1]
                instructor_id = row[2]
                instructor_name = f'{row[3]} {row[4]}'
                student_id = row[5]
                student_name = f'{row[6]} {row[7]}'
                
                if exercise_name not in exercises:
                    exercises[exercise_name] = {}
                    if instructor_name not in exercises[exercise_name]:
                        exercises[exercise_name] = {
                            instructor_name: [student_name]
                            }
                    else:
                        exercises[exercise_name][instructor_name].append(student_name)
                else: 
                    exercises[exercise_name][instructor_name].append(student_name)
                    
            print("****EXERCISES WITH ASSIGNED INSTRUCTORS AND STUDENTS****")
            for exercise_name, instructors in exercises.items():
                print(exercise_name)
                for instructor in instructors:
                    for students in instructors.values():
                        for student in students:
                            print(f"\t* {instructor} assigned this to {student}")
            print("----------------------------------------")

reports = StudentExerciseReports()
reports.all_cohorts()
reports.all_students()
reports.all_instructors()
reports.all_exercises()
reports.javascript_exercises()
reports.python_exercises()
reports.cSharp_exercises()
reports.exercises_with_students()
reports.students_with_exercises()
reports.instructors_with_exercises()
reports.exercises_with_instructors_and_students()


