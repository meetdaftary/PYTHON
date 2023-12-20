class Employee:
    def __init__(self, name, emp_id, e_type):
        self.name = name
        self.emp_id = emp_id
        self.e_type=e_type

    def display_info(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Type:{self.e_type}"

class Developer(Employee):
    def __init__(self, name, emp_id, e_type):
        super().__init__(name, emp_id,e_type)

class Tester(Employee):
    def __init__(self, name, emp_id, e_type):
        super().__init__(name, emp_id,e_type)

class Manager(Employee):
    def __init__(self, name, emp_id,e_type):
        super().__init__(name, emp_id,e_type)
        self.managed_employees = []

    def add_employee(self, employee):
        self.managed_employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.managed_employees:
            self.managed_employees.remove(employee)
        else:
            print(f"{employee.name} not found in managed employees.")

    def display_managed_employees(self):
        print(f"Employees managed by {self.name}:")
        for emp in self.managed_employees:
            print(emp.display_info())



# Creating employees
dev1 = Developer("Leo Messi", 101, "Developer")
tester1 = Tester("Cristiano Ronaldo", 102, "Tester")

# Creating manager
manager = Manager("MEET DAFTARY", 100,"Manager")

# Manager managing employees
manager.add_employee(dev1)
manager.add_employee(tester1)

# Displaying managed employees by manager
manager.display_managed_employees()

# Removing an employee
manager.remove_employee(tester1)

# Displaying managed employees after removal
manager.display_managed_employees()