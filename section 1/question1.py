class Employee:
     def __init__(self):
        self.__salary = 50000
     def increment(self):
        self.__salary += 1000   
     def deduct(self):
        self.__salary -= 5000
     def get_salary(self):
        print(f"current salary: {self.__salary}")      
emp1 = Employee()
emp2 = Employee()

print("For employee 1")
emp1.increment()
emp1.deduct()
emp1.get_salary()

print("For employee 2")
emp2.increment()
emp2.deduct()
emp2.get_salary()



