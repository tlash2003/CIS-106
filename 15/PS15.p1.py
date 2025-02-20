# Employee class

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def bonus(self, rate):
        self.bonus_amount = rate * self.pay
        return self.bonus_amount

class Manager(Employee):
    def bonus(self, rate: float = 0.4) -> float:
        return rate * self.pay

class Executive(Employee):
    def bonus(self, rate: float = 2.0) -> float:
        return rate * self.pay

    def longtermbonus(self) -> float:
        return 0.5 * self.pay


# Creating objects of the class
emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

man1 = Manager("Sue", "Smith", 90000)
man2 = Manager("John", "Doe", 100000)

exec1= Executive("Jane", "Doe", 100000)
exec2 = Executive("John", "Smith", 110000)

# Example usage
bonus_rate = float(input("Enter the bonus rate: "))
print(emp1.first, emp1.bonus(bonus_rate))

print(man1.first, man1.bonus())
print(exec1.first, exec1.bonus())

