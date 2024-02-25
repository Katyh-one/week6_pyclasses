from person import Person

class Employee(Person):
    # init function assigns values to object properties
    def __init__(self, name, gender, dept):
        Person.__init__(self, name, gender)
        self._dept = dept
