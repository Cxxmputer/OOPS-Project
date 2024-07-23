class School:
    # Initialize instances as soon as they are created.
    def __init__(self, name, year):
        self.name = name
        self.year = year

    """
    Using the '__str__' method which displays the following when we print the name of the class
    for instance, "School", rather than displaying the memory location of the object.
    """

    def __str__(self):
        return f"School: {self.name}; Year: {self.year}"


# Inheritance - A Template or Class called 'Person'; Defined For Derived Classes
# This class is explicitly created for 'name' and 'age'.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}; Age: {self.age}"


# Creating a derived class called 'Student,' also called "Person's Object."
class Student(Person):
    """
    Note:
        The variable 'name' and 'age' are derived from the previous class, but they are not going
        to be initialized become when creating objects, we are going to use 'Student' class not the Person as we are
        creating school project. Due to this we are going to use the 'super()' method/function.
    """

    def __init__(self, name, age, student_id, student_grade):
        # Using the 'super()' method/function to assign the provided value to the Parent class; 'Person.'
        super().__init__(name, age)
        self.student_id = student_id
        self.student_grade = student_grade

    def __str__(self):
        # Implementing mechanics for printing the following whenever the user prints the following class.
        # The first 'f' block represents the '__str__' function of the parent class, because we are using 'super()' method.
        return f"{super().__str__()}; ID: {self.student_id}; Grade: {self.student_grade}"


# This class is also derived from the 'Person' class.
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def __str__(self):
        # Implementing mechanics for printing the following whenever the user prints the following class.
        return f"{super().__str__()}; ID: {self.employee_id}; Subject: {self.subject}"


class SchoolManagement:
    def __init__(self):
        # Initialize an empty list for storing the schools, students, and teachers.
        self.schools = []
        self.students = []
        self.teachers = []

    def add_schools(self, school):
        # This function appends the provided name inside the 'school' variable to the empty list; 'schools.'
        self.schools.append(school)

    def add_students(self, student):
        # This function appends the provided name inside the 'student' variable to the empty list; 'students.'
        self.students.append(student)

    def add_teachers(self, teacher):
        # This function appends the provided name inside the 'teacher' variable to the empty list; 'teachers.'
        self.teachers.append(teacher)

    def school_list(self):
        # This function iterates over all the elements inside a given list and prints all the schools in the list.
        print("===============")
        print("LIST OF SCHOOLS")
        print("===============")
        for school in self.schools:
            print(school)

    def student_list(self):
        # This function iterates over all the elements inside a given list and prints all the student in the list.
        print("================")
        print("LIST OF STUDENTS")
        print("================")
        for student in self.students:
            print(student)

    def teacher_list(self):
        # This function iterates over all the elements inside a given list and prints all the teachers in the list.
        print("================")
        print("LIST OF TEACHERS")
        print("================")
        for teacher in self.teachers:
            print(teacher)


"""
INSTANTIATION IMPLEMENTATION TIME!
"""
school1 = School("Green House", 1778)
school2 = School("Millennium High", 1980)
print(school1)
print(school2)

student1 = Student("David", 18, 'S12354', '7th Grade')
student2 = Student("John", 19, 'S98765', '8th Grade')
print(student1)
print(student2)

teacher1 = Teacher("Mary", 45, 'T98765', 'Math')
teacher2 = Teacher("John", 40, 'T12345', 'Science')
print(teacher1)
print(teacher2)

school_manager = SchoolManagement()  # Creating an object of "SchoolManagement."

school_manager.add_schools(school1)  # Adds the previously implemented 'school1.'
school_manager.add_schools(school2)  # Adds the previously implemented 'school2.'
school_manager.school_list()  # Prints the list.

school_manager.add_students(student1)  # Adds the previously implemented 'student1.'
school_manager.add_students(student2)  # Adds the previously implemented 'student2.'
school_manager.student_list()  # Prints the list.

school_manager.add_teachers(teacher1)  # Adds the previously implemented 'teacher1.'
school_manager.add_teachers(teacher2)  # Adds the previously implemented 'teacher2.'
school_manager.teacher_list()  # Prints the list.
