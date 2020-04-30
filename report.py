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

        """Retrieve c# exercises"""

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



reports = StudentExerciseReports()
reports.all_cohorts()
reports.all_students()
reports.all_instructors()
reports.all_exercises()
reports.javascript_exercises()
reports.python_exercises()
reports.cSharp_exercises()



