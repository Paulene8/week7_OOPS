from week7_OOPS.Yuliannas.personPackage.person import Person


# inherits from the Person class. This means that Employee inherits the attributes and methods of the Person class.
class Employee(Person):
    # __init__ method initializes instances of the Employee class with five parameters: name, age, employee_id,
    # hourly_rate, and hours_worked. The super().__init__(name, age) line calls the constructor of the superclass
    # (Person) to initialise the name and age attributes inherited from the Person class. The employee_id, hourly_rate,
    # and hours_worked attributes are initialised with the provided values.
    def __init__(self, first_name, last_name, age, gender, employee_id, hourly_rate, hours_worked):
        super().__init__(first_name, last_name, age, gender)
        self._employee_id = employee_id
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    # decorator is used to define a getter method for the employee_id attribute, allowing access
    # to it as if it were a property of the Employee object.
    def get_employee_id(self):
        return self._employee_id

    # a setter method is defined for the employee_id attribute using @employee_id.setter,
    # which allows setting the value of the employee_id attribute.
    def set_employee_id(self, value):
        self._employee_id = value

    # Getter method for hourly_rate attribute
    def get_hourly_rate(self):
        return self._hourly_rate

    # Getter method for hours_worked attribute
    def get_hours_worked(self):
        return self._hours_worked

    def get_calculate_salary(self):
        # calculate_salary method calculates the salary of the employee based on their hourly rate, hours worked,
        # overtime pay, bonus, and deductions. If the hours_worked exceed 40, overtime pay is calculated at 1.5 times
        # the hourly rate for the extra hours. A fixed bonus amount is added to the base salary, and a fixed deduction
        # amount is subtracted.

        base_salary = self.get_hourly_rate() * self.get_hours_worked()

        # Example: Overtime pay calculation (assuming overtime rate is 1.5 times the hourly rate)
        if self.get_hours_worked() > 40:
            overtime_hours = self.get_hours_worked() - 40
            overtime_pay = overtime_hours * (self.get_hourly_rate() * 1.5)
            base_salary += overtime_pay

        # Example: Bonus calculation (assuming a fixed bonus amount)
        bonus = 1000  # Example bonus amount
        base_salary += bonus

        # Example: Deduction calculation (assuming a fixed deduction amount)
        deduction = 500  # Example deduction amount
        base_salary -= deduction

        return base_salary

    def __str__(self):
        return (f"First name: {self.firstname}\nLast name: {self.get_last_name()}\nAge: {self.get_age()}\n"
                f"Gender: {self.get_gender()}\nEmployee ID: {self.get_employee_id()}\nHourly Rate: {self.get_hourly_rate()}\n"
                f"Hours Worked: {self.get_hours_worked()}\nSalary: £{self.get_calculate_salary()}\n**************")
