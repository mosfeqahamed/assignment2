import json
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def display_student_info(self):
        self.display_person_info()
        print(f"ID: {self.student_id}")
        print(f"Enrolled Courses: {', '.join(self.courses)}")
        print(f"Grades: {self.grades}")

class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def display_course_info(self):
        print(f"Course Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor}")
        print("Enrolled Students:", ", ".join(self.students))      
    
class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self):
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        student_id = input("Enter Student ID: ")
        if student_id not in self.students:
            student = Student(name, age, address, student_id)
            self.students[student_id] = student
            print(f"Student: {name} (ID: {student_id}) added successfully.")
        else:
            print("Student ID already exists.")

    def add_course(self):
        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")
        instructor = input("Enter Instructor Name: ")
        if course_code not in self.courses:
            course = Course(course_name, course_code, instructor)
            self.courses[course_code] = course
            print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")
        else:
            print("Course code already exists.")

    def enroll_student_in_course(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course = self.courses[course_code]
            student.enroll_course(course.course_name)
            course.add_student(student.name)
            print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")
        else:
            print("Invalid Student ID or Course Code.")

    def add_grade_for_student(self):
        student_id = input("Enter Student ID: ")
        course_code = input("Enter Course Code: ")
        grade = input("Enter Grade: ")
        if student_id in self.students and course_code in self.courses:
            student = self.students[student_id]
            course_name = self.courses[course_code].course_name
            if course_name in student.courses:
                student.add_grade(course_name, grade)
                print(f"Grade {grade} added for {student.name} in {course_name}.")
            else:
                print("Student is not enrolled in this course.")
        else:
            print("Invalid Student ID or Course Code.")

    def display_student_details(self):
        student_id = input("Enter Student ID: ")
        if student_id in self.students:
            self.students[student_id].display_student_info()
        else:
            print("Student ID not found.")

    def display_course_details(self):
        course_code = input("Enter Course Code: ")
        if course_code in self.courses:
            self.courses[course_code].display_course_info()
        else:
            print("Course Code not found.")
    
    def save_data(self):
        data = {
            "students": {sid: {"name": student.name, "age": student.age, "address": student.address, "grades": student.grades, "courses": student.courses} for sid, student in self.students.items()},
            "courses": {cid: {"course_name": course.course_name, "course_code": course.course_code, "instructor": course.instructor, "students": course.students} for cid, course in self.courses.items()},
        }
        with open("student_data.json", "w") as f:
            json.dump(data, f)
        print("All student and course data saved successfully.")

    def load_data(self):
        try:
            with open("student_data.json", "r") as f:
                data = json.load(f)
                for sid, info in data["students"].items():
                    student = Student(info["name"], info["age"], info["address"], sid)
                    student.grades = info["grades"]
                    student.courses = info["courses"]
                    self.students[sid] = student
                for cid, info in data["courses"].items():
                    course = Course(info["course_name"], cid, info["instructor"])
                    course.students = info["students"]
                    self.courses[cid] = course
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")
            
    def run(self):
        while True:
            print("\n==== Student Management System ====")
            print("1. Add New Student")
            print("2. Add New Course")
            print("3. Enroll Student in Course")
            print("4. Add Grade for Student")
            print("5. Display Student Details")
            print("6. Display Course Details")
            print("7. Save Data to File")
            print("8. Load Data from File")
            print("0. Exit")
            choice = input("Select Option: ")
            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_course()
            elif choice == "3":
                self.enroll_student_in_course()
            elif choice == "4":
                self.add_grade_for_student()
            elif choice == "5":
                self.display_student_details()
            elif choice == "6":
                self.display_course_details()
            elif choice == "7":
                self.save_data()
            elif choice == "8":
                self.load_data()
            elif choice == "0":
                print("Exiting Student Management System. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")


system = StudentManagementSystem()
system.run()