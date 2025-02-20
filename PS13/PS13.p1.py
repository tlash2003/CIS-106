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

# Creating objects of the class
emp1 = Employee("Corey", "Schafer", 50000)
emp2 = Employee("Test", "User", 60000)

# Example usage
bonus_rate = float(input("Enter the bonus rate: "))
print(emp1.bonus(bonus_rate))