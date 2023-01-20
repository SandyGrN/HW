class Student:
    pass

class Marks:
    pass


ann = Student()
nice = Marks()

#check whether created instances are instances of the said classes or not

print(isinstance(ann, Student))
print(isinstance(nice, Marks))

print(isinstance(ann, Marks))
print(isinstance(nice, Student))
 
#Check whether the said classes are subclasses of the built-in object class or not.
print(issubclass(Student, object))
print(issubclass(Marks, object)) 