from salaries import get_salary as gs

class Worker:
    name = ''
    age = ''

    def __init__(self, name, age, wrks_list):
        self.name = name
        self.age = age
        self.list = wrks_list
        print(f"Created {self.age} year-old {self.__class__.__name__.lower()} {self.name} with {self.salary} salary")
        wrks_list.append(self)

    def __str__(self):
        return f"{self.name}, {self.age} y.o., salary {self.salary}"

    def fire(self):
        self.list.remove(self)
        print(f"{self.name} was fired")


class Builder(Worker):
    ability = 'build something'

    def __init__(self, name, age, lst):
        self.salary = gs(self.__class__.__name__)
        super().__init__(name, age, lst)

class Programmer(Worker):
    ability = 'programm something'

    def __init__(self, name, age, lst):
        self.salary = gs(self.__class__.__name__) 
        super().__init__(name, age, lst)

wrks_list = []
w1 = Builder("Vasya", 25, wrks_list)
w2 = Builder("Kolya", 38, wrks_list)
w3 = Programmer("Pyotr", 19, wrks_list)
w4 = Programmer("Nikita", 19, wrks_list)
print("Meet", w1)
w2.fire()

print("Currently working: " + ", ".join([f"{w.__class__.__name__.lower()} {w.name}" for w in wrks_list]))