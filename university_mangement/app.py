class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
#Yahan humne inheritance ka use kiya hai, jisme super() method ka
#istemal hota hai. Isse hum parent class ki methods aur properties ko
#child class mein access kar sakte hain.

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
        self.courses = []

    def register_for_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        print(f"{self.name} is registered for the following courses:")
        for course in self.courses:
            print(f"- {course.name}")

class Instructor(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        print(f"{self.name} is teaching the following courses:")
        for course in self.courses:
            print(f"- {course.name}")

class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name
        self.students = []
        self.instructor = None

    def add_student(self, student):
        self.students.append(student)

    def assign_instructor(self, instructor):
        self.instructor = instructor

    def display_course_info(self):
        print(f"Course: {self.name} (ID: {self.course_id})")
        if self.instructor:
            print(f"Instructor: {self.instructor.name}")
        print("Registered students:")
        for student in self.students:
            print(f"- {student.name}")

def main():
    # Creating some courses
    course1 = Course('C001', 'Software Development')
    course2 = Course('C002', 'Computer Security and Networks')
    course3 = Course('C003', 'Web Development')

    # Creating some students
    student1 = Student('Sakeena', 16, 'S123')
    student2 = Student('Sara', 17, 'S124')

    # Registering students for courses
    student1.register_for_course(course1)
    student2.register_for_course(course2)

    # Creating an instructor
    instructor1 = Instructor('Mr. Hamzah Syed', 25, 50000)

    # Assigning instructor to a course
    course1.assign_instructor(instructor1)

    # Adding students to courses
    course1.add_student(student1)
    course2.add_student(student2)

    # Displaying information
    print("\n--- Students and their courses ---")
    student1.display_courses()
    student2.display_courses()

    print("\n--- Instructor and their courses ---")
    instructor1.display_courses()

    print("\n--- Course details ---")
    course1.display_course_info()
    course2.display_course_info()

if __name__ == '__main__':
    main()
