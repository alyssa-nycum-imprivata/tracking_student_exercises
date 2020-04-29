CREATE TABLE Cohort (
	Id 		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name 	TEXT NOT NULL UNIQUE
);

CREATE TABLE Student (
	Id			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	First_Name 	TEXT NOT NULL UNIQUE,
	Last_Name 	TEXT NOT NULL UNIQUE,
	Slack		TEXT NOT NULL UNIQUE,
	CohortId	INTEGER NOT NULL REFERENCES Cohort(Id)
);

CREATE TABLE Instructor (
	Id			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	First_Name 	TEXT NOT NULL UNIQUE,
	Last_Name 	TEXT NOT NULL UNIQUE,
	Slack		TEXT NOT NULL UNIQUE,
	Specialty	TEXT NOT NULL UNIQUE,
	CohortId	INTEGER NOT NULL REFERENCES Cohort(Id)	
);

CREATE TABLE Exercise (
	Id 			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	Name 		TEXT NOT NULL UNIQUE,
	Language 	TEXT NOT NULL UNIQUE
);

CREATE TABLE Student_Exercises (
	Id  		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	StudentId	INTEGER NOT NULL REFERENCES Student(Id),
	ExerciseId 	INTEGER NOT NULL REFERENCES Exercise(Id)
);

--Add 3 cohorts

INSERT INTO Cohort (Name)
Values ("Cohort 38"), ("Cohort 37"), ("Cohort 36");

SELECT * FROM Cohort;

--Add 5 exercises 

INSERT INTO Exercise (Name, Language)
VALUES ("Movie Page", "HTML"), ("Flex-Box Froggy", "CSS"), ("ChickenMonkey", "JavaScript"), ("Kennel", "React"), ("Flower Shop", "Python");

SELECT * FROM Exercise;

--Add 3 instructors
INSERT INTO Instructor (First_Name, Last_Name, Slack, Specialty, CohortId) 
VALUES ("Jisie", "David", "@jisiedavid", "Googling", 3), ("Andy", "Collins", "@andycollins", "Dry Humor", 1), ("Bryan", "Neilson", "@bryanneilson", "Dad Jokes", 2);

SELECT * FROM Instructor;

--Add 7 students 
INSERT INTO Student (First_Name, Last_Name, Slack, CohortId)
VALUES ("Alyssa", "Nycum", "@alyssanycum", 1), ("Katy", "Wohl", "@katywohl", 1), ("Dustin", "Murdock", "@dustinmurdock", 1), ("Cooper", "Nichols", "@coopernichols", 2), ("Sofia", "Candiani", "@sofiacandiani", 2), ("Matt", "Crook", "@mattcrook", 3), ("Jeremy", "Mattingly", "@jeremymattingly", 3);

SELECT * FROM Student;

--Assign 2 exercises to each student 
INSERT INTO Student_Exercises (StudentId, ExerciseId)
VALUES (1, 1), (1, 2), (2, 3), (2, 4), (3, 5), (3, 1), (4, 2), (4, 3), (5, 4), (5, 5), (6, 1), (6, 2), (7, 3), (7, 4);

SELECT * FROM Student_Exercises;