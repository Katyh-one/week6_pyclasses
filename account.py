# this is our capsule
# it's a collection of attributes(properties) and methods
import sys
from datetime import date


def verify_pin(pin, supplied_pin, attempts, max_num_attempts=3):
    if supplied_pin in pin:
        return 'Welcome how can I help?'
    elif supplied_pin not in pin and attempts < 3:
        remaining_attempts = max_num_attempts - attempts
        return f'Your pin is incorrect, you have {remaining_attempts} left.'
    else:
        return 'Your account is now locked. Have a nice day!'


def write_report(statement, firstname, lastname, initialbalance, depositamount, newbalance):
    today = date.today()
    statement.write(f'Hello {firstname} {lastname}\n' + ('*' * 50) + '\n')
    statement.write(f'Statement date: {today}\n')
    statement.write(f'Your starting balance was {initialbalance}\n')
    statement.write(f'You deposited {depositamount}\n')
    statement.write(f'Your new balance is {newbalance}')
    statement.close()


class Account:
    # public class variable
    numCreated = 0
    pin = '1234'

    # special method called the constructor - dunder
    # a constructor method is used to get your object ready to be used
    #  preparatory to work
    # bring our object to life in a usable state
    # self object pointer - point to who ever bank account is calling the deposit method on
    # in java c# it's this instead of self
    # implicit parameter instance self

    def __init__(self, initial_amount, firstname, lastname):
        # _balance is an attribute - piece of data
        # single underscore is semi private
        self.supplied_pin = ''
        self._balance = initial_amount
        self.first_name = firstname
        # dunder on a field means private keep out
        # encapsulation - appropriate level of hiding stuff
        # double underscore means fully private
        self.__last_name = lastname
        # private class variable
        Account.numCreated += 1

    # methods about behaviour
    #     all methods - functions defined within a class
    # first argument passed to a method is usually called self
    def get_pin(self):
        self.supplied_pin = input('Enter your pin: ')
        return self.supplied_pin

    def deposit(self):
        amount = int(input("Enter amount to be deposited: "))
        self._balance += amount
        return amount

    # method
    def withdraw(self, amount):
        if amount >= 0:
            self._balance -= amount
            # else situation we would raise an exception

    # this is what java calls a getter
    # java uses these to retrieve attribute values
    # method that is getting data - not functionality based method
    #  data retrieval method
    def getbalance(self):
        return self._balance

    #  create a getter method to retrieve the first_name attribute
    # getter method starts with get
    def get_firstname(self):
        return self.first_name

    # getter method can change how presents
    def get_last_name(self):
        return self.__last_name.upper()

    # setter - write a piece of information
    # getters read
    # setters have parameters
    def set_lastname(self, new_lastname):
        self.__last_name = new_lastname
        return self.__last_name

        # getters can translate or modify the data before returning it
        #  setters often validate the incoming data
        # setters often contain if statements - if its in allowed range or if it's in this list
    def set_firstname(self, new_firstname):
        self.first_name = new_firstname

    def __str__(self):
        return f"Account\nFirstname: {self.get_firstname()}\nLastname: {self.get_last_name()}"\
                f"\nBalance: ${self.getbalance()}\n************"

