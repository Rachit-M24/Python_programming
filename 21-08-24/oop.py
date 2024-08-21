# This is code for OOPS concepts. Time:8:40P.M

# First : Basic Class, Object, __init__, and self. 

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand;
#         self.model = model;

# my_car = Car("Tata","Nano");
# print(my_car.brand);
# print(my_car.model);

# This is code for OOPS concepts. Time:9:30P.M

#Second: Inheritance.

# class Info:
#   def __init__(self, name, age,city):
#     self.name = name;
#     self.age = age;
#     self.city = city;

#   def Sentence(self):
#       return f"{self.name} is {int(self.age)} years old and is from {self.city}"

# class Employee(Info):
#   def __init__(self,name, age,current_city,job_role):
#        self.current_city = current_city;
#        self.job_role = job_role;
#        super().__init__(name, age , city = current_city)

# Person1 = Info("Raju",19,"jabalpur");
# print(Person1.Sentence())

# Employee1 = Employee("Raju",22,"lucknow","SDE")
# print(f"{Employee1.Sentence()} working as {Employee1.job_role}")




    