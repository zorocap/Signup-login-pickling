from student import Student
import pickle

s1=Student("Vansh", 55, "Male")
with open("student.pickle", "wb") as f:
    pickle.dump(s1,f)