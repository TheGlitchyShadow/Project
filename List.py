classmates = ["Aarav", "Priya", "Rahul", "Sneha", "Dev"]
print("Class List:", classmates)

print("Total Students:", len(classmates))
print("First Student", classmates[0])
print("Last Student", classmates[-1])
print("First Three", classmates[:3])

classmates.append("Meera")
print("\nAfter adding Meera:", classmates)
classmates.remove("Dev")
print("After removing Dev:", classmates)
classmates.sort()
print("Sorted Alphabetically:", classmates)
classmates.reverse()
print("Reversed", classmates)

Teacher = {"Name" : "Mr. Sharma", "Subject" : "Python", "Experience" : 5}
print("\nTeacher Profile:", Teacher)

print("Subject", Teacher["Subject"])
print("Experience", Teacher.get("Experience", "Not found"))
Teacher["Experience"] = 6
Teacher["Email"] = "shamar@school.com"
Teacher.pop("Experience")
print("Updated Teacher Profile", Teacher)

roll_numbers = [1, 2, 3, 4, 5]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Meera"]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory)
print("Student at Roll 3:", student_directory[3])