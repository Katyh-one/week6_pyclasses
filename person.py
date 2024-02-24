class Person:
    def __init__(self, name, gender):
        self._name = name
        self._gender = gender.upper()

    def __str__(self):
        # the string representation of the object
        # __str__ function controls what should be returned when the class object is str
        return "Name: " + self._name + \
            " Gender: " + self._gender


