# This is code for OOPS concepts. Time:8:40P.M

# First : Basic Class, Object, __init__, and self. 

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand;
#         self.model = model;

# my_car = Car("Tata","Nano");
# print(my_car.brand);
# print(my_car.model);

#Second: Inheritance.
class Info:
  def __init__(self, name, age,city):
    self.name = name;
    self.age = age;
    self.city = city;

  def Sentence(self):
      return f"{self.name} is {int(self.age)} years old and is from {self.city}"
    
Person1 = Info("person1",19,"jabalpur");
print(Person1.Sentence())



    