class Employee(object):
    """Models real-life employees!"""
    def init(self, employeename):
        self.employeename = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

class PartTimeEmployee(Employee):
    def __init__(self, employee_name):
        def calculate_wage(self, hours):
            self.hours = hours
            return hours * 12.00

    def full_time_wage(self, hours):
        self.hours = hours
        return hours * 20.00
        return super(PartTimeEmployee, self).calculate_wage()

milton = PartTimeEmployee("milton")
print milton.full_time_wage(10)
        