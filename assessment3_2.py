"""
Assessment 3.2 - Student Class

Write a "Student" class, as defined below, that keeps track of all created students.

Your class should implement the following methods, class variables and properties:

- An instance attribute called "name".

- A property called "grade" that returns the grade of that student. Trying to set the grade should raise a ValueError if the new grade
is not a new number between 0 and 100.

- A static method called "calculate_average_grade(students) that accepts a list of "Student" objects and returns the average grade for 
those students. If there are no students in the list, it should return -1.

- A class variable called "all_students" that stores all of the student objects that have been created in a list.

- A class method called "get_average_grade()" which returns the average grade of all created students.

- A class method named "get_best_student" which returns the student object with the best grade out of all the currently created students.
If there are no students created this method should return "None". You may assume there will always be one student with the best grade,
except in the case where there are no students created.
"""

class Student:
    # Write your code here.
    all_students = []           # Class variable (pg.8)

    def __init__(self, name, grade):
        # Write your code here.
        self.name = name        # Instance attribute (pg.8)
        self._grade = grade     # Instance attribute (pg.8)
        Student.all_students.append(self)
        
        @property               # Property (pg.7)
        def grade(self):        # Getter (pg.7)
            return self._grade

        @grade.setter           # Setter (pg.7)
        def grade(self, grade):
            # Checks if grade is between 0-100, raises ValueError otherwise (pg.7):
            if grade < 0 or grade > 100:
                raise ValueError("Grade should be between 0-100.")
            self._grade = grade

    @classmethod
    def get_best_student(cls):  # cls is a mandatory parameter for any class method, stands for name of class (pg.8)
        best_student = None
        for student in cls.all_students:
            if best_student == None or best_student.grade < student.grade:
                best_student = student
        return best_student
    
    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)

    @staticmethod
    def calculate_average_grade(students):
        # Returns -1 if list is empty:
        if len(students) == 0:
            return -1
        
        # Calculates average grade:
        total = 0
        for student in students:
            total += student.grade
        return total / len(students)

