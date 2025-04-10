class Student:
     
     classyear = 2027
     # this is the class variable this can be accessed by any instance of the class.
     num_student = 0
     def __init__(self,name,age):
          
         self.name = name;  #here these are the instance variable of the this class every instance of this  class will have these variables separately

         self.age = age;
         Student.num_student=Student.num_student+1
         
student1 = Student("Vighnesh",20)
student2 = Student("Suresh",20)
student3 = Student("Ritik",19)

# print(student1.name)
# print(student2.name)
# print(Student.classyear)
# print(Student.classyear)
# print(Student.num_student)
print(f"My Graduating year will be {Student.classyear} and the number of the student that i am graduation with is {Student.num_student}.")
print(student1.name)
print(student2.name)
print(student3.name)
