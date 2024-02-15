# from student import Student
import pickle

with open("student.pickle", "rb") as f:
    obj=pickle.load(f)

obj.display()